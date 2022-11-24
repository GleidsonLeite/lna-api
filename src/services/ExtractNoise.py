from typing import Literal
from PySpice.Spice.Netlist import SubCircuit
from circuits import Circuit
from PySpice.Spice.NgSpice.Shared import NgSpiceShared
from PySpice.Probe.WaveForm import NoiseAnalysis
from PySpice.Spice.NgSpice.Simulation import NgSpiceSharedCircuitSimulator


class ExtractNoiseService:
    @staticmethod
    def execute(
        sub_circuit: SubCircuit,
        start_frequency: float,
        stop_frequency: float,
        number_of_points: int,
        simulator: Literal[
            "ngspice-subprocess",
            "ngspice-shared",
        ] = "ngspice-shared",
        temperature: float = 25,
        nominal_temperature: float = 25,
        variation: Literal["dec", "oct", "lin"] = "lin",
    ) -> NoiseAnalysis:
        circuit = Circuit("test")
        circuit.SinusoidalVoltageSource("inp", "net1", 0)
        circuit.subcircuit(subcircuit=sub_circuit)
        circuit.X(1, sub_circuit.name, "inp", "out")
        circuit.R("1", "net1", "inp", 50)
        simulator: NgSpiceSharedCircuitSimulator = circuit.simulator(
            temperature=temperature,
            nominal_temperature=nominal_temperature,
        )
        simulator.ngspice.set("sqrnoise")
        print(simulator.ngspice.ngspice_version)

        try:
            analysis: NoiseAnalysis = simulator.noise(
                output_node="out",
                ref_node="0",
                src="Vinp",
                variation=variation,
                points=number_of_points,
                start_frequency=start_frequency,
                stop_frequency=stop_frequency,
            )
        except Exception as exception:
            ngspice: NgSpiceShared = simulator.ngspice
            try:
                ngspice.quit()
            except:
                pass
            finally:
                raise exception
        ngspice: NgSpiceShared = simulator.ngspice
        ngspice.remove_circuit()
        ngspice.destroy()

        return analysis
