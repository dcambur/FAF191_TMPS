# provides the simple implementation of the decorator pattern to log the activities between different factories
# the idea is to notify the recipient about factories activity.
# Every Logged object is registered as "created"
import datetime


class ProductLogger:
    toys_created = 0

    def __init__(self, director):
        self.product = director.builder.product

    def switch(self, new_director):
        self.product = new_director.builder.product

    def log(self, send_from, send_to):
        self.toys_created += 1

        return {"from": send_from,
                "to": send_to,
                "msg": f"{self.product.factory_name}: the {self.product.type} "
                       f"toy was created at {datetime.datetime.now()} ",
                "toys_created": self.toys_created,
                "toys_parts": f"{self.product.parts}"}
