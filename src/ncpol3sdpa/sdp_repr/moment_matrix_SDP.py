from typing import List, Tuple


class MomentMatrixSDP:
    """This is an represents size x size symmetric positive
    matrix variable. The coefficients in each equivalence class are considered to be equal"""

    def __init__(self, size: int, eq_classes: List[List[Tuple[int, int]]]):
        self.size = size
        self.eq_classes = eq_classes

        # Validation
        once = set()
        for eq_class in eq_classes:
            for i, j in eq_class:
                assert 0 <= i < size
                assert (i, j) not in once
                once.add((i, j))
