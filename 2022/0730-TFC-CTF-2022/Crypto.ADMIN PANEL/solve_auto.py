from ast import While
from dataclasses import replace
from pwn import *
import os
from Crypto.Cipher import AES

def xor(byte, bytes_second):
    d = b''
    for i in range(len(bytes_second)):
        d += bytes([byte ^ bytes_second[i]])
    return d

def decrypt(ciphertext):
    KEY = os.urandom(16)
    iv = ciphertext[:16]
    ct = ciphertext[16:]
    cipher = AES.new(KEY, AES.MODE_ECB)
    pt = b''
    state = iv
    for i in range(len(ct)):
        b = cipher.encrypt(state)[0]
        c = b ^ ct[i]
        pt += bytes([c])
        state = state[1:] + bytes([ct[i]])
    return pt

def decoder(r_byte_hex):
    token = '0000000000000000000000000000000000000000000000000000000000000000'
    hex_token = bytes.fromhex(token)
    r_byte = bytes.fromhex(r_byte_hex)
    xorred = xor(r_byte[0], hex_token)
    PASSWORD = decrypt(xorred)
    PASSWORD_hex = PASSWORD.hex()
    return PASSWORD_hex


def stop(text):
    stopsign = 0
    while stopsign != 1:
        startText = proc.recvline()
        print(str(startText).replace("\\n", ""))
        if str(startText).find(text)>1: 
            stopsign = 1
            return str(startText)
            break

server = '01.linux.challenges.ctf.thefewchosen.com'
port = 60939

while True:
    proc = remote(server, port)
    response = proc.recvline()

    # Change Password
    stop("====")
    proc.sendline(b'2')
    print('>>> 2')
    proc.sendline('0000000000000000000000000000000000000000000000000000000000000000')
    print('>>> 0000000000000000000000000000000000000000000000000000000000000000')

    # Get XORing
    r_byte_hex = stop("XORing")
    r_byte_hex = r_byte_hex.replace("b'> Token > XORing with: ","").replace("\\n'","")
    # r_byte_hex = input("b'> Token > XORing with: ")
    stop("====")
    while True:
        proc.clean
        proc.sendline(b'1')
        proc.sendline(decoder(r_byte_hex));
        stop("====")
    exit()

