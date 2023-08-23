from .BasicComponent import BasicComponent


class Sulfur (BasicComponent):
    def __init__(self):
        super().__init__("pink", 15, 2.58)

    def get_en(self, other: BasicComponent):
        """
        Determines the electronegativity difference between sulfur and another atom.
        Special cases are defined for interactions with Oxygen, Nitrogen, Carbon,
        Phosphorus, and Hydrogen. If the other atom type isn't one of these,
        sulfur's intrinsic electronegativity is returned.
        """
        from .Oxygen import Oxygen
        from .Nitrogen import Nitrogen
        from .Hydrogen import Hydrogen
        from .Carbon import Carbon
        from .Phosphorus import Phosphorus

        if isinstance(other, Nitrogen):
            return -0.46
        if isinstance(other, Oxygen):
            return -0.86
        if isinstance(other, Carbon):
            return 0.03
        if isinstance(other, Phosphorus):
            return 0.38
        if isinstance(other, Hydrogen):
            return -0.01
        return self.electronegativity
