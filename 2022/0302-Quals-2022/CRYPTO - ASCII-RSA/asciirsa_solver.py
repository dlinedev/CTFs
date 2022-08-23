with open("flag.txt") as flag_file:
    flag = flag_file.read()
modulo = 256
public_key = 17

flag_encrypted = []
for c in flag:
    char_code = ord(c) * 2 - 1
    encrypted_char_code = pow(char_code, public_key, modulo)
    flag_encrypted.append(encrypted_char_code)

with open("rsa.enc", "wb") as encrypted_file:
    encrypted_file.write(bytes(flag_encrypted))


# Solusion
# get [n e c]  sol [d]
# φ(n) = φ(p^k) = p^k - p^(k-1) = (p-1) * p^(k-1) = p^k(1-1/p)
# φ(256) = 256 - 128 = 1 * 128 = 256*(1 - 0.5)
with open("rsa.enc", "rb") as encrypted_file:
    encrypted_flag = encrypted_file.read()

e = 17
n = 256  # φ(256) = 256 - 128 = 1 * 128 = 256*(1 - 0.5)
d = gmpy2.invert(17, 128)
flag_decrypt = []
for i in range(len(encrypted_flag)):
    c = encrypted_flag[i]
    ord_code = pow(c, d, n)
    org_ord_code = int((ord_code + 1) / 2)
    char_code = chr(org_char_code)
    flag_decrypt.append(char_code)
flag_meg = ''.join(flag_decrypt)
print(flag_meg)