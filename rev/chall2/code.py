#!/usr/bin/env python3
import string

flag = open("./flag.txt","r").read()
k = open("./key.txt","r").read() #hint: The professor who was never truely evil
key = k[:-1]
alphabet = string.ascii_lowercase
assert all([c in alphabet for c in alphabet])
assert len(key) == 5
enc = ''
for i in key:
    for j in range(len(flag)):
        x = ord(flag[j])
        k = ord(i)
        enc += chr(x^k)
    flag = enc
    if i!=key[-1]:
        enc = ''
print(enc)
