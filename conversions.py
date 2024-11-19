def decimal_to_binary(n):
    return bin(n).replace("0b", "")

def binary_to_decimal(b):
    return int(b, 2)

def decimal_to_octal(n):
    return oct(n).replace("0o", "")

def octal_to_decimal(o):
    return int(o, 8)

def decimal_to_hexadecimal(n):
    return hex(n).replace("0x", "").upper()

def hexadecimal_to_decimal(h):
    return int(h, 16)