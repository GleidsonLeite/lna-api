from PySpice.Spice.Netlist import SubCircuit


class LNATBSubCircuit(SubCircuit):
    NODES = ("INP", "OUT")

    def __init__(
        self,
        name: str,
        nfet_type: str,
        vdd: float,
        R1: float,
        l3: float,
        w3: float,
        R2: float,
        LG: float,
        w1: float,
        l1: float,
        LS: float,
        l2: float,
        w2: float,
        RTANk: float,
        CTANK: float,
        LTANK: float,
        CG: float,
    ):
        super().__init__(name, *self.NODES)

        self.V("VDD", "VDD", 0, vdd)
        self.R("R1", "R1", "VD3", R1)
        self.X(
            "M3",
            nfet_type,
            "VD3",
            "VD3",
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
        self.R("R2", "VD3", "VG1", R2)
        self.C("CG", "VG1", "INP", CG)
        self.L("LG", "VG1", "VG", LG)
        self.X(
            "M1",
            nfet_type,
            "VD1",
            "VG",
            "LS",
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
        self.L("LS", "LS", 0, LS)
        self.X(
            "M2",
            nfet_type,
            "OUT",
            "VDD",
            "VD1",
            0,
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
        self.R("RTANK", "VDD", "OUT", RTANk)
        self.C("CTANK", "VDD", "OUT", CTANK)
        self.L("LTANK", "VDD", "OUT", LTANK)
