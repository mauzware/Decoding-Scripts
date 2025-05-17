def brute_force_rot(text):
    print("[*] Brute-forcing ROT ciphers (1–25):\n")
    for i in range(1, 26):
        result = ""
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - base + i) % 26 + base)
            else:
                result += char
        print(f"ROT{i:2}: {result}")

if __name__ == "__main__":
    cipher_text = input("Enter the ROT cipher text: ")
    brute_force_rot(cipher_text)
