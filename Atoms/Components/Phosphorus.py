from .BasicComponent import BasicComponent
class Phosphorus (BasicComponent):
    def __init__(self):
        super().__init__("white", 22, 2.19)

    def get_en(self, other: BasicComponent):
        """
        Determines the electronegativity difference between phosphorus and another atom.
        Special cases are defined for interactions with Oxygen, Nitrogen, Sulfur, Carbon,
        and Hydrogen. If the other atom type isn't one of these,
        phosphorus's intrinsic electronegativity is returned.
        """
        from .Oxygen import Oxygen
        from .Nitrogen import Nitrogen
        from .Sulfur import Sulfur
        from .Hydrogen import Hydrogen
        from .Carbon import Carbon

        if isinstance(other, Nitrogen):
            return -0.85
        if isinstance(other, Oxygen):
            return -1.25
        if isinstance(other, Carbon):
            return -0.36
        if isinstance(other, Sulfur):
            return -0.39
        if isinstance(other, Hydrogen):
            return -0.01
        return self.electronegativity