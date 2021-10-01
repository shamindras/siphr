import string
from typing import List

def get_substitution_map(alphabet: str, shift: int) -> dict:
    alphabet_conv = alphabet.lower()
    shifted_alphabet = alphabet_conv[shift:] + alphabet_conv[:shift]
    return str.maketrans(alphabet_conv, shifted_alphabet)

def get_substitution_map2(alphabets: List[str], shift: int) -> dict:
    shifted_alphabets = [alphabet[shift:] + alphabet[:shift]
                         for alphabet in alphabets]
    return str.maketrans("".join(alphabets), "".join(shifted_alphabets))

def reverse_map(cipher_map: dict) -> dict:
    return {val: ky for ky, val in cipher_map.items()}

def get_substitution_encipher(plaintext: str, cipher_map: dict) -> str:
    return plaintext.translate(cipher_map)



table = get_substitution_map(alphabet=string.ascii_lowercase, shift=3)
table2 = get_substitution_map2(alphabets=[string.ascii_lowercase],
                               shift=3)
table3 = get_substitution_map2(alphabets=[string.ascii_lowercase,
                                          string.ascii_uppercase],
                               shift=3)


plaintext = 'THE QUICK BROWN FOX JUMPS OVER THE LAZY dog?!#$@$a dOG'
print(f"plaintext: {plaintext}")

# Encryption
encrypttext = plaintext.translate(table)
encrypttext2 = plaintext.translate(table2)
encrypttext3 = plaintext.translate(table3)
print(f"encrypttext: {encrypttext}")
print(f"encrypttext2: {encrypttext2}")
print(f"encrypttext3: {encrypttext3}")

# Decryption
reverse_table = reverse_map(cipher_map=table)
reverse_table2 = reverse_map(cipher_map=table2)
reverse_table3 = reverse_map(cipher_map=table3)
decrypttext = encrypttext.translate(reverse_table)
decrypttext2 = encrypttext2.translate(reverse_table2)
decrypttext3 = encrypttext3.translate(reverse_table3)
print(f"decrypttext: {decrypttext}")
print(f"decrypttext2: {decrypttext2}")
print(f"decrypttext3: {decrypttext3}")
