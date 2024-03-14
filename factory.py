from abc import ABC, abstractmethod, abstractstaticmethod


# Target objects we want to give to the client code.
class Animal(ABC):
    """Interface for products."""

    def __init__(self, name) -> None:
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
    def __init__(self, name, human) -> None:
        super().__init__(name)
        self.human = human

    def make_sound(self) -> None:
        print("I am a Dog so barff")

    def go_out(self) -> None:
        print(f"I need to ask to my {self.human} to go out.")


# Factories


def factory_method(animal: str, name: str, **kwargs):
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


class DogFactory(Factory):
    def __init__(self, name, human) -> None:
        self.name = name
        self.human = human

    def create_animal(self) -> Dog:
        return Dog(self.name, self.human)


class CatFactory(Factory):
    def __init__(self, name) -> None:
        self.name = name

    def create_animal(self) -> Cat:
        return Cat(self.name)


if __name__ == "__main__":
    # client code getting a dog using the simple function:
    animal = factory_method(animal="dog", name="Billy", **{"human": "John"})
    animal.make_sound()

    # client code getting a dog using the concrete factory
    animal_factory = DogFactory(name="Billy", human="John")
    animal = animal_factory.create_animal()
    animal.make_sound()
