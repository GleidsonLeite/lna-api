from PySpice.Spice.Netlist import SubCircuit


class LNASubCircuit(SubCircuit):
    NODES = ("INP", "OUT")

    def __init__(
        self,
        name: str,
        nfet_type: str,
        pfet_type: str,
    ) -> None:
        super().__init__(name, *self.NODES)

        self.L("LG", "INP", "PLG", 5.8e-9)
        self.R("RPOL1", "PLG", "VPOL1", 19939)
        self.V("VPOL1", "VPOL1", 0, 0.9)

        self.X(
            "M1",
            nfet_type,
            "PRF",
            "PLG",
            0,
            0,
            L=2.2,
            W=68.3,
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

        self.C("C1", "PC1", "PLG", 19.7e-12)
        self.R("RF", "PC1", "PRF", 19540)

        self.X(
            "M2",
            pfet_type,
            "VCC",
            "PC1",
            "PRF",
            0,
            L=39.9,
            W=1.1,
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
        self.C("CDEC", "VCC", 0, 1e-6)
        self.C("CM1", "PRF", "PCM1", 4.7e-12)
        self.R("RPOL2", "PCM1", "VPOL2", 13548)

        self.X(
            "M3",
            nfet_type,
            "PM3",
            "PCM1",
            0,
            0,
            L=48,
            W=6.5,
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
        self.L("LPK", "VDD", "PM3", 7.6e-9)
        self.C("CM2", "PM3", "OUT", 0.65e-12)
        self.C("CM3", "OUT", 0, 4.7e-12)

        self.V("VCC", "VCC", 0, 1.8)
        self.V("VDD", "VDD", 0, 1.8)
        self.V("VPOL2", "VPOL2", 0, 0.53)
