from matplotlib import pyplot as plt
from src.configuration import skywater_configuration
from src.services.ExtractSParameters import ExtractSParametersService
from src.subCircuits.LNA import LNASubCircuit

test_subcircuit = LNASubCircuit(
    "test",
    nfet_type=skywater_configuration.nfet_type,
    pfet_type=skywater_configuration.pfet_type,
)
s_parameters = ExtractSParametersService.execute(
    test_subcircuit, 2.3e9, 2.5e9, 100
)


plt.subplot(2, 2, 1)
plt.plot(s_parameters.frequency, s_parameters.S11_db, label="S11")
plt.legend()
plt.xlabel("Frequency [Hz]")
plt.ylabel("dB")
plt.subplot(2, 2, 2)
plt.plot(s_parameters.frequency, s_parameters.S12_db, label="S12")
plt.legend()
plt.xlabel("Frequency [Hz]")
plt.ylabel("dB")
plt.subplot(2, 2, 3)
plt.plot(s_parameters.frequency, s_parameters.S21_db, label="S21")
plt.legend()
plt.xlabel("Frequency [Hz]")
plt.ylabel("dB")
plt.subplot(2, 2, 4)
plt.plot(s_parameters.frequency, s_parameters.S22_db, label="S22")
plt.legend()
plt.xlabel("Frequency [Hz]")
plt.ylabel("dB")
plt.tight_layout()
plt.show()
