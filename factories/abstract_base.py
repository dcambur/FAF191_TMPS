from abc import abstractmethod, ABC


class ToysFactory(ABC):

    @abstractmethod
    def create_robot_director(self):
        pass

    @abstractmethod
    def create_ship_director(self):
        pass

    @abstractmethod
    def create_car_director(self):
        pass
