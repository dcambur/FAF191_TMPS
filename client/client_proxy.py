# This class implements proxy pattern
# this proxy solves the problem where we have to restrict access to some of our product recipients(blacklisted)
# plus logging
from subscriber.subcription import SubscribeObserver
from logger.product_logger import ProductLogger


class ClientProxy:
    def __init__(self, real_client, log_required=False):
        self.log_required = log_required
        self.real_client = real_client
        self.notifier = SubscribeObserver()

        self.logger = None

    def __logger_init(self, director):
        if not self.logger:
            self.logger = ProductLogger(director)
        else:
            self.logger.switch(director)

    def create_product(self, director, mvp=False):
        product = self.real_client.create_product(director, mvp)

        if self.real_client.recipient in self.notifier.subscriptions:
            self.notifier.notify()

        if self.log_required:
            self.__logger_init(director)
            print(self.logger.log(self.real_client.sender, self.real_client.recipient))

        return product