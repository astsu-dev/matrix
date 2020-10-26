import time

from .matrix import Matrix


class MatrixPrinter:
    def __init__(self, matrix: Matrix, delay: float) -> None:
        self.matrix = matrix
        self.delay = delay

    def run(self) -> None:
        try:
            while True:
                print(self.matrix.gen_new_line())
                time.sleep(self.delay)
        except KeyboardInterrupt:
            pass
