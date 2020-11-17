import time

from .matrix import Matrix


class MatrixPrinter:
    """This class needs for printing matrix."""

    def __init__(self, matrix: Matrix, speed: int) -> None:
        """
        Args:
            matrix (Matrix): matrix
            speed (int): lines per second
        """

        self.matrix = matrix
        self.delay = 1 / speed

    def run(self) -> None:
        """Runs printing matrix."""

        try:
            while True:
                print(self.matrix.gen_new_line())
                time.sleep(self.delay)
        except KeyboardInterrupt:
            pass
