RSA Key Generator 🔑

Easily generate RSA Public and Private Keys with selectable key sizes: 1024, 2048, or 4096 bits!

🚀 Introduction

The RSA Key Generator project provides a simple and secure Python script to quickly generate RSA cryptographic key pairs. Users can effortlessly select their desired security level (1024, 2048, or 4096 bits) to fit their encryption needs.

🌟 Features

✅ Easy to use: Intuitive command-line interface.

✅ Secure: Uses the widely trusted PyCryptodome library.

✅ Flexible: Select between different key lengths based on security requirements:

1024 bits for standard security.

2048 bits recommended for robust security.

4096 bits for maximum security.

🛠️ Installation

Step 1: Clone the repository

git clone https://github.com/scdnz/Create-RSA-Python.git

Step 2: Navigate to the project directory

cd rsa-key-generator

Step 3: Install dependencies

pip install pycryptodome

▶️ Usage

Run the script from your command line:

python rsa_generator.py

Follow the on-screen instructions to select your preferred key size. Keys are displayed directly in the terminal.

📌 Example Output

Select RSA key size:
1. 1024 bits
2. 2048 bits
3. 4096 bits
Enter your choice (1-3): 2

Private Key:
-----BEGIN RSA PRIVATE KEY-----
...
-----END RSA PRIVATE KEY-----

Public Key:
-----BEGIN PUBLIC KEY-----
...
-----END PUBLIC KEY-----

🔒 Security Recommendations

2048-bit keys are widely recommended for secure applications.

For critical applications requiring strong cryptographic standards, prefer 4096-bit keys.

💻 Code Example

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

📖 License

This project is licensed under the MIT License. See the LICENSE file for details.

🙌 Contributing

Contributions are welcome! Feel free to open issues, submit pull requests, or suggest improvements.

© 2025 RSA Key Generator - Made with ❤️ by Your Name

