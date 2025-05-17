def encode_hex():
	string = input("Enter string to encode to Hex: ")
	encoded = string.encode().hex()
	print(f"Encoded Hex value: {encoded}")
	
def decode_hex():
	string = input("Enter Hex string for decoding: ")
	try:
		decoded = bytes.fromhex(string).decode()
		print(f"Decode Hex value: {decoded}")
		
	except ValueError:
		print(f"Invalid hex value {string}")
		
	
def main():
	prompt = input("What you wanna do? encode or decode? ").strip().lower()
	
	if prompt == "encode":
		encode_hex()
		
	elif prompt == "decode":
		decode_hex()
		
	else:
		print("Invalid choice! You must type encode or decode!")
		
if __name__ == "__main__":
	main()


