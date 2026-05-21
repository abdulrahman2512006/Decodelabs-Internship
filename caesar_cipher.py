def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char  # spaces, punctuation unchanged
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    print("========================================")
    print("  DecodeLabs - Caesar Cipher Tool")
    print("========================================")

    while True:
        print("\nOptions:")
        print("  1. Encrypt")
        print("  2. Decrypt")
        print("  3. Quit")

        choice = input("\nChoose (1/2/3): ").strip()

        if choice == "3":
            break

        if choice not in ("1", "2"):
            print("Invalid choice. Try again.")
            continue

        text  = input("Enter text  : ")
        shift = int(input("Enter shift key (e.g. 3): "))

        if choice == "1":
            encrypted = caesar_encrypt(text, shift)
            decrypted = caesar_decrypt(encrypted, shift)
            print(f"\nOriginal  : {text}")
            print(f"Encrypted : {encrypted}")
            print(f"Decrypted : {decrypted}")

        elif choice == "2":
            decrypted = caesar_decrypt(text, shift)
            print(f"\nCiphertext : {text}")
            print(f"Decrypted  : {decrypted}")

    print("\nGoodbye! Stay secure. - DecodeLabs")

if __name__ == "__main__":
    main()
