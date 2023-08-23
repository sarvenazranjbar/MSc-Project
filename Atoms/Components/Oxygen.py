from .BasicComponent import BasicComponent


class Oxygen (BasicComponent):
    def __init__(self):
        super().__init__("red", 640, 3.44)

    def get_en(self, other: BasicComponent):
        """
        Determines the electronegativity difference between oxygen and another atom.
        Special cases are defined for interactions with Nitrogen, Sulfur, Carbon,
        Phosphorus, and Hydrogen. If the other atom type isn't one of these,
        oxygen's intrinsic electronegativity is returned.
        """
        from .Nitrogen import Nitrogen
        from .Hydrogen import Hydrogen
        from .Carbon import Carbon
        from .Phosphorus import Phosphorus
        from .Sulfur import Sulfur

        if isinstance(other, Nitrogen):
            return 0.4
        if isinstance(other, Sulfur):
            return 0.86
        if isinstance(other, Carbon):
            return 0.89
        if isinstance(other, Phosphorus):
            return -0.39
        if isinstance(other, Hydrogen):
            return 1.24
        return self.electronegativity
