from abc import ABC, abstractmethod


@abstractmethod
class CommonBuilder(ABC):
    @abstractmethod
    def product(self):
        pass

    @abstractmethod
    def reset(self):
        pass


class RobotBuilder(ABC):
    @abstractmethod
    def create_arms(self):
        pass

    @abstractmethod
    def create_legs(self):
        pass

    @abstractmethod
    def create_body(self):
        pass

    @abstractmethod
    def create_head(self):
        pass


class ShipBuilder(ABC):
    @abstractmethod
    def create_body(self):
        pass

    @abstractmethod
    def create_anchor(self):
        pass

    @abstractmethod
    def create_mast(self):
        pass


class CarBuilder(ABC):
    @abstractmethod
    def create_wheels(self):
        pass

    @abstractmethod
    def create_engine(self):
        pass

    @abstractmethod
    def create_body(self):
        pass
