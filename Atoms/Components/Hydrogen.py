from .BasicComponent import BasicComponent


class Hydrogen (BasicComponent):
    def __init__(self):
        super().__init__("green", 15, 2.58)


    def get_en(self, other: BasicComponent):
        """
        Hydrogen is a subclass of BasicComponent representing the hydrogen atom.
        This class initializes hydrogen with its specific attributes such as color, size,
        and electronegativity. It also defines a method to return electronegativity
        values when interacting with other specific atom types.
        """
        from .Oxygen import Oxygen
        from .Nitrogen import Nitrogen
        from .Sulfur import Sulfur
        from .Phosphorus import Phosphorus
        from .Carbon import Carbon

        if isinstance(other, Nitrogen):
            return -0.84
        if isinstance(other, Oxygen):
            return -1.24
        if isinstance(other, Carbon):
            return -0.35
        if isinstance(other, Sulfur):
            return -0.38
        if isinstance(other, Phosphorus):
            return 0.01
        return self.electronegativity