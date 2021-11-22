# This is a Facade pattern implementation designed to shorten the written code required for client
# here we will create and log the product automatically


class ClientProcessor:
    def __init__(self, sender, recipient):
        self.sender = sender
        self.recipient = recipient

    @staticmethod
    def create_product(director, mvp=False):
        if not mvp:
            product = director.create_full_product()
        else:
            product = director.create_minimal_product()
        return product
