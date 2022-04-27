from typing import Literal
from PySpice.Spice.Netlist import SubCircuit
from circuits import Circuit
from entities import SParameters
from services.SimulateAC import SimulateACService
from subCircuits import SPARAM


class ExtractSParametersService:
    @staticmethod
    def execute(
        sub_circuit: SubCircuit,
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
    ) -> SParameters:

        circuit = Circuit("Test")
        sparam = SPARAM("sparam", Vbias_in=1)
        circuit.subcircuit(sparam)
        circuit.subcircuit(sub_circuit)

        circuit.X(1, sparam.name, "inp", "out")
        circuit.X(2, sub_circuit.name, "inp", "out")
        analysis = SimulateACService.execute(
            circuit=circuit,
            start_frequency=start_frequency,
            stop_frequency=stop_frequency,
            number_of_points=number_of_points,
            simulator=simulator,
            nominal_temperature=nominal_temperature,
            temperature=temperature,
            variation=variation,
        )
        S11 = 2 * analysis.inp.as_ndarray() - 1
        S21 = 2 * analysis.out.as_ndarray()

        circuit = Circuit("Test")
        sparam = SPARAM("sparam", Vbias_out=1)
        circuit.subcircuit(sparam)
        circuit.subcircuit(sub_circuit)

        circuit.X(1, sparam.name, "inp", "out")
        circuit.X(2, sub_circuit.name, "inp", "out")
        analysis = SimulateACService.execute(
            circuit=circuit,
            start_frequency=start_frequency,
            stop_frequency=stop_frequency,
            number_of_points=number_of_points,
            simulator=simulator,
            nominal_temperature=nominal_temperature,
            temperature=temperature,
            variation=variation,
        )

        S12 = 2 * analysis.inp.as_ndarray()
        S22 = 2 * analysis.out.as_ndarray() - 1

        s_parameters = SParameters(
            frequency=analysis.frequency,
            S11=S11,
            S12=S12,
            S21=S21,
            S22=S22,
        )

        return s_parameters
