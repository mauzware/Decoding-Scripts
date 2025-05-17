import string

# Ciphertext and key
ciphertext = input("Enter encrypted string: ")
key = input("Enter key: ")

# Alphabet
alphabet = string.ascii_lowercase
alpha_len = len(alphabet)

# Map characters to index
char_to_index = {ch: idx for idx, ch in enumerate(alphabet)}
index_to_char = {idx: ch for idx, ch in enumerate(alphabet)}

# Try Beaufort cipher decryption
def beaufort_decrypt(ciphertext, key):
    decrypted = []
    key_len = len(key)
    for i, c in enumerate(ciphertext):
        c_idx = char_to_index[c]
        k_idx = char_to_index[key[i % key_len]]
        # Beaufort decryption: P = (K - C) mod 26
        p_idx = (k_idx - c_idx) % alpha_len
        decrypted.append(index_to_char[p_idx])
    return ''.join(decrypted)

decrypted_beaufort = beaufort_decrypt(ciphertext, key)
decrypted_beaufort_flag = f"{decrypted_beaufort}"

print(decrypted_beaufort_flag)
