import argparse

from .consts import AVAILABLE_COLORS
from .defaults import DEFAULT_CHARS, DEFAULT_COLOR, DEFAULT_SPEED


def setup_argparser(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--color", "-c", default=DEFAULT_COLOR,
                        choices=AVAILABLE_COLORS, help="matrix characters color")
    parser.add_argument("--speed", "-s", type=int,
                        default=DEFAULT_SPEED, help="lines per second")
    parser.add_argument("--chars", "-ch", type=list, default=DEFAULT_CHARS,
                        help="matrix will consist of these characters")
