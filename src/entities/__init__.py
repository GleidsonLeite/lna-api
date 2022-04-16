from dataclasses import dataclass
from numpy.typing import NDArray

from utils import convert_to_db


@dataclass
class SParameters:
    S11: NDArray
    S12: NDArray
    S21: NDArray
    S22: NDArray
    frequency: NDArray

    @property
    def S11_db(self) -> NDArray:
        return convert_to_db(self.S11)

    @property
    def S12_db(self) -> NDArray:
        return convert_to_db(self.S12)

    @property
    def S21_db(self) -> NDArray:
        return convert_to_db(self.S21)

    @property
    def S22_db(self) -> NDArray:
        return convert_to_db(self.S22)
