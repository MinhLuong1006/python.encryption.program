import string
import random

chars = " " + string.punctuation +  string.ascii_letters + string.digits
chars = list(chars)
keys = chars.copy()
random.shuffle(keys)

while True:
    print("Do you want to encrypt or decrypt?")
    print("E: Encryption/ D: Decryption")
    choice = input("Your choice: ").lower()

    if choice == "e":
        text = input("Enter a message: ")
        encrypted = ""
        for letter in text:
            index = chars.index(letter)
            encrypted += keys[index]
        print(f"Encrypted message: {encrypted}")

    if choice == "d":
        text = input("Enter a code: ")
        decrypted = ""
        for letter in text:
            index = keys.index(letter)
            decrypted += chars[index]
        print(f"Encrypted message: {decrypted}")




