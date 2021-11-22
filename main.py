from client.client_processor import ClientProcessor
from client.client_proxy import ClientProxy
from factories.toy_factory import WoodenToysFactory, MetalToysFactory

# this is where you can test my code as a client.


def client_code(sender, recipient):
    client = ClientProcessor(sender, recipient)
    client_proxy = ClientProxy(client)
    wooden_toys_factory = WoodenToysFactory()
    metal_toys_factory = MetalToysFactory()

    wooden_director = wooden_toys_factory.create_car_director()
    metal_director = metal_toys_factory.create_ship_director()

    client_proxy.create_product(wooden_director, mvp=True)
    client_proxy.create_product(metal_director)
    client_proxy.create_product(wooden_director)


if __name__ == "__main__":
    SENDER = "ToyLite@factory.com"
    RECIPIENT = "JohnSmith"
    client_code(SENDER, RECIPIENT)
