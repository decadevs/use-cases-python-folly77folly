# Document at least 3 use cases of the * and ** operators

# * in python is asterisks operator 
# case 1 to add numbers i dont now the numbers
def adder(*num):
    sum = 0
    
    for n in num:
        sum = sum + n
    print("Sum:",sum)

