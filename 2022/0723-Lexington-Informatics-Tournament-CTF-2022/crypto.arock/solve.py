from Crypto.PublicKey import RSA
from Crypto.Util.number import *
import base64
import gmpy2

# with open('C:\\Users\\Menglin\\Desktop\\pub.pem' ,'r') as f:
# key = RSA.import_key(f.read())
# e = key.e
# n = key.n
# print(key.size_in_bits())
# with open("C:\\Users\\Menglin\\Desktop\\flag.enc") as f:
# c = base64.b64decode(f.read())
# c = bytes.decode(c)
# print("e = {}".format(e))
# print("n = {}".format(n))
# print("c = {}".format(c))

e = 65537
n = 8721839759350069167278335804233522732628197837843780295129915563071581371083672792796544014245271677069445637593635290140076123157617389715458979685368727
c = 3831129304332239255280117442393824529915871197799278700713657686877437561020805823052809122048327006270135775002283258453774226602640149683603252934547033
# print(n.bit_length())
p=123411621633636675541493070644959834875873057348494554188657868973313372350191
q=70672758723177433011581077796363544664410141195648490771860623139983928782297

phi_n = (p-1)*(q-1)
d = gmpy2.invert(e,phi_n)
m = pow(c,d,n)
print(long_to_bytes(m).decode('UTF-8'))