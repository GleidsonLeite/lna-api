from PySpice.Spice.Netlist import SubCircuit


class SPARAM(SubCircuit):
    NODES = (22, 66, 5, 7)

    def __init__(
        self,
        name: str,
        Vbias_in: float = 0,
        Vbias_out: float = 0,
        Rbase: float = 50,
    ):
        super().__init__(name, *self.NODES)

        self.R("S1", 22, 2, 0.001)
        self.R("S2", 66, 6, 0.001)
        self.R("S3", 22, 5, 1e12)
        self.R("S4", 66, 2, 1e12)
        self.SinusoidalVoltageSource("acdc", 1, 0, Vbias_in, 1)
        self.R(1, 1, 2, Rbase)
        self.VoltageControlledVoltageSource(1, 3, 0, 2, 0, 2)
        self.SinusoidalVoltageSource("ac", 3, 4, 0, 1)
        self.R("_loop", 4, 5, 0.001)
        self.R(3, 5, 0, 1)
        self.VoltageControlledVoltageSource(2, 7, 0, 6, 0, 2)
        self.R(4, 6, 8, Rbase)
        self.SinusoidalVoltageSource("dc", 8, 0, Vbias_out, 0)
