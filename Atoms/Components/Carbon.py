from .BasicComponent import BasicComponent


class Carbon (BasicComponent):
    def __init__(self):
        super().__init__("blue", 180, 2.55)


    def get_en(self, other: BasicComponent):
        """
        Determines the electronegativity difference between carbon and another atom.
        Special cases are defined for interactions with Nitrogen, Oxygen, Hydrogen,
        Sulfur, and Phosphorus. If the other atom type isn't one of these,
        carbon's intrinsic electronegativity is returned.
        """
        from .Oxygen import Oxygen
        from .Nitrogen import Nitrogen
        from .Sulfur import Sulfur
        from .Hydrogen import Hydrogen
        from .Phosphorus import Phosphorus

        if isinstance(other, Nitrogen):
            return 0.49
        if isinstance(other, Oxygen):
            return 0.89
        if isinstance(other, Hydrogen):
            return -0.35
        if isinstance(other, Sulfur):
            return 0.03
        if isinstance(other, Phosphorus):
            return -0.36
        return self.electronegativity


