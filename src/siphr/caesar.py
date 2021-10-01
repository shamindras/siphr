import string
from typing import List, Dict

def get_substitution_map(alphabets: List[str], shift: int) -> Dict[int, int]:
    """Get substitution cipher map for a given list of alphabet strings and
common forward shift parameter. The map will be for the concatenated shifted
alphabet strings.

    Args:
        alphabets (List[str]): List of alphabet strings.
        shift (int): A integer shift for the substitution cipher.

    Returns:
        Dict[int, int]: A dictionary mapping for the shifted substitution
cipher.
    """
    shifted_alphabets = [alphabet[shift:] + alphabet[:shift]
                         for alphabet in alphabets]
    return str.maketrans("".join(alphabets), "".join(shifted_alphabets))

def get_reverse_map(cipher_map: Dict[int, int]) -> Dict[int, int]:
    """Reverse a given (key-value) cipher map.

    Args:
        cipher_map (Dict[int, int]): A cipher map, typically derived from the
substitution cipher with given shift.

    Returns:
        Dict[int, int]: The reversed (key-value) cipher map.
    """
    return {val: ky for ky, val in cipher_map.items()}

def get_translate(plain_text: str, cipher_map: Dict[int, int]) -> str:
    """Get a plain text translation based on a given substitution cipher map.

    Args:
        plain_text (str): The input plain text to encipher or decipher.
        cipher_map (Dict[int, int]): The given key-value cipher map.

    Returns:
        str: The converted plain text after applying the substitution cipher
map.
    """
    return plain_text.translate(cipher_map)

# Get input plain_text to convert
plain_text = 'THE QUICK BROWN FOX JUMPS OVER THE LAZY dog?!#$@$a%% dOG'
print(f"plain_text: {plain_text}")

encipher_map = get_substitution_map(alphabets=[string.ascii_lowercase,
                                               string.ascii_uppercase],
                                    shift=3)

# Encryption
# encipher_text = plain_text.translate(encipher_map)
encipher_text = get_translate(plain_text=plain_text, cipher_map=encipher_map)
print(f"encipher_text: {encipher_text}")

# Decryption
decipher_map = get_reverse_map(cipher_map=encipher_map)
decipher_text = get_translate(plain_text=encipher_text, cipher_map=decipher_map)
print(f"decipher_text: {decipher_text}")
