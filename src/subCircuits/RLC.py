from PySpice.Spice.Netlist import SubCircuit


class RLCSubCircuit(SubCircuit):
    NODES = ("INP", "OUT")

    def __init__(
        self, name: str, inductance: float, capacitance: float, resistance: float
    ):
        super().__init__(name, *self.NODES)

        self.C("C", "INP", "OUT", capacitance)
        self.R("R", "INP", "OUT", resistance)
        self.L("L", "INP", "OUT", inductance)
