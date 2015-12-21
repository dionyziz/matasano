import binascii

def hexxor(a, b):
  a_bin = binascii.unhexlify(a)
  b_bin = binascii.unhexlify(b)

  a_ord = map(ord, a_bin)
  b_ord = map(ord, b_bin)

  c_ord = [a ^ b for (a, b) in zip(a_ord, b_ord)]
  c_bin = ''.join(map(chr, c_ord))

  print(c_bin)

  return binascii.b2a_hex(c_bin)

IN_A = '1c0111001f010100061a024b53535009181c'
IN_B = '686974207468652062756c6c277320657965'

print(hexxor(IN_A, IN_B))
