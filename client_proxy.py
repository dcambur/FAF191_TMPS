# This class implements proxy pattern
# this proxy solves the problem where we have to restrict access to some of our product recipients(blacklisted)
# plus logging
from product_logger import ProductLogger

blacklisted = ["TomSmith", "Jerry", "Impostor", "sus1234"]


class ClientProxy:
    def __init__(self, real_client):
        self.real_client = real_client
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
        print(self.logger.log(self.real_client.sender, self.real_client.recipient))

        return product
