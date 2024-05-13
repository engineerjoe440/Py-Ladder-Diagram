# Py-Ladder-Diagram

Ladder Logic Diagrams written in Python.

## Installation

Install with `pip`:

```shell
pip install py-ladder-diagram
```

## Usage

A simple, two-rung system can be modeled with the following code:

```python
from pyld import Ladder, Rung
from pyld.elements import Coil, Contact, NegatedContact

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

The addition of a branch is relatively easy, and can render a few ways:

```python
from pyld import Ladder, Rung, Branch
from pyld.elements import Coil, Contact, NegatedContact

Ladder(
    Rung(
        Branch(
            Rung(
                Contact("In1"),
                Contact("In2"),
            ),
            Rung(
                Contact("In1"),
                NegatedContact("In2"),
            )
        ),
        Coil("Out3"),
    )
)
# Renders:
# █
# █         In1    In2      Out3
# █─────┬───┤ ├────┤ ├──┬────( )
# █     │               │       
# █     │   In1    In2  │       
# █     └───┤ ├────┤/├──┘       
# █                             
# █

Ladder(
    Branch(
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
)
# Renders:
# █
# █       In1    In2   Out1
# █───┬───┤ ├────┤ ├────( )
# █   │                    
# █   │   In1    In2   Out2
# █   └───┤ ├────┤/├────( )
# █                        
# █
```

### YAML Format (Future Work)

At some point in the future, functionality will be built in to model ladder
diagrams from YAML.

```yaml
Rung:
  - Contact: In1
  - Contact: In2
  - Coil: Out1
Rung:
  - Branch:
    - Rung:
      - Contact: In1
      - Contact: In2
    - Rung:
      - Contact: In1
      - NegatedContact: In2
  - Coil: Out3
```
