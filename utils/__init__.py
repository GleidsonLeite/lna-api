import numpy as np
from numpy.typing import NDArray


def convert_to_db(x: NDArray) -> NDArray:
    return 20 * np.log10(np.abs(x))
