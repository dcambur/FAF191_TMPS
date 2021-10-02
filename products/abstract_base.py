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
    @abstractmethod
    def sail(self):
        pass


class Car(ABC):
    @abstractmethod
    def drive(self):
        pass


class Robot(ABC):
    @abstractmethod
    def run(self):
        pass
