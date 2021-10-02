import copy

from products.abstract_base import CommonBuilderProduct, Robot


class WoodenToyRobot(Robot, CommonBuilderProduct):
    def __init__(self):
        self.parts = []

    def run(self):
        print("Your wooden toy robot is lazy. Instead of running, it walks")

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        print(f"Wooden Toy Robot Parts: {', '.join(self.parts)}", end="")

    def clone(self):
        return copy.copy(self)


class MetalToyRobot(Robot, CommonBuilderProduct):
    def __init__(self):
        self.parts = []

    def run(self):
        print("Your metal toy robot is heavy. It failed to run")

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        print(f"Metal Toy Robot Parts: {', '.join(self.parts)}", end="")

    def clone(self):
        return copy.copy(self)
