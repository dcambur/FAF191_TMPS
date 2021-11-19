class ToyCarDirector:
    product_type = "car"

    def __init__(self, builder=None):
        self._builder = builder

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, builder):
        self._builder = builder

    def create_minimal_product(self):
        self._builder.create_body()
        self._builder.create_wheels()

    def create_full_product(self):
        self._builder.create_body()
        self._builder.create_wheels()
        self._builder.create_engine()


class ToyRobotDirector:
    product_type = "robot"

    def __init__(self, builder=None):
        self._builder = builder

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, builder):
        self._builder = builder

    def create_minimal_product(self):
        self._builder.create_body()
        self._builder.create_head()

    def create_full_product(self):
        self._builder.create_body()
        self._builder.create_arms()
        self._builder.create_legs()
        self._builder.create_head()


class ToyShipDirector:
    product_type = "ship"

    def __init__(self, builder=None):
        self._builder = builder

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, builder):
        self._builder = builder

    def create_minimal_product(self):
        self._builder.create_body()

    def create_full_product(self):
        self._builder.create_body()
        self._builder.create_anchor()
        self._builder.create_mast()
