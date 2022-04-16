from dataclasses import dataclass
from typing import List


@dataclass
class SkyWaterConfiguration:
    libraries: List[str]
    nfet_type: str = "sky130_fd_pr__nfet_01v8"
    pfet_type: str = "sky130_fd_pr__pfet_01v8"


skywater_configuration = SkyWaterConfiguration(
    libraries=[
        "/edatools/skywater-pdk/libraries/sky130_fd_pr/latest/models/corners/tt.spice"
    ]
)
