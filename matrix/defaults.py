import string
from typing import List

from typing_extensions import Final

from .typedefs import TermColor

DEFAULT_COLOR: Final[TermColor] = "green"
DEFAULT_SPEED: Final[int] = 40
DEFAULT_CHARS: Final[List[str]] = [
    *string.ascii_letters,
    *string.digits,
    *string.punctuation,
]
