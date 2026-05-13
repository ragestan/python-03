"""Exercise 02: Multiple inheritance and properties."""

from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing the king with mixed lineage."""

    def __init__(self, first_name, is_alive=True):
        """Initialize the king with Baratheon traits by default."""
        super().__init__(first_name, is_alive)

    def set_eyes(self, eyes):
        """Set eye color."""
        self.eyes = eyes

    def get_eyes(self):
        """Get eye color."""
        return self.eyes

    def set_hairs(self, hairs):
        """Set hair color."""
        self.hairs = hairs

    def get_hairs(self):
        """Get hair color."""
        return self.hairs


def main():
    """Entry point for manual testing."""


if __name__ == "__main__":
    main()
