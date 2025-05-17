import argparse

def derive_key_part(hex_encoded, known_plaintext, start_index):
    encrypted_bytes = bytes.fromhex(hex_encoded)
    derived_key = ""
    
    for i in range(len(known_plaintext)):
        derived_key += chr(encrypted_bytes[start_index + i] ^ ord(known_plaintext[i]))
    
    return derived_key

def xor_decrypt(hex_encoded, key):
    encrypted_bytes = bytes.fromhex(hex_encoded)
    decrypted_message = ""
    
    for i in range(len(encrypted_bytes)):
        decrypted_message += chr(encrypted_bytes[i] ^ ord(key[i % len(key)]))
    
    return decrypted_message

def main():
    parser = argparse.ArgumentParser(description='XOR Decryption')
    parser.add_argument('hex_encoded', type=str, help='Hex encoded string to decrypt')
    #parser.add_argument('key_length', type=int, help='Length of the encryption key')

    args = parser.parse_args()
    hex_encoded = args.hex_encoded
    key_length = int(input("Enter encryption key length: "))

    # Inputs for known plaintexts
    known_start_plaintext = input("Enter known starting plaintext (e.g. THM{ ): ").strip()
    known_end_plaintext = input("Enter known ending plaintext, YOU MUST PUT ONLY ONE CHARACTER!!! (e.g. } ): ").strip()

    # Derive the first part of the key using the known starting plaintext
    derived_key_start = derive_key_part(hex_encoded, known_start_plaintext, 0)
    print("Derived start of the key:", derived_key_start)

    # Derive the last character of the key using the known ending plaintext
    derived_key_end = derive_key_part(hex_encoded, known_end_plaintext, len(hex_encoded) // 2 - 1)
    print("Derived end of the key:", derived_key_end)

    # Since the key length is key_length, the derived key will repeat
    derived_key = (derived_key_start + derived_key_end)[0:key_length]
    print("Derived key:", derived_key)

    # Decrypt the full message using the derived key
    decrypted_message = xor_decrypt(hex_encoded, derived_key)
    print("Decrypted message:", decrypted_message)

if __name__ == '__main__':
    main()

