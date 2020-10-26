import string
import random
from typing import List, Optional
from typing_extensions import TypedDict

import termcolor


class VLine(TypedDict):
    empty: bool
    length: int
    max_length: int


class Matrix:
    def __init__(self, width: int, height: int,
                 color: str, chars: Optional[List[str]] = None) -> None:
        self.width = width
        self.height = height
        self.color = color
        self.min_vline_len = 5
        self.max_vline_len = height // 2
        self.chars: List[str] = [
            *string.ascii_letters,
            *string.digits,
            *string.punctuation,
        ] if chars is None else chars
        # self.matrix = [" " * width for _ in range(height)]
        self.vlines: List[VLine] = [
            {"empty": True, "length": 0, "max_length": height} for _ in range(width)]

    def gen_new_line(self) -> str:
        # matrix = self.matrix

        line = ""
        for vline in self.vlines:
            line += self.gen_char_for_vline(vline)

        # self._add_new_line(line)
        return line

    def gen_char_for_vline(self, vline: VLine) -> str:
        vline_len = vline["length"] = vline["length"] + 1
        if vline_len <= vline["max_length"]:
            char = " " if vline["empty"] else self._gen_char()
            return char
        else:
            vline["empty"] = not vline["empty"]
            vline["length"] = 0
            vline["max_length"] = random.randint(
                self.min_vline_len, self.max_vline_len)
            return self.gen_char_for_vline(vline)

    def _gen_char(self) -> str:
        """Returns random ascii character."""

        return termcolor.colored(random.choice(self.chars), self.color)

    # def _add_new_line(self, line) -> None:
    #     # matrix = self.matrix

    #     matrix.append(line)
    #     if len(matrix) > self.height:
    #         self.matrix = matrix[1:]

    # def __str__(self) -> str:
    #     return "\n".join(self.matrix)
