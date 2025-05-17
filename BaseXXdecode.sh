#!/bin/bash

echo "[1] Base64"
echo "[2] Base32"
echo "[3] Base16 (hex)"
echo "[4] Base58 (requires Python)"
read -r -p "Choose encoding type: " type
read -r -p "Enter encoded string: " input

case $type in
  1)
    echo "$input" | base64 -d 2>/dev/null || echo "Base64 decoding failed"
    ;;
  2)
    input_upper=$(echo "$input" | tr '[:lower:]' '[:upper:]')
    len=${#input_upper}
    mod=$(( len % 8 ))
    if [ $mod -ne 0 ]; then
      pad=$(( 8 - mod ))
      input_upper="${input_upper}$(printf '=%.0s' $(seq 1 $pad))"
    fi
    echo "$input_upper" | base32 -d 2>/dev/null || echo "Base32 decoding failed"
    ;;
  3)
    echo "$input" | xxd -r -p 2>/dev/null || echo "Base16 (hex) decoding failed"
    ;;
  4)
    python3 - <<END
import base58
input_str = "$input"
try:
    decoded = base58.b58decode(input_str)
    print(decoded.decode())
except UnicodeDecodeError:
    print(decoded.hex())
except Exception as e:
    print(f'Decoding failed: {e}')
END
    ;;
  *)
    echo "Invalid option"
    ;;
esac


