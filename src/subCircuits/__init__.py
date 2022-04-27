from PySpice.Spice.Netlist import SubCircuit


class SPARAM(SubCircuit):
    NODES = ("p1", "p2")

    def __init__(
        self,
        name: str,
        Vbias_in: float = 0,
        Vbias_out: float = 0,
        Rbase: float = 50,
    ):
        super().__init__(name, *self.NODES)

        self.SinusoidalVoltageSource("1", 1, 0, 0, Vbias_in)
        self.R(1, "p1", 1, Rbase)
        self.R(2, "p2", 2, Rbase)
        self.SinusoidalVoltageSource("2", 2, 0, 0, Vbias_out)
