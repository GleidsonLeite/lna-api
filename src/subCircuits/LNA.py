from PySpice.Spice.Netlist import SubCircuit


class LNASubCircuit(SubCircuit):
    NODES = ("INP", "OUTBUFFER")

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
        w3: float,
        l1: float,
        l2: float,
        l3: float,
        c1: float,
        rf: float,
        cm1: float,
        cm2: float,
        cm3: float,
        rpol2: float,
        vpol2: float,
        lpk: float,
        vcc: float,
        vdd: float,
    ) -> None:
        super().__init__(name, *self.NODES)

        self.V("CC", "VCC", 0, vcc)
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
        self.C(1, "INP1", "PRF", c1)
        self.R("pol1", "INP1", "pol1", rpol1)
        self.V("pol1", "pol1", 0, vpol1)
        self.L("g", "inp", "inp1", lg)

        # Buffer

        self.C("M1", "OUT", "BUFFER", cm1)
        self.R("pol2", "BUFFER", "pol2", rpol2)
        self.V("pol2", "pol2", 0, vpol2)

        self.X(
            "M3",
            nfet_type,
            "PK",
            "BUFFER",
            0,
            0,
            L=l3,
            W=w3,
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

        self.L("pk", "DD", "PK", lpk)
        self.V("DD", "DD", 0, vdd)
        self.C("M2", "PK", "OUTBUFFER", cm2)
        self.C("M3", "OUTBUFFER", 0, cm3)
