from logo import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo + "\n")


def caesar(text, shift, direction):
    if direction == "encode":
        cipher_text = ""
        for letter in text:
            letter_index = alphabet.index(letter)
            cipher_index = (letter_index + shift) % 26
            cipher_letter = alphabet[cipher_index]
            cipher_text += cipher_letter
        return cipher_text
    else:
        plain_text = ""
        for letter in text:
            letter_index = alphabet.index(letter)
            plain_index = (letter_index - shift + 26) % 26
            plain_letter = alphabet[plain_index]
            plain_text += plain_letter
        return plain_text


again = "yes"

while (again == "yes"):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    result = caesar(text, shift, direction)
    print("Result is: " + result)
    again = input("Type 'yes' to run again, type 'no' to quit: ")
