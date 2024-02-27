def caesar_encode(plain_text, shift):
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            cipher_text += chr(start + (ord(char) - start + shift) % 26)
        else:
            cipher_text += char
    return cipher_text