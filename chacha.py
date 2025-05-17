from binascii import unhexlify, hexlify

# Given ciphertexts and their known plaintexts
ct1 = unhexlify("5123dc5d95631fad3a30062e69c2f5b7e4")  # len: 18
ct2 = unhexlify("a7d3133a11ac4f114aa04bb9caf63909f117")  # len: 19

pt1 = b"Slide to the left"
pt2 = b"Slide to the right"

# Get keystream by XORing ciphertext and plaintext
ks1 = bytes([c ^ p for c, p in zip(ct1, pt1)])
ks2 = bytes([c ^ p for c, p in zip(ct2, pt2)])

# Combine keystream
keystream = ks1 + ks2  # Total length: 18 + 19 = 37 bytes

# Target message
target = b"Criss cross, criss cross"  # 23 bytes

# Encrypt only the first 23 bytes of the keystream
final_keystream = keystream[:len(target)]

# XOR target with keystream
encrypted = bytes([t ^ k for t, k in zip(target, final_keystream)])

# Output the hex string
print("Paste this into the challenge script when prompted:")
print(hexlify(encrypted).decode())


