def rot13():
    text = input("Enter text to encode/decode with ROT13: ")
    result = text.translate(str.maketrans(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
        "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    ))
    print(f"ROT13 result: {result}")


def rot47():
    text = input("Enter text to encode/decode with ROT47: ")
    result = ''.join(
        chr(33 + ((ord(c) - 33 + 47) % 94)) if 33 <= ord(c) <= 126 else c
        for c in text
    )
    print(f"ROT47 result: {result}")


def main():
	while True:
		choice = input("\nChoose which ROT cipher, rot13/rot47 or type 'exit' to quit: ").strip().lower()
		
		if choice == "rot13":
			rot13()
			
		elif choice == "rot47":
			rot47()
			
		elif choice == "exit":
			print("Exiting, bye!")
			break
			
		else:
			print("Invalid choice! Choose rot13 or rot47!")

if __name__ == "__main__":
	main()		





