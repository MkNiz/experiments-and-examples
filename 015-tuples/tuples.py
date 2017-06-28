bits = (2, 8, 16, 32, 64)

print("A tuple named 'bits':")
print(bits)
print("")

print("The first value of bits:")
print(bits[0])
print("")

print("The last value of bits:")
print(bits[-1])
print("")

print("Iterating through each value of bits:")
for bit in bits:
    print(bit)
print("")

print("Redefining bits:")
bits = (2, 256)
print(bits)
print("")

print("Attempting to overwrite an index of bits (should error):")
bits[0] = 420
