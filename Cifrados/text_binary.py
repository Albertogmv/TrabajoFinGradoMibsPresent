# -*- coding: utf-8 -*-
from BitsFunctions1 import addZerosBloqueDatos
import codecs
def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'



# print(text_to_bits("hola"))
# print(text_from_bits("01101000011011110110110001100001"))""