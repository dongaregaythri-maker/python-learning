# print 
# A
# A B
# A B C
# A B C D
# A B C D E 

for i in range (1 , 6):
    for j in range (1 , i + 1):
        print (chr(64 + j) , end = " ")
    print()

# A B C D E 
# A B C D 
# A B C
# A B 
# A

for i in range(6 , 0 , -1):
    for j in range (1 , i+1):
        print(chr(64+j) , end = " ")
    print()

# A
# A A 
# A A A
# A A A A
# A A A A A

for i in range (1 , 6):
    for i in range (1 , i + 1):
        print ("A" , end = " ")
    print()

# A 
# B B 
# C C C 
# D D D D 
# E E E E E

for i in range (1 , 6):
    for j in range (1 , i+1):
        print(chr(64+i) , end =" ")
    print()