from Cryptodome.Util.number import inverse, long_to_bytes
from sympy import factorint
from math import prod

N = int(input("Insert N value: "))
e = int(input("Insert e value: "))
c = int(input("Insert c value, encrypted text: "))

factors = factorint(N)
print("[+] Factors:", factors)

# Generalized phi(n) for multiple primes
phi = 1
for p, e_ in factors.items():
    phi *= (p - 1) * p**(e_ - 1)

d = inverse(e, phi)
m = pow(c, d, N)
print("[+] Decrypted:", long_to_bytes(m))
