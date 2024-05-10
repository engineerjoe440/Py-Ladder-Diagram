# PyLD
Ladder Logic Diagrams written in Python.

## Installation

:information_source: TBD


## Usage

```python
from PyLD import Ladder, Rung
from PyLD.elements import Coil, Contact, NegatedContact

Ladder(
    Rung(
        Contact("In1"),
        Contact("In2"),
        Coil("Out1"),
    ),
    Rung(
        Contact("In1"),
        NegatedContact("In2"),
        Coil("Out2"),
    )
)
# Renders:
# █
# █     In1    In2   Out1
# █─────┤ ├────┤ ├────( )
# █
# █     In1    In2   Out2
# █─────┤ ├────┤/├────( )
# █
```
