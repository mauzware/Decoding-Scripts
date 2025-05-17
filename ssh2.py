import math


N = int(input("Enter your N value: "))

# Step 1: Compute integer square root
sqrt_n = int(math.isqrt(N))

# Step 2: Convert to bytes
flag_bytes = sqrt_n.to_bytes((sqrt_n.bit_length() + 7) // 8, 'big')

# Step 3: Try decoding
try:
    flag_str = flag_bytes.decode()
    print("Possible flag:", flag_str)
except:
    print("Byte output (non-UTF-8):", flag_bytes)
