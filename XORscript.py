def xor_hex_strings(hex1, hex2):
    if len(hex1) != len(hex2):
        raise ValueError("Hex strings must be of equal length")
    b1 = bytes.fromhex(hex1)
    b2 = bytes.fromhex(hex2)
    xored = bytes([x ^ y for x, y in zip(b1, b2)])
    try:
        return xored.decode()
    except UnicodeDecodeError:
        return xored.hex()

if __name__ == "__main__":
    s1 = input("Enter first hex string: ").strip()
    s2 = input("Enter second hex string: ").strip()
    try:
        result = xor_hex_strings(s1, s2)
        print("Decoded XOR result:", result)
    except Exception as e:
        print("Error:", e)
