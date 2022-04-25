from PySpice.Probe.WaveForm import AcAnalysis
from PySpice.Spice.Netlist import Circuit
from PySpice.Spice.NgSpice.Shared import NgSpiceShared
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

        try:
            analysis = simulator.ac(
                start_frequency=start_frequency,
                stop_frequency=stop_frequency,
                number_of_points=number_of_points,
                variation=variation,
            )
        except Exception as exception:
            ngspice: NgSpiceShared = simulator.ngspice
            try:
                ngspice.quit()
            except:
                pass
            raise exception

        ngspice: NgSpiceShared = simulator.ngspice
        ngspice.remove_circuit()
        ngspice.destroy()

        return analysis
