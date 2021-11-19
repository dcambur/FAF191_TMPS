# This is a Facade pattern implementation designed to shorten the written code required for client
# here we will create and log the product automatically
from product_logger import ProductLogger


class ClientProcessor:
    def __init__(self, sender, recipient):
        self.sender = sender
        self.recipient = recipient
        self.logger = None

    def __logger_init(self, director):
        if not self.logger:
            self.logger = ProductLogger(director)
        else:
            self.logger.switch(director)

    def create_product(self, director, mvp=False):
        if not mvp:
            product = director.create_full_product()

        else:
            product = director.create_minimal_product()

        self.__logger_init(director)
        print(self.logger.log(self.sender, self.recipient))

        return product
