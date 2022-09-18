from random import randint, choice
from key_exchange_lib import Client


def main():
    # Initialize parameters
    p = choice([5, 7, 11, 13, 17, 19, 23, 29])
    g = randint(2, 200)
    secret_num1 = randint(2, 50)
    secret_num2 = randint(51, 100)

    # Create clients
    client1 = Client("Jack", p, g, secret_num1)
    client2 = Client("Jill", p, g, secret_num2)

    # Print clients
    print(client1)
    print(client2)

    # Generate partial keys
    partial_key1 = client1.generate_partial_key()
    partial_key2 = client2.generate_partial_key()

    # Print partial keys
    print(f"{client1.name} will send {client2.name} {partial_key1} as a partial key")
    print(f"{client2.name} will send {client1.name} {partial_key2} as a partial key")

    # Generate full key
    full_key1 = client1.generate_full_key(partial_key2)
    full_key2 = client2.generate_full_key(partial_key1)

    # Print full keys
    print(f"{client1.name} generated the key: {full_key1}")
    print(f"{client2.name} generated the key: {full_key2}")

    # Compare full keys
    print(
        f"Diffie-Hellman Key Exchange successful: {'False' if full_key1 != full_key2 else 'True'}"
    )


if __name__ == "__main__":
    main()
