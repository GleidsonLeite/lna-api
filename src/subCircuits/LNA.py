from PySpice.Spice.Netlist import SubCircuit


class LNASubCircuit(SubCircuit):
    NODES = ("INP", "OUT")

    def __init__(
        self,
        name: str,
        nfet_type: str,
        pfet_type: str,
        lg: float,
        rpol1: float,
        vpol1: float,
        w1: float,
        w2: float,
        l1: float,
        l2: float,
        c1: float,
        rf: float,
    ) -> None:
        super().__init__(name, *self.NODES)

        self.V("CC", "VCC", 0, 1.8)
        self.C("dec", "VCC", 0, 1e-6)

        self.X(
            "M2",
            pfet_type,
            "OUT",
            "PRF",
            "VCC",
            "VCC",
            L=l2,
            W=w2,
            ad="'W * 0.29'",
            pd="'W + 2 * 0.29'",
            as_="'W * 0.29'",
            ps="'W + 2 * 0.29'",
            nrd=0,
            nrs=0,
            sa=0,
            sb=0,
            sd=0,
            nf=1,
            mult=1,
        )
        self.X(
            "M1",
            nfet_type,
            "OUT",
            "INP1",
            0,
            0,
            L=l1,
            W=w1,
            ad="'W * 0.29'",
            pd="'W + 2 * 0.29'",
            as_="'W * 0.29'",
            ps="'W + 2 * 0.29'",
            nrd=0,
            nrs=0,
            sa=0,
            sb=0,
            sd=0,
            nf=1,
            mult=1,
        )

        self.R("f", "OUT", "PRF", rf)
        self.C("1", "INP1", "PRF", c1)
        self.R("pol1", "INP1", "pol1", rpol1)
        self.V("pol1", "pol1", 0, vpol1)
        self.L("g", "inp", "inp1", lg)
