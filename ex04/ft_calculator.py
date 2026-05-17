class calculator:
    """Provide static vector operations."""

    @staticmethod
    def dotproduct(v1: list[float], v2: list[float]) -> None:
        """Print the dot product of two vectors."""
        result = sum(float(value * other) for value, other in zip(v1, v2))
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(v1: list[float], v2: list[float]) -> None:
        """Print the element-wise addition of two vectors."""
        result = [float(value + other) for value, other in zip(v1, v2)]
        print(f"Add Vector is : {result}")

    @staticmethod
    def sous_vec(v1: list[float], v2: list[float]) -> None:
        """Print the element-wise subtraction of two vectors."""
        result = [float(value - other) for value, other in zip(v1, v2)]
        print(f"Sous Vector is: {result}")


def main():
    """Entry point for manual testing."""


if __name__ == "__main__":
    main()
