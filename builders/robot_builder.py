from builders.abstract_base import CommonBuilder, RobotBuilder
from products.robots import WoodenToyRobot, MetalToyRobot


class WoodenToyRobotBuilder(CommonBuilder, RobotBuilder):
    def __init__(self):
        self.reset()

    @property
    def product(self):
        toy_robot = self._toy_robot
        self.reset()
        return toy_robot

    def reset(self):
        self._toy_robot = WoodenToyRobot()

    def create_arms(self):
        self._toy_robot.add("wooden_arms")

    def create_legs(self):
        self._toy_robot.add("wooden_legs")

    def create_body(self):
        self._toy_robot.add("wooden_body")

    def create_head(self):
        self._toy_robot.add("wooden_head")


class MetalToyRobotBuilder(CommonBuilder, RobotBuilder):
    def __init__(self):
        self.reset()

    @property
    def product(self):
        toy_robot = self._toy_robot
        self.reset()
        return toy_robot

    def reset(self):
        self._toy_robot = MetalToyRobot()

    def create_arms(self):
        self._toy_robot.add("metal_arms")

    def create_legs(self):
        self._toy_robot.add("metal_legs")

    def create_body(self):
        self._toy_robot.add("metal_body")

    def create_head(self):
        self._toy_robot.add("metal_head")
