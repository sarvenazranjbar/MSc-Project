from .BasicComponent import BasicComponent


class Nitrogen (BasicComponent):
    def __init__(self):
        super().__init__("yellow", 12, 3.04)

    def get_en(self, other: BasicComponent):
        """
        Determines the electronegativity difference between nitrogen and another atom.
        Special cases are defined for interactions with Hydrogen, Oxygen, Carbon,
        Sulfur, and Phosphorus. If the other atom type isn't one of these,
        nitrogen's intrinsic electronegativity is returned.
        """
        from .Oxygen import Oxygen
        from .Sulfur import Sulfur
        from .Hydrogen import Hydrogen
        from .Carbon import Carbon
        from.Phosphorus import Phosphorus

        if isinstance(other, Hydrogen):
            return 0.84
        if isinstance(other, Oxygen):
            return -0.4
        if isinstance(other, Carbon):
            return 0.49
        if isinstance(other, Sulfur):
            return 0.46
        if isinstance(other, Phosphorus):
            return 0.85
        return self.electronegativity