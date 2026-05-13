from abc import ABC, abstractmethod


class Character(ABC):
    """Base character with a living state."""

    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """Initialize a character with name and living state."""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Set the character's state to dead."""
        self.is_alive = False


class Stark(Character):
    """Stark family character."""

    def __init__(self, first_name, is_alive=True):
        """Initialize a Stark character."""
        super().__init__(first_name, is_alive)


def main():
    """Entry point for manual testing."""


if __name__ == "__main__":
    main()
