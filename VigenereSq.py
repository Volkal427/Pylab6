def vigenere_header(alphabet):
    alpha_len = len(alphabet)
    print('|   ', end='')
    for i in range(alpha_len):
        print(f"| {alphabet[i % alpha_len]}", end=' ')
    print('|')
    print(f"{'|---' * (alpha_len + 1)}|")

def vigenere_sq(alphabet):
    alpha_len = len(alphabet)
    vigenere_header(alphabet)
    for shift in range(alpha_len):
        for i in range(alpha_len):
            if i == 0:
                c = alphabet[(i + shift) % alpha_len]
                print(f"| {c}", end=' ')
                print(f"| {c}", end=' ')
            else:
                print(f"| {alphabet[(i + shift) % alpha_len]}", end=' ')
        print("|")

def letter_to_index(letter, alphabet: str):
    return alphabet.lower().index(letter.lower())

def index_to_letter(index, alphabet):
    if 0 <= index < len(alphabet):
        return alphabet[index]
    return ''

def vigenere_index(key_letter, plaintext_letter, alphabet):
    return (letter_to_index(key_letter, alphabet) +
            letter_to_index(plaintext_letter, alphabet)) % len(alphabet)

def encrypt_vigenere(key, plaintext, alphabet):
    cipher_text = ''
    counter = 0

    for c in plaintext:
        if c == ' ':
            cipher_text += ' '
        elif c.upper() in alphabet:
            cipher_text += index_to_letter(
                vigenere_index(key[counter % len(key)], c, alphabet),
                alphabet
            )
            counter += 1

    return cipher_text

def undo_vigenere_index(key_letter, cipher_letter, alphabet):
    return (letter_to_index(cipher_letter, alphabet) -
            letter_to_index(key_letter, alphabet)) % len(alphabet)

def decrypt_vigenere(key, cipher_text, alphabet):
    plain_text = ''
    counter = 0

    for c in cipher_text:
        if c == ' ':
            plain_text += ' '
        elif c.upper() in alphabet:
            plain_text += index_to_letter(
                undo_vigenere_index(
                    key[counter % len(key)],
                    c,
                    alphabet
                ),
                alphabet
            )
            counter += 1

    return plain_text

key = 'BLUESMURF'
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
message = 'Hello World, I am here'

while True:
    print()
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        plaintext = input("Enter plain text: ")
        encrypted = encrypt_vigenere(key, plaintext, alphabet)
        print("Encrypted text:", encrypted)

    elif choice == '2':
        cipher_text = input("Enter cipher text: ")
        decrypted = decrypt_vigenere(key, cipher_text, alphabet)
        print("Decrypted text:", decrypted)

    elif choice == '3':
        print("Goodbye!")
        break

    else:
        print("Please enter 1, 2, or 3.")