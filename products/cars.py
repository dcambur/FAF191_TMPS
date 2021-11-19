import copy

from products.abstract_base import CommonBuilderProduct, Car


class WoodenToyCar(Car, CommonBuilderProduct):
    factory_name = "Wooden Toy Factory"

    def __init__(self):
        self.parts = []

    def drive(self):
        print("Your wooden toy car drives as slow as ever!")

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        return f"Wooden Toy Car Parts: {', '.join(self.parts)}"

    def clone(self):
        return copy.copy(self)


class MetalToyCar(Car, CommonBuilderProduct):
    factory_name = "Metal Toy Factory"

    def __init__(self):
        self.parts = []

    def drive(self):
        print("Your metal toy car drives as fast as ever!")

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        return f"Metal Toy Car Parts: {', '.join(self.parts)}"

    def clone(self):
        return copy.copy(self)
