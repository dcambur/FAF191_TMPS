import copy

from products.abstract_base import CommonBuilderProduct, Ship


class WoodenToyShip(Ship, CommonBuilderProduct):
    def __init__(self):
        self.parts = []

    def sail(self):
        print(
            "Your wooden toy ship was preyed upon the merciless bathtub water ")

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        print(f"Wooden Toy Ship Parts: {', '.join(self.parts)}", end="")

    def clone(self):
        return copy.copy(self)


class MetalToyShip(Ship, CommonBuilderProduct):
    def __init__(self):
        self.parts = []

    def sail(self):
        print(
            "Your metal toy ship was preyed upon the merciless bathtub water ")

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        print(f"Metal Toy Ship Parts: {', '.join(self.parts)}", end="")

    def clone(self):
        return copy.copy(self)
