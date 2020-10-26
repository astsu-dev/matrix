import os

from .matrix import Matrix
from .matrix_printer import MatrixPrinter


def main() -> None:
    term_size = os.get_terminal_size()
    matrix = Matrix(term_size.columns, term_size.lines, "green")
    printer = MatrixPrinter(matrix, 1 / 40)
    printer.run()


if __name__ == "__main__":
    main()
