from matplotlib import pyplot as plt
import numpy as np
from PySpice.Spice.Netlist import Circuit
from subCircuits import SPARAM

circuit = Circuit("Test")
sparam = SPARAM("sparam")

circuit.subcircuit(sparam)

circuit.C("1", "in", 0, 33.2e-12)
circuit.L("1", "in", 2, 99.2e-9)
circuit.C("2", 2, 0, 57.2e-12)
circuit.L("2", 2, "out", 99.2e-9)
circuit.C("3", "out", 0, 33.2e-12)

circuit.X(1, "sparam", "in", "out", "S22", "S12")

simulator = circuit.simulator(temperature=25, nominal_temperature=25)
analysis = simulator.ac(
    start_frequency=2.5e6,
    stop_frequency=250e6,
    number_of_points=100,
    variation="lin",
)

sparam.Vdc.dc_value = np.abs(analysis.nodes["x1.1"].as_ndarray())[0]
sparam.Vacdc.dc_value = np.abs(analysis.nodes["x1.8"].as_ndarray())[0]
sparam.RS1.resistance = 1e12
sparam.RS2.resistance = 1e12
sparam.RS3.resistance = 1e-3
sparam.RS4.resistance = 1e-3

simulator2 = circuit.simulator(temperature=25, nominal_temperature=25)
analysis2 = simulator2.ac(
    start_frequency=2.5e6,
    stop_frequency=250e6,
    number_of_points=100,
    variation="lin",
)


S11 = 20 * np.log10(np.abs(analysis2.s12.as_ndarray()))
S12 = 20 * np.log10(np.abs(analysis.s12.as_ndarray()))
S21 = 20 * np.log10(np.abs(analysis2.s22.as_ndarray()))
S22 = 20 * np.log10(np.abs(analysis.s22.as_ndarray()))

plt.subplot(2, 2, 1)
plt.plot(analysis.frequency, S11, label="S11")
plt.legend()
plt.xlabel("Frequency [Hz]")
plt.ylabel("dB")
plt.subplot(2, 2, 2)
plt.plot(analysis.frequency, S12, label="S12")
plt.legend()
plt.xlabel("Frequency [Hz]")
plt.ylabel("dB")
plt.subplot(2, 2, 3)
plt.plot(analysis.frequency, S21, label="S21")
plt.legend()
plt.xlabel("Frequency [Hz]")
plt.ylabel("dB")
plt.subplot(2, 2, 4)
plt.plot(analysis.frequency, S22, label="S22")
plt.legend()
plt.xlabel("Frequency [Hz]")
plt.ylabel("dB")
plt.tight_layout()
plt.show()
