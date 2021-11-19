import copy

from products.abstract_base import CommonBuilderProduct, Robot


class WoodenToyRobot(Robot, CommonBuilderProduct):
    factory_name = "Wooden Toy Factory"

    def __init__(self):
        self.parts = []

    def run(self):
        print("Your wooden toy robot is lazy. Instead of running, it walks")

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        return f"Wooden Toy Robot Parts: {', '.join(self.parts)}"

    def clone(self):
        return copy.copy(self)


class MetalToyRobot(Robot, CommonBuilderProduct):
    factory_name = "Metal Toy Factory"

    def __init__(self):
        self.parts = []

    def run(self):
        print("Your metal toy robot is heavy. It failed to run")

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        return f"Metal Toy Robot Parts: {', '.join(self.parts)}"

    def clone(self):
        return copy.copy(self)
