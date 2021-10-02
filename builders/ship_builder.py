from builders.abstract_base import CommonBuilder, ShipBuilder
from products.ships import WoodenToyShip, MetalToyShip


class WoodenToyShipBuilder(CommonBuilder, ShipBuilder):
    def __init__(self):
        self.reset()

    @property
    def product(self):
        toy_ship = self._toy_ship
        self.reset()
        return toy_ship

    def reset(self):
        self._toy_ship = WoodenToyShip()

    def create_body(self):
        self._toy_ship.add("wooden_body")

    def create_anchor(self):
        self._toy_ship.add("wooden_anchor")

    def create_mast(self):
        self._toy_ship.add("wooden_mast")


class MetalToyShipBuilder(CommonBuilder, ShipBuilder):
    def __init__(self):
        self.reset()

    @property
    def product(self):
        toy_ship = self._toy_ship
        self.reset()
        return toy_ship

    def reset(self):
        self._toy_ship = MetalToyShip()

    def create_body(self):
        self._toy_ship.add("metal_body")

    def create_anchor(self):
        self._toy_ship.add("metal_anchor")

    def create_mast(self):
        self._toy_ship.add("metal_mast")
