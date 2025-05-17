from Cryptodome.PublicKey import RSA
import base64

# Read and parse the public key
with open("ssh_host_rsa_key.pub", "r") as f:
    lines = f.read().strip().splitlines()
    key_b64 = ''.join(lines[1:-1])  # Remove BEGIN/END lines

    key_der = base64.b64decode(key_b64)
    pubkey = RSA.import_key(key_der)

    print("Modulus N =", pubkey.n)
    print("Exponent e =", pubkey.e)
