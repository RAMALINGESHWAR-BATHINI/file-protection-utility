#pip install cryptography
from cryptography.fernet import Fernet

# Generate key
key = Fernet.generate_key()

with open("key.key", "wb") as key_file:
    key_file.write(key)

fernet = Fernet(key)

choice = input("1.Encrypt\n2.Decrypt\nChoose: ")

if choice == "1":
    
    text = input("Enter Text: ")

    with open("sample.txt", "w") as file:
        file.write(text)

    encrypted = fernet.encrypt(text.encode())

    with open("encrypted.txt", "wb") as enc_file:
        enc_file.write(encrypted)

    print("File Encrypted Successfully")

elif choice == "2":

    with open("encrypted.txt", "rb") as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted).decode()

    with open("decrypted.txt", "w") as dec_file:
        dec_file.write(decrypted)

    print("Decrypted Content:")
    print(decrypted)

else:
    print("Invalid Choice")