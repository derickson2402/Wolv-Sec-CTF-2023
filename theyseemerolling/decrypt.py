#!/usr/local/bin/python
import os
from operator import xor
import itertools

try:
	cypher = open('output.txt', 'r').read()
	cypher = bytes.fromhex(cypher)
except:
	print("Couldn't open file")
	exit(1)

# Hacks because I dont understand python :/
# wB = b'\x77'
# cB = b'\x63'
# tB = b'\x74'
# fB = b'\x66'

wB = 119
cB = 99
tB = 116
fB = 102

blockLen = 8
numBlocks = int(len(cypher) // blockLen)
key = bytearray(8)
key[0:3] = cypher[0:3]
key[3] = xor(cypher[3], 1)
key[4] = xor(cypher[4], wB)
key[5] = xor(cypher[5], cB)
key[6] = xor(cypher[6], tB)
key[7] = xor(cypher[7], fB)

# Decrypt the message
def decryptBlock(key, block):
	rtrn = bytearray(len(key))
	for i in range(len(key)):
		rtrn[i] = xor(key[i], block[i])
	return rtrn

for blockAddr in range(0, len(cypher), blockLen):
	print(decryptBlock(key, cypher[blockAddr:blockAddr+blockLen]))
