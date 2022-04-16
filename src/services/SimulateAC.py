from PySpice.Probe.WaveForm import AcAnalysis
from PySpice.Spice.Netlist import Circuit
from typing import Literal


class SimulateACService:
    @staticmethod
    def execute(
        circuit: Circuit,
        start_frequency: float,
        stop_frequency: float,
        number_of_points: float,
        simulator: Literal[
            "ngspice-subprocess",
            "ngspice-shared",
        ] = "ngspice-shared",
        temperature: float = 25,
        nominal_temperature: float = 25,
        variation: Literal["dec", "oct", "lin"] = "lin",
    ) -> AcAnalysis:
        simulator = circuit.simulator(
            temperature=temperature,
            nominal_temperature=nominal_temperature,
        )

        analysis = simulator.ac(
            start_frequency=start_frequency,
            stop_frequency=stop_frequency,
            number_of_points=number_of_points,
            variation=variation,
        )

        return analysis
