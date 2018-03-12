# Bitwise Operations
print 0b1,    #1
print 0b10,   #2
print 0b11,   #3
print 0b100,  #4
print 0b101,  #5


# Converting
print bin(4)
print int("0b100",2)


# Shifting
shift_right = 0b1100 >> 2
shift_left = 0b1 << 2
print bin(shift_right)
print bin(shift_left)