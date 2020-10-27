import argparse
import os

from .argparser import setup_argparser
from .matrix import Matrix
from .matrix_printer import MatrixPrinter


def main() -> None:
    argparser = argparse.ArgumentParser("matrix")
    setup_argparser(argparser)
    args = argparser.parse_args()

    term_size = os.get_terminal_size()
    matrix = Matrix(term_size.columns, term_size.lines, args.color, args.chars)
    printer = MatrixPrinter(matrix, args.speed)
    printer.run()


if __name__ == "__main__":
    main()
