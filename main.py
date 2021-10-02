from factories.toy_factory import WoodenToysFactory, MetalToysFactory


# this is where you can test my code as a client.
def client_code():
    wooden_toys_factory = WoodenToysFactory()

    director = wooden_toys_factory.create_car_director()
    director.create_full_product()

    builder = director.builder
    product = builder.product
    prototype = product.clone()

    product.list_parts()
    print()
    prototype.list_parts()


if __name__ == "__main__":
    client_code()
