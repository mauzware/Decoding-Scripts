from sys import exit
from Cryptodome.Util.number import bytes_to_long, inverse, getPrime


def gen_key(k, e):
    """
    Generates RSA key with k bits
    """
    p = getPrime(k//2)
    q = getPrime(k//2)
    N = p*q
    d = inverse(e, (p-1)*(q-1))

    return ((N,e), d)

def encrypt(pubkey, m):
    N,e = pubkey
    return pow(bytes_to_long(m.encode('utf-8')), e, N)

def main(flag, e):
    pubkey, _privkey = gen_key(1024, e)
    encrypted = encrypt(pubkey, flag) 
    return (pubkey[0], encrypted)

if __name__ == "__main__":
    flag = input("Enter the value to encrypt: ").strip()
    e = int(input("Enter public exponent (e): "))
    N, cypher  = main(flag, e)
    print("N:", N)
    print("e:", e)
    print("cyphertext:", cypher)
    exit()
