from typing import Literal
from PySpice.Spice.Netlist import Circuit, SubCircuit
import numpy as np
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
        sparam = SPARAM("sparam")
        circuit.subcircuit(sparam)
        circuit.subcircuit(sub_circuit)

        circuit.X(1, "sparam", "in", "out", "S22", "S12")
        circuit.X(2, sub_circuit.name, "in", "out")

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

        sparam.Vdc.dc_value = np.abs(analysis.nodes["x1.1"].as_ndarray())[0]
        sparam.Vacdc.dc_value = np.abs(analysis.nodes["x1.8"].as_ndarray())[0]
        sparam.RS1.resistance = 1e12
        sparam.RS2.resistance = 1e12
        sparam.RS3.resistance = 1e-3
        sparam.RS4.resistance = 1e-3

        analysis2 = SimulateACService.execute(
            circuit=circuit,
            start_frequency=start_frequency,
            stop_frequency=stop_frequency,
            number_of_points=number_of_points,
            simulator=simulator,
            nominal_temperature=nominal_temperature,
            temperature=temperature,
            variation=variation,
        )

        s_parameters = SParameters(
            frequency=analysis.frequency,
            S11=analysis2.s12.as_ndarray(),
            S12=analysis.s12.as_ndarray(),
            S21=analysis2.s22.as_ndarray(),
            S22=analysis.s22.as_ndarray(),
        )

        return s_parameters
