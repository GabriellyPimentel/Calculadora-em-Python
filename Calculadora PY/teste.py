

#bin() oct() hex() int()

def numero_para_decimal(numero, base):
    decimal = int(numero, base)
    binario = bin(decimal)
    octal = oct(decimal)
    hexadecimal = hex(decimal)

    print('decimal : '+str(decimal))
    print('binario : '+str(binario[:2]))
    print('octal : '+str(octal[:2]))
    print('hexadecimal : '+str(hexadecimal[:2].upper()))