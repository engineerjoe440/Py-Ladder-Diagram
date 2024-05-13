# Test a Rung will be Rendered as ASCII

from pyld import Ladder, Rung, Branch
from pyld.elements import Coil, Contact, NegatedCoil, NegatedContact

SIMPLE_LADDER = """\
█
█               
█─────┤ ├────( )
█"""

def test_generate_simple_rung():
    """Validate Simple Ladder Generation with One Rung."""
    ladder = Ladder(
        Rung(
            Contact(),
            Coil(),
        )
    )
    assert SIMPLE_LADDER == ladder.render()

NEGATED_SIMPLE_LADDER = """\
█
█               
█─────┤/├────( )
█"""

def test_generate_simple_negated_rung():
    """Validate Simple Ladder Generation with One Rung."""
    ladder = Ladder(
        Rung(
            NegatedContact(),
            Coil(),
        )
    )
    assert NEGATED_SIMPLE_LADDER == ladder.render()

NEGATED_COIL_SIMPLE_LADDER = """\
█
█               
█─────┤ ├────(/)
█"""

def test_generate_simple_rung_neg_coil():
    """Validate Simple Ladder Generation with One Rung."""
    ladder = Ladder(
        Rung(
            Contact(),
            NegatedCoil(),
        )
    )
    assert NEGATED_COIL_SIMPLE_LADDER == ladder.render()

NEGATED_COIL_NEGATED_SIMPLE_LADDER = """\
█
█               
█─────┤/├────(/)
█"""

def test_generate_simple_negated_rung_negated_coil():
    """Validate Simple Ladder Generation with One Rung."""
    ladder = Ladder(
        Rung(
            NegatedContact(),
            NegatedCoil(),
        )
    )
    print(ladder.render())
    assert NEGATED_COIL_NEGATED_SIMPLE_LADDER == ladder.render()

SIMPLE_LADDER_LONG_NAMES = """\
█
█    SomePOU.LongName  AnotherPOU.EvenLongerName
█──────────┤ ├───────────────────────────────( )
█"""

def test_generate_simple_rung_long_name():
    """Validate Simple Ladder Generation with One Rung."""
    ladder = Ladder(
        Rung(
            Contact("SomePOU.LongName"),
            Coil("AnotherPOU.EvenLongerName"),
        )
    )
    assert SIMPLE_LADDER_LONG_NAMES == ladder.render()


BRANCHED_LADDER = """\
█
█       In1    In2   Out1
█───┬───┤ ├────┤ ├────( )
█   │                    
█   │   In1    In2   Out2
█   └───┤ ├────┤/├────( )
█                        
█\
"""

def test_generate_simple_branched_ladder():
    """Validate Simple Ladder Generation with One Rung."""
    ladder = Ladder(
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
    print(ladder.render())
    assert BRANCHED_LADDER == ladder.render()


JOINING_BRANCHED_LADDER = """\
█
█         In1    In2      Out3
█─────┬───┤ ├────┤ ├──┬────( )
█     │               │       
█     │   In1    In2  │       
█     └───┤ ├────┤/├──┘       
█                             
█\
"""

def test_generate_joining_branched_ladder():
    """Validate Simple Ladder Generation with One Rung."""
    ladder = Ladder(
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
    assert JOINING_BRANCHED_LADDER == ladder.render()
