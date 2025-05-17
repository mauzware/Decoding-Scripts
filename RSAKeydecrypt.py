from Cryptodome.Util.number import inverse, long_to_bytes
from sympy import factorint

N = int(input("Insert N value: "))
e = int(input("Insert e value: "))
c = int(input("Insert c value, encrypted text: "))

# Try to factor N (SymPy is slow but works for small N)
factors = factorint(N)
p, q = list(factors.keys())
assert p * q == N

# Compute private key
phi = (p - 1) * (q - 1)
d = inverse(e, phi)

# Decrypt
m = pow(c, d, N)
flag = long_to_bytes(m)
print("Flag:", flag.decode())
