



#-----------------------------------
#------- Built in Function---------
#-----------------------------------
# all()
# any()
# bin()
# id()
#-------------------------------------


# all()

x = [1,2,3,4]
x = [1,2,3,4 , []]

if all(x) :
    
    print("all Elements is True") # all Elements is True

else :
    print("there is at Least One Element false") # there is at Least One Element false


print("#" * 50) # ##################################################

# any()

x = [1,2,3,4 , []]
x = [0, 0, []]

if any(x) :
    
    print("there is at Least One Element True") #   there is at Least One Element True

else :
    print("there is no any true Elements") # there is no any true Elements


print("#" * 50) # ##################################################


# bin()

print(bin(100)) # 0b1100100



print("#" * 50) # ##################################################

# id()

a = 1
b = 2


print(id(a)) # 140735839138600
print(id(b)) # 140735839138632

