def autokey_vigenere_decrypt(ciphertext, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    decrypted = ''
    key_stream = key

    for i in range(len(ciphertext)):
        key_char = key_stream[i]
        c = ciphertext[i]
        shift = alphabet.index(key_char)
        p_index = (alphabet.index(c) - shift) % 26
        p = alphabet[p_index]
        decrypted += p
        key_stream += p  # Autokey: extend key with plaintext

    return decrypted

ciphertext = input("Enter encrypted string: ")
key = input("Enter key: ")

plaintext = autokey_vigenere_decrypt(ciphertext, key)
flag = f"{plaintext}"

print("Decrypted flag:", flag)
