# Python script for RSA key generation with selectable key size (1024, 2048, 4096)
from Crypto.PublicKey import RSA


def generate_rsa_keypair(key_size):
    key = RSA.generate(key_size)
    private_key = key.export_key().decode('utf-8')
    public_key = key.publickey().export_key().decode('utf-8')
    return private_key, public_key


def main():
    print("Select RSA key size:")
    print("1. 1024 bits")
    print("2. 2048 bits")
    print("3. 4096 bits")

    choice = input("Enter your choice (1-3): ")
    if choice == '1':
        key_size = 1024
    elif choice == '2':
        key_size = 2048
    elif choice == '3':
        key_size = 4096
    else:
        print("Invalid choice, defaulting to 2048 bits.")
        key_size = 2048

    private_key, public_key = generate_rsa_keypair(key_size)

    print("\nPrivate Key:\n")
    print(private_key)
    print("\nPublic Key:\n")
    print(public_key)


if __name__ == '__main__':
    main()
