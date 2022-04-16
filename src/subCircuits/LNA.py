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
        rpol2: float,
        vpol1: float,
        vpol2: float,
        w1: float,
        w2: float,
        w3: float,
        l1: float,
        l2: float,
        l3: float,
        c1: float,
        rf: float,
        cdec: float,
        cm1: float,
        cm2: float,
        cm3: float,
        lpk: float,
    ) -> None:
        super().__init__(name, *self.NODES)

        self.L("LG", "INP", "PLG", lg)
        self.R("RPOL1", "PLG", "VPOL1", rpol1)
        self.V("VPOL1", "VPOL1", 0, vpol1)

        self.X(
            "M1",
            nfet_type,
            "PRF",
            "PLG",
            0,
            0,
            L=l1,
            W=w1,
            ad="'W*0.29'",
            pd="'2*(W+0.29)'",
            as_="'W*0.29'",
            ps="'2*(W+0.29)'",
            nrd="'0.29/W'",
            nrs="'0.29/W'",
            sa=0,
            sb=0,
            sd=0,
            nf=1,
            mult=1,
        )

        self.C("C1", "PC1", "PLG", c1)
        self.R("RF", "PC1", "PRF", rf)

        self.X(
            "M2",
            pfet_type,
            "VCC",
            "PC1",
            "PRF",
            0,
            L=l2,
            W=w2,
            ad="'W*0.29'",
            pd="'2*(W+0.29)'",
            as_="'W*0.29'",
            ps="'2*(W+0.29)'",
            nrd="'0.29/W'",
            nrs="'0.29/W'",
            sa=0,
            sb=0,
            sd=0,
            nf=1,
            mult=1,
        )
        self.C("CDEC", "VCC", 0, cdec)
        self.C("CM1", "PRF", "PCM1", cm1)
        self.R("RPOL2", "PCM1", "VPOL2", rpol2)

        self.X(
            "M3",
            nfet_type,
            "PM3",
            "PCM1",
            0,
            0,
            L=l3,
            W=w3,
            ad="'W*0.29'",
            pd="'2*(W+0.29)'",
            as_="'W*0.29'",
            ps="'2*(W+0.29)'",
            nrd="'0.29/W'",
            nrs="'0.29/W'",
            sa=0,
            sb=0,
            sd=0,
            nf=1,
            mult=1,
        )
        self.L("LPK", "VDD", "PM3", lpk)
        self.C("CM2", "PM3", "OUT", cm2)
        self.C("CM3", "OUT", 0, cm3)

        self.V("VCC", "VCC", 0, 1.8)
        self.V("VDD", "VDD", 0, 1.8)
        self.V("VPOL2", "VPOL2", 0, vpol2)
