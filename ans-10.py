#addition of octal and hexadecimal and result in binary

a='0o31'                                   # 25 in octal
b='0x27'                                   # 39 in hexadecimal
result=int(a, 8)+int(b, 16)
binaryEquivalent=bin(result)
print(binaryEquivalent)