from abc import ABC, abstractmethod


class CommonBuilderProduct(ABC):
    @abstractmethod
    def add(self, part):
        pass

    @abstractmethod
    def list_parts(self):
        pass

    @abstractmethod
    def clone(self):
        pass


class Ship(ABC):
    type = "ship"

    @abstractmethod
    def sail(self):
        pass


class Car(ABC):
    type = "car"

    @abstractmethod
    def drive(self):
        pass


class Robot(ABC):
    type = "robot"

    @abstractmethod
    def run(self):
        pass
