#!/usr/bin/env python3
    
# for i in range(0, 2880138, 4800):
offset1 = 4800
offset2 = 4800+4800

f = open('yougotrickrolled1.bmp', 'rb')
read = f.read()
imp1 = read[offset1:offset2]
f.close()

# print (imp1)

f = open('yougotrickrolled2.bmp', 'rb')
read = f.read()
imp2 = read[offset1:offset2]
f.close()

# print (imp2)

f = open('yougotrickrolled3.bmp', 'rb')
read = f.read()
imp3 = read[offset1:offset2]
f.close()

# print (imp3)

# Certain bytes are different
# for i in range(4800):
#     print (imp1[i] == imp2[i] == imp3[i])

print (chr(imp1[0]))
print (chr(imp2[0]))
print (chr(imp3[0]))

# param_3 = 3
# # print (param_2 & 0xfffffffe | (int)(uint)param_3 >> (0 & 0x1f) & 1U)
# print (ord(imp2[1]) & 0xfffffffe | param_3 >> (0 & 0x1f) & 1)