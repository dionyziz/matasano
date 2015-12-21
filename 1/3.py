import binascii
import re

INPUT = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

def hexxor(a, b):
  a_bin = binascii.unhexlify(a)
  b_bin = binascii.unhexlify(b)

  return binascii.b2a_hex(binxor(a_bin, b_bin))

def binxor(a, b):
  a_ord = map(ord, a)
  b_ord = map(ord, b)

  c_ord = [a ^ b for (a, b) in zip(a_ord, b_ord)]
  c_bin = ''.join(map(chr, c_ord))

  return c_bin

def is_english(phrase):
  return re.match('^[a-zA-Z ,.!\'"()_\\[\\]:;?-]+$', phrase)

IN_BIN = binascii.unhexlify(INPUT)

for i in range(0, 256):
  out = binxor(IN_BIN, len(IN_BIN) * chr(i))
  if is_english(out):
    print(out)
