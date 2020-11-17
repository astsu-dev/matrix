import random
from typing import List

import termcolor

from .typedefs import TermColor


class VLine:
    """This class represents matrix vertical line."""

    def __init__(self, is_empty: bool, length: int, max_length: int) -> None:
        self.is_empty = is_empty
        self.length = length
        self.max_length = max_length


class Matrix:
    """This class represents matrix."""

    def __init__(self, width: int, height: int,
                 color: TermColor, chars: List[str]) -> None:
        """Initializes

        Args:
            width (int): matrix width
            height (int): matrix height
            color (TermColor): matrix color
            chars (List[str]): characters for matrix construct
        """

        self.width = width
        self.height = height
        self.color = color
        self.min_vline_len = 5
        self.max_vline_len = height // 2
        self.chars = chars
        self.vlines = [
            VLine(is_empty=True, length=0, max_length=0) for _ in range(width)]

    def gen_new_line(self) -> str:
        """Generates new matrix line.

        Returns:
            str: new matrix line
        """

        line = ""
        for vline in self.vlines:
            line += self._gen_char_for_vline(vline)
        return line

    def _gen_char_for_vline(self, vline: VLine) -> str:
        """Generates new character for vertical line.

        Args:
            vline (VLine): vertical line

        Returns:
            str: new character for vertical line
        """

        vline_len = vline.length = vline.length + 1
        if vline_len > vline.max_length:
            vline.is_empty = not vline.is_empty
            vline.length = 1
            vline.max_length = random.randint(
                self.min_vline_len, self.max_vline_len)
        char = " " if vline.is_empty else self._gen_char()
        return char

    def _gen_char(self) -> str:
        """Generates random colored ascii character.

        Returns:
            str: random colored ascii character
        """

        return termcolor.colored(random.choice(self.chars), self.color)
