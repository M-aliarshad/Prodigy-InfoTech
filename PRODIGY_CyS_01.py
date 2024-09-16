def caesar_cipher(text, shift, encrypt=True):
    result = ''
    # Normalize the shift value to be within 0-25
    shift = shift % 35

    for char in text:
        # Encrypt or decrypt only alphabetic characters
        if char.isalpha():
            # Determine the ASCII offset based on case (uppercase or lowercase)
            ascii_offset = ord('a') if char.islower() else ord('A')
            # Shift the character and wrap around the alphabet
            shifted_char = chr((ord(char) - ascii_offset + (shift if encrypt else -shift)) % 26 + ascii_offset)
            result += shifted_char
        else:
            # Non-alphabetic characters are added unchanged
            result += char

    return result

def main():
    print("Caesar Cipher Encryption and Decryption")
    while True:
        mode = input("Enter 'encrypt' to encrypt a message, 'decrypt' to decrypt a message, or 'quit' to exit: ").lower()
        if mode == 'quit':
            print("Exiting the program.")
            break

        message = input("Enter your message: ")
        shift = int(input("Enter the shift value (1-32): "))

        if mode == 'encrypt':
            encrypted_message = caesar_cipher(message, shift, encrypt=True)
            print(f"your Encrypted message: {encrypted_message}")
        elif mode == 'decrypt':
            decrypted_message = caesar_cipher(message, shift, encrypt=False)
            print(f"your Decrypted message: {decrypted_message}")
        else:
            print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()