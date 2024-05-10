################################################################################
"""PyLadderDiag - Draw Ladder Diagrams as SVG in Python."""
################################################################################

from enum import Enum

from .common import RenderStyle

class Justification(str, Enum):
    """String Justification Control."""

    LEFT = "<"
    RIGHT = ">"
    CENTER = "^"

class LadderElement:
    """Base Class for all Other Ladder Elements to Extend."""

    ascii: str
    justification: Justification = Justification.CENTER
    depth: int = 2

    def __init__(self, name: str = None) -> None:
        """Construct the Basic Ladder Element Information."""
        self._name = name or ""

    @property
    def name(self) -> str:
        """Return the Name Value."""
        return self._name

    @name.setter
    def name(self, value):
        """Set the Name Value."""
        self._name = str(value)

    @property
    def width(self) -> int:
        """Evaluate the Element Width."""
        return max(len(self.ascii), len(self.name))

    def justifier(self) -> str:
        """Generate an Appropriate Justification Control."""
        return f"{{:─{self.justification.value}{self.width}}}"

    def render(self, style: RenderStyle = RenderStyle.ASCII) -> list[str]:
        """Render the Ladder Rung as a String."""
        match style:
            case RenderStyle.ASCII:
                return [
                    self.name.center(self.width),
                    self.justifier().format(self.ascii),
                ]



class Contact(LadderElement):
    """Contact Element for Ladder Diagrams."""

    ascii: str = "─┤ ├─"

class NegatedContact(LadderElement):
    """Negated Contact Element for Ladder Diagrams."""

    ascii: str = "─┤/├─"

class Coil(LadderElement):
    """Coil Element for Ladder Diagrams."""

    ascii: str = "─( )"
    justification: Justification = Justification.RIGHT

class NegatedCoil(LadderElement):
    """Negated Coil Element for Ladder Diagrams."""

    ascii: str = "─(/)"
    justification: Justification = Justification.RIGHT
