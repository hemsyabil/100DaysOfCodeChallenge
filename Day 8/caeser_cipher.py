direction = input("Enter 'encode' to to encrypt the message. Enter 'decode' to decrypt the message: ").lower()
text = input("Enter the message: ")
shift = int(input("Enter the shift amount: "))

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            encrypted_text += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            encrypted_text += char
    
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            decrypted_text += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
        else:
            decrypted_text += char
    
    return decrypted_text

if direction == 'encode':
    encrypted_text = encrypt(text, shift)
    print("Encrypted message:", encrypted_text)

elif direction == 'decode':
    decrypted_text = decrypt(text, shift)
    print("Decrypted message:", decrypted_text)

else:
    print("Invalid direction. Please enter 'encode' or 'decode'.")

