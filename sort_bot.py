from enum import Enum
from constant import MAX_VOLUME, MAX_DIMENSION


class StackType(Enum):
    """
    define three stack type
    """
    STANDARD = 1
    SPECIAL = 2
    REJECTED = 3


class SortBot:
    """
    Sort the packages using the following criteria:

    - A package is **bulky** if its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³ or when one of its dimensions is greater or equal to 150 cm.
    - A package is **heavy** when its mass is greater or equal to 20 kg.

    You must dispatch the packages in the following stacks:

    - **STANDARD**: standard packages (those that are not bulky or heavy) can be handled normally.
    - **SPECIAL**: packages that are either heavy or bulky can't be handled automatically.
    - **REJECTED**: packages that are **both** heavy and bulky are rejected.
    """
    def sort(self, width: int, height: int, length: int, mass: int) -> StackType:

        if width <=0 or height <= 0 or length <= 0 or mass <= 0:
            raise ValueError("dimension and mass must be positive")

        bulky = width * height * length >= MAX_VOLUME or max(width, height, length) >= MAX_DIMENSION

        heavy = mass >= 20

        if not bulky and not heavy:
            return StackType.STANDARD
        elif bulky and heavy:
            return StackType.REJECTED
        else:
            return StackType.SPECIAL
