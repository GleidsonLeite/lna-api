from PySpice.Spice.Netlist import SubCircuit


class TestSubCircuit(SubCircuit):
    NODES = ("in", "out")

    def __init__(self, name: str):
        super().__init__(name, *self.NODES)

        self.C("1", "in", 0, 33.2e-12)
        self.L("1", "in", 2, 99.2e-9)
        self.C("2", 2, 0, 57.2e-12)
        self.L("2", 2, "out", 99.2e-9)
        self.C("3", "out", 0, 33.2e-12)
