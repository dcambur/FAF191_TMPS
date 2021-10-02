from builders.directors import ToyRobotDirector, ToyShipDirector, \
    ToyCarDirector
from factories.abstract_base import ToysFactory
from builders.car_builder import WoodenToyCarBuilder, MetalToyCarBuilder
from builders.robot_builder import WoodenToyRobotBuilder, MetalToyRobotBuilder
from builders.ship_builder import WoodenToyShipBuilder, MetalToyShipBuilder


class WoodenToysFactory(ToysFactory):
    def create_robot_director(self):
        return ToyRobotDirector(WoodenToyRobotBuilder())

    def create_ship_director(self):
        return ToyShipDirector(WoodenToyShipBuilder())

    def create_car_director(self):
        return ToyCarDirector(WoodenToyCarBuilder())


class MetalToysFactory(ToysFactory):
    def create_robot_director(self):
        return ToyRobotDirector(MetalToyRobotBuilder())

    def create_ship_director(self):
        return ToyShipDirector(MetalToyShipBuilder())

    def create_car_director(self):
        return ToyShipDirector(MetalToyCarBuilder())
