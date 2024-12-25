class Animal:
    """
    Base class representing a generic animal.
    """
    def __init__(self):
        pass  # No specific initialization for the base class

    def make_sound(self):
        """
        Generic method to print the sound made by an animal.
        Can be overridden by subclasses to provide specific behavior.
        """
        print("I make some sound!")


class Dog(Animal):
    """
    Subclass of Animal representing a dog.
    """
    def __init__(self):
        super().__init__()  # Call the constructor of the parent class

    def make_sound(self):
        """
        Override the make_sound method to specify the sound a dog makes.
        """
        print("Woof!")


class Cat(Animal):
    """
    Subclass of Animal representing a cat.
    """
    def __init__(self):
        super().__init__()  # Call the constructor of the parent class

    def make_sound(self):
        """
        Override the make_sound method to specify the sound a cat makes.
        """
        print("Meow!")


# Demonstrate polymorphism
if __name__ == "__main__":
    # Create an instance of the Animal class
    a = Animal()
    a.make_sound()  # Output: I make some sound!

    # Create an instance of the Dog class
    d = Dog()
    d.make_sound()  # Output: Woof!

    # Create an instance of the Cat class
    c = Cat()
    c.make_sound()  # Output: Meow!
