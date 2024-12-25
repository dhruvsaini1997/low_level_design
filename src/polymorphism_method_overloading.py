class Calculator:
    def __init__(self):
        pass  # No initialization is needed in this case

    def add(self, a=None, b=None, c=None):
        """
        Demonstrates method overloading by handling different numbers of arguments.

        Python does not support traditional method overloading like Java or C++,
        but we can achieve similar behavior using default arguments and conditional logic.

        :param a: First number (optional)
        :param b: Second number (optional)
        :param c: Third number (optional)
        :return: Sum of provided arguments, or a message if insufficient arguments
        """
        if a and b and c:
            # Case: All three arguments provided
            return a + b + c
        elif a and b:
            # Case: Only two arguments provided
            return a + b
        else:
            # Case: Fewer than two arguments provided
            return "Please provide at least two variables"


# Entry point for testing the Calculator class
if __name__ == "__main__":
    calc = Calculator()

    # Test cases
    print(calc.add(10, 20))  # Output: 30
    print(calc.add(10, 20, 30))  # Output: 60
    print(calc.add(10))  # Output: Please provide at least two variables
