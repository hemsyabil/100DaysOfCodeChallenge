alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Enter 'encode' to to encrypt the message. Enter 'decode' to decrypt the message: ").lower()
text = input("Enter the message: ").lower()
shift = int(input("Enter the shift amount: "))


def caeser(text, direction, shift):
    output_text = ''

    if direction == 'decode':
        shift *= -1

    for char in text:
        if char in alphabet:
            shifted_position = alphabet.index(char) + shift
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            output_text += char

    print(f"Here is the {direction}ed result: {output_text}")


caeser(text, direction, shift)

# def encrypt(original_message, shift_amount):
#     cipher_text = ""
#     for char in original_message:
#         if char in alphabet:
#             shifted_position = alphabet.index(char) + shift_amount
#             shifted_position %= len(alphabet)
#             cipher_text += alphabet[shifted_position]

#     return cipher_text

# def decrypt(cipher_text, shift_amount):
#     original_message = ""
#     for char in cipher_text:
#         if char in alphabet:
#             shifted_position = alphabet.index(char) - shift_amount
#             shifted_position %= len(alphabet)
#             original_message += alphabet[shifted_position]

#     return original_message


# if direction == 'encode':
#     cipher_text = encrypt(text, shift)
#     print("Encrypted message:", cipher_text)
# elif direction == 'decode':
#     original_message = decrypt(text, shift)
#     print("Decrypted message:", original_message)
# else:
#     print("Invalid direction. Please enter 'encode' or 'decode'.")
