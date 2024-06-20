"""
Factory.

When to use :
+ when you don't know beforehand the exact objects your code should work with. (Need a new animal just add a new constructor subclass.)
+ save system resources by reusing existing objects instead of rebuilding them (pooling).
"""

from abc import ABC, abstractmethod


# Target objects we want to give to the client code.
class Animal(ABC):
    """Interface for products."""

    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def make_sound(self) -> None: ...

    @abstractmethod
    def go_out(self) -> None: ...


class Cat(Animal):
    def make_sound(self) -> None:
        print("I am a Cat so 'meoww'")

    def go_out(self) -> None:
        print("I can go out alone.")


class Dog(Animal):
    def __init__(self, name: str, human) -> None:
        super().__init__(name)
        self.human = human

    def make_sound(self) -> None:
        print("I am a Dog so barff")

    def go_out(self) -> None:
        print(f"I need to ask to my {self.human} to go out.")


# Factories
## Simple Factory Function
def factory_method(animal: str, name: str, **kwargs) -> Animal:
    """
    Simple Function

    Simple enough to handle the case where all products share the same attributes.

    Become cumbersome otherwise. 👇

    """
    return {
        "dog": Dog(name=name, human=kwargs["human"] if "human" in kwargs else None),
        "cat": Cat(name=name),
    }[animal]


class Factory(ABC):
    """Interface for our concrete factories."""

    def __init__(self) -> None: ...
    def create_animal(self) -> Animal: ...

    def make_animal_speak(self) -> None:
        """
        Make the animal speak.

        The creator's primary responsibility is not creating products.
        It usually contains some core business logic that relies
        on product objects returned by the factory method.

        Subclasses can indirectly change that business logic by overriding the factory method
        and returning a different type of product from it.

        """
        animal = self.create_animal()
        animal.make_sound()


class DogFactory(Factory):
    def __init__(self, name: str, human) -> None:
        self.name = name
        self.human = human

    def create_animal(self) -> Dog:
        return Dog(self.name, self.human)


class CatFactory(Factory):
    def __init__(self, name: str) -> None:
        self.name = name

    def create_animal(self) -> Cat:
        return Cat(self.name)


if __name__ == "__main__":
    # client code getting a dog using the simple function:
    animal = factory_method(
        animal="dog", name="Billy", **{"human": "John"}
    )  # inferred type is Animal
    animal.make_sound()

    # client code getting a dog using the concrete factory
    animal_factory = DogFactory(name="Billy", human="John")
    animal = animal_factory.create_animal()  # inferred type is Dog
    animal.make_sound()
