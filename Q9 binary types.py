print("BYTES EXAMPLE")
# creating a byte object
b=bytes([65,66,67,68])
print(b)
print(f'First Element: {b[0]}')
#iterating through  byte object
for byte in b:
    print(byte,end=' ')

print("\n\nBYTE ARRAY EXAMPLE")
#creating a bytearray object
ba=bytearray([65,66,67,68])
print(ba)
#modifying elemnts in a bytearray
ba[0]=97
print(ba)

print("\n\nMEMORY VIEW EXAMPLE")
#creating a memeory view obj
mv=memoryview(b)
print(mv)
print(f'Third Element: {mv[2]}')
print(f'Sliced Byte: {mv[1:3].tobytes()}')
mv_ba = memoryview(ba)
mv_ba[2] = 50
print(ba)

print("\nThis program is written by Tanisha. \nERPID: 0221BCA066")