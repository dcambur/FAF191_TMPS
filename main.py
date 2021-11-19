from client_processor import ClientProcessor
from factories.toy_factory import WoodenToysFactory, MetalToysFactory

# this is where you can test my code as a client.
from product_logger import ProductLogger


def client_code(sender, recipient):
    client = ClientProcessor(SENDER, RECIPIENT)

    wooden_toys_factory = WoodenToysFactory()
    metal_toys_factory = MetalToysFactory()

    wooden_director = wooden_toys_factory.create_car_director()
    metal_director = metal_toys_factory.create_ship_director()

    client.create_product(wooden_director, mvp=True)
    client.create_product(metal_director)
    client.create_product(wooden_director)


if __name__ == "__main__":
    SENDER = "DMITRIY CAMBUR"
    RECIPIENT = "ANONYMOUS"
    client_code(SENDER, RECIPIENT)
