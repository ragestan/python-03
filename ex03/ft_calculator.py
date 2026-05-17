class calculator:
    """Perform vector-scalar arithmetic operations."""

    def __init__(self, values):
        """Initialize with a list of numeric values."""
        self.values = values

    def __add__(self, object) -> None:
        """Add scalar to each element and print the result."""
        result = [value + object for value in self.values]
        self.values = result
        print(result)

    def __mul__(self, object) -> None:
        """Multiply each element by scalar and print the result."""
        result = [value * object for value in self.values]
        self.values = result
        print(result)

    def __sub__(self, object) -> None:
        """Subtract scalar from each element and print the result."""
        result = [value - object for value in self.values]
        self.values = result
        print(result)

    def __truediv__(self, object) -> None:
        """Divide each element by scalar and print the result."""
        if object == 0:
            print("Error: division by zero")
            return
        result = [value / object for value in self.values]
        self.values = result
        print(result)


def main():
    """Entry point for manual testing."""


if __name__ == "__main__":
    main()
