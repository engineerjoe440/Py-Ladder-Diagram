################################################################################
"""PyLD - Draw Ladder Diagrams Programmatically in Python."""
################################################################################

from typing import Union

from .common import RenderStyle
from .elements import LadderElement

class Rung:
    """Generate the Representative Structure of a Ladder-Diagram Rung."""

    elements: list[Union[LadderElement, "Branch"]]

    def __init__(self, *elements: tuple[Union[LadderElement, "Branch"]]) -> None:
        """Prepare the Class Attributes."""
        self.elements = list(elements)

    def ascii(self) -> list[str]:
        """Generate a List of the Strings for Each 'Row' of Content."""
        rows = {i: "" for i in range(self.depth)}
        for elem in self.elements:
            contents = elem.render(style=RenderStyle.ASCII)
            for i in rows:
                if i < elem.depth:
                    # Content Present for the Row of Interest
                    padding = " " * 2
                    if contents[i][0] == "─":
                        padding = "─" * 2
                    rows[i] += padding + contents[i]
                else:
                    # Nothing Present, Pad with Whitespace
                    rows[i] += ' ' * (elem.width + 2)
        # Render All Rows, Together
        return list(rows.values())

    @property
    def depth(self) -> int:
        """Evaluate the Maximum Depth for Any Elements in the Rung."""
        return max(*[elem.depth for elem in self.elements])

    def render(self, style: RenderStyle = RenderStyle.ASCII) -> Union[list[str], str]:
        """Render the Ladder Rung as a String."""
        match style:
            case RenderStyle.ASCII:
                return self.ascii()


class Branch:
    """Generate Multiple Parallel-Connected Segments."""

    rungs: list[Rung]

    def __init__(self, *rungs: tuple[Rung]) -> None:
        """Construct the Basic Structure."""
        self.rungs = list(rungs)

    def ascii(self) -> list[str]:
        """Generate a List of the Strings for Each 'Row' of Content."""
        branch = []
        branching = False
        for i, rung in enumerate(self.rungs, 1):
            row_length = 0
            joining = "─" in [r[-1] for r in rung.render()]
            for row in rung.render():
                row_length = len(row)
                # Add Each Row's Worth of Content to the Ladder
                if row.startswith("─"):
                    if not branching:
                        content = "─┬" + row
                        post = "─┬─"
                        branching = True
                    elif i == self.count:
                        content = " └" + row
                        post = "─┘ "
                        branching = False
                    else:
                        content = " ├" + row
                        post = "─┤ "
                elif branching:
                    content = " │" + row
                    post = " │ "
                else:
                    content = "  " + row
                    post = "   "
                if joining:
                    content += post
                branch.append(content)
            # Add Separation
            if branching:
                content = " │" + (" " * row_length)
                post = " │ "
            else:
                content = "  " + (" " * row_length)
                post = "   "
            if joining:
                content += post
            branch.append(content)
        return branch

    @property
    def count(self) -> int:
        """Evaluate the Number of Rungs."""
        return len(self.rungs)

    @property
    def depth(self) -> int:
        """Evaluate the Maximum Depth for Any Elements in the Rung."""
        return sum([r.depth + 1 for r in self.rungs])

    def render(self, style: RenderStyle = RenderStyle.ASCII) -> Union[list[str], str]:
        """Render the Branch of Multiple Rungs as a String."""
        match style:
            case RenderStyle.ASCII:
                return self.ascii()


class Ladder:
    """
    A Ladder Diagram to Consist of One or More Ladder Rungs.

    Examples
    --------
    >>> from pyld import Ladder, Rung
    >>> from pyld.elements import Coil, Contact, NegatedContact
    >>> Ladder(
    >>>     Rung(
    >>>         Contact("In1"),
    >>>         Contact("In2"),
    >>>         Coil("Out1"),
    >>>     ),
    >>>     Rung(
    >>>         Contact("In1"),
    >>>         NegatedContact("In2"),
    >>>         Coil("Out2"),
    >>>     )
    >>> )
    >>> # Renders:
    >>> # █
    >>> # █     In1    In2   Out1
    >>> # █─────┤ ├────┤ ├────( )
    >>> # █
    >>> # █     In1    In2   Out2
    >>> # █─────┤ ├────┤/├────( )
    >>> # █
    """

    rungs: list[Union[Rung, Branch]]

    def __init__(self, *rungs: tuple[Rung | Branch]) -> None:
        """Construct the Basic Structure."""
        self.rungs = list(rungs)

    def __repr__(self) -> str:
        """Represent the Ladder as a String."""
        ladder = "█"
        for rung in self.rungs:
            for row in rung.render():
                # Add Each Row's Worth of Content to the Ladder
                padding = " " * 2
                if row[0] == "─":
                    padding = "─" * 2
                ladder += '\n█' + padding + row
            ladder += "\n█"
        return ladder

    def render(self, style: RenderStyle = RenderStyle.ASCII) -> str:
        """Render the Ladder as a String."""
        match style:
            case RenderStyle.ASCII:
                return repr(self)
