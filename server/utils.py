import os, binascii

def random_hex_str(n):
    """
    Generate a random hexadecimal string of length n
    """
    return binascii.b2a_hex(os.urandom(n // 2)).decode()