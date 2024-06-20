from abc import ABC, abstractmethod


# Product
class Computer:
    def __init__(self):
        self.case: str = ""
        self.motherboard: str = ""
        self.cpu: str = ""
        self.ram: str = ""

    def __str__(self):
        return f"Computer: Case={self.case}, Motherboard={self.motherboard}, CPU={self.cpu}, RAM={self.ram}"

class Package:
    def __init__(self):
        self.case: str = ""
        self.motherboard: str = ""
        self.cpu: str = ""
        self.ram: str = ""

    def __str__(self):
        return f"Package: Case={self.case}, Motherboard={self.motherboard}, CPU={self.cpu}, RAM={self.ram}"

# Builder
class ComputerBuilder(ABC):
    def __init__(self):
        self._computer = Computer()

    @abstractmethod
    def build_case(self): ...

    @abstractmethod
    def build_motherboard(self, motherboard): ...

    @abstractmethod
    def build_cpu(self, cpu): ...

    @abstractmethod
    def build_ram(self, ram): ...

    @property
    def computer(self):
        """Cannot type the return object. It can be different for each builder."""
        return self._computer


# Concrete Builders
class GamingComputerBuilder(ComputerBuilder):
    def build_case(self):
        self._computer.case = "Gaming Case"
        return self

    def build_motherboard(self):
        self._computer.motherboard = "Gaming Motherboard"
        return self

    def build_cpu(self):
        self._computer.cpu = "High-end CPU"
        return self

    def build_ram(self):
        self._computer.ram = "32GB RAM"
        return self


class OfficeComputerBuilder(ComputerBuilder):
    def build_case(self):
        self._computer.case = "Office Case"
        return self

    def build_motherboard(self):
        self._computer.motherboard = "Office Motherboard"
        return self

    def build_cpu(self):
        self._computer.cpu = "Mid-range CPU"
        return self

    def build_ram(self):
        self._computer.ram = "8GB RAM"
        return self

class ComputerPackage(ComputerBuilder):
    def __init__(self):
        self._computer_package = Package()

    def build_case(self):
        self._computer_package.case = "XL Package with lot of protection."
        return self

    def build_motherboard(self):
        self._computer_package.motherboard = "M package with standard protection."
        return self

    def build_cpu(self):
        self._computer_package.cpu = "S package with standard protection."
        return self

    def build_ram(self):
        self._computer_package.ram = "S package without protection."
        return self
    
    @property
    def computer(self):
        return self._computer_package


# Director
class ComputerDirector:
    def construct_computer(self, builder):
        return (
            builder.build_case()
            .build_motherboard()
            .build_cpu()
            .build_ram()
            .computer
        )


if __name__ == "__main__":
    gaming_computer_builder = GamingComputerBuilder()
    director = ComputerDirector()
    gaming_computer = director.construct_computer(gaming_computer_builder)
    print(gaming_computer)

    office_computer_builder = OfficeComputerBuilder()
    office_computer = director.construct_computer(office_computer_builder)
    print(office_computer)

    computer_package = ComputerPackage()
    price = director.construct_computer(computer_package)
    print(price)
