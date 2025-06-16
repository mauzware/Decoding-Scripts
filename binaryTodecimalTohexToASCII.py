b = input("Enter binary that you want to decode: ")

d = int(b,2)

h = hex(d)[2:]

string = bytes.fromhex(h).decode('ASCII')
print(string)
