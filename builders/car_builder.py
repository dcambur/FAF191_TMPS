from builders.abstract_base import CommonBuilder, CarBuilder
from products.cars import WoodenToyCar, MetalToyCar


class WoodenToyCarBuilder(CommonBuilder, CarBuilder):
    def __init__(self):
        self.reset()

    @property
    def product(self):
        toy_car = self._toy_car
        self.reset()
        return toy_car

    def reset(self):
        self._toy_car = WoodenToyCar()

    def create_wheels(self):
        self._toy_car.add("wooden_wheels")

    def create_engine(self):
        self._toy_car.add("wooden_engine")

    def create_body(self):
        self._toy_car.add("wooden_body")


class MetalToyCarBuilder(CommonBuilder, CarBuilder):
    def __init__(self):
        self.reset()

    @property
    def product(self):
        toy_car = self._toy_car
        self.reset()
        return toy_car

    def reset(self):
        self._toy_car = MetalToyCar()

    def create_wheels(self):
        self._toy_car.add("metal_wheels")

    def create_engine(self):
        self._toy_car.add("metal_engine")

    def create_body(self):
        self._toy_car.add("metal_body")
