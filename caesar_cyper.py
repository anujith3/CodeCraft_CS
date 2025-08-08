def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)
if __name__ == "__main__":
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))

    encrypted = caesar_cipher_encrypt(message, shift)
    print(f"Encrypted Message: {encrypted}")

    decrypted = caesar_cipher_decrypt(encrypted, shift)
    print(f"Decrypted Message: {decrypted}")
