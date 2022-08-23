#!/usr/local/bin/python
import random
import time
import math
import binascii
from Crypto.Util.number import *
from gmpy2 import invert

n = 68531945575030673723159238229738419654294394655118880671248139550780638960125162173761407168085284736406778946925400147391935575652090676870330263788690694314447484190818994341529811625035830371073653273023158261381539223774749525331551836094942346398187107530710672585302502733548986218340087916822102546719
encrypt_msg = '53ff4a80f17c061c8f1307fa2246b7f377568d49dd8c4e4ece777948e08565aa7e2baed8b832d4981f0800e05f67b9362a14d14284f8649383e02c9bf51b1f480c11f2ec29ab8a9867b379c72ad878c9f1a360f2d84dbc2498e00bee49e15b10f501e9d70a90fd703805395d0e5c94452630e32c86f0d3999072bc042892a619'
c1 = '1018d1c0a805357939fe718b94174d68843dab5f250405471e48bdb4ea566dd13cabe966cc823394b33ba4d236fdd24062109329111a2b203568dcf31d2a143618f9536d964d107533ee90b3b77ce776bde20ba8f432df0d030b33c4694b66abaad7a8825fbbe31b3d7cccfc60ab614b4fdcda89d00e2ae9882055a794c25fda'
c2 = '1544bac7e1f1cb1f53561c8c7c410b3def909ac1c9ad70d2abae4756666098dc63b13ef997ed5361a4becc1f2dd36ee2c403c73c6945cd019b595585a06ea278391026bf4ac322feae472394bc62f852850b9ee9b3af8dcf42ab706365d9bfb6627797332ef7dbc5f1f273368b7d0ec3a1429b9a3ea8a062821bd4970344d27e'
c1 = int(c1, 16)
c2 = int(c2, 16)

def egcd(a, b):
  if a == 0:
    return (b, 0, 1)
  else:
    g, y, x = egcd(b % a, a)
    return (g, x - (b // a) * y, y)

def commonMod(c1,c2,e1,e2):
  try:
    s = egcd(e1, e2)
    s1 = s[1]
    s2 = s[2]
    if s1<0:
        s1 = - s1
        c1 = invert(c1, n)
    elif s2<0:
        s2 = - s2
        c2 = invert(c2, n)
    m = pow(c1,s1,n)*pow(c2,s2,n) % n
    print(long_to_bytes(m).decode())
    print('DONE')
    return True
  except: 
    return False

def encrypt(msg):
  e = random.randint(1, n)
  pt = bytes_to_long(msg)
  ct = pow(pt, e, n)
  return binascii.hexlify(long_to_bytes(ct)).decode()

def get_pt(time, c1,c2):
  time = 1659782613
  random.seed(time)
  e = []
  for i in range(100):
    e.append(random.randint(1, n))
  for i in range(50):
    for j in range(50):
      k = i+j
      toggle = commonMod(c1,c2,e[i],e[k])
      if (toggle):
        exit()

def testEqual(msg, time,c1,c2):
  e_msg = encrypt(binascii.unhexlify(msg))
  if(e_msg == encrypt_msg):
    print('Find the time seed:')
    print(f"time = {time}")
    print(f"e_msg = {e_msg}")
    get_pt(time,c1,c2)
    exit()

def main():
  # time = 1659751436
  # time = 1659780939
  time = 1659782610
  # time = 1659782613
  random.seed(time)

  msg = '30'
  print(f'n = {n}')
  print(f'c1 = {c1}')
  print(f'c2 = {c2}')
  print(f'encrypt_msg = {encrypt_msg}')
  print(f'msg = {msg}')

  while True:
    time = time+1
    random.seed(time)
    for _ in range(10):
      testEqual(msg, time,c1,c2)

if __name__ == '__main__':
    main()
