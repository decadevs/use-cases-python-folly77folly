# Document at least 3 use cases of generators

# a generator to get even numbers btw
def get_even(num):
    for number in range(start, stop):
        if number % 2 == 0:
            yield number
print(next(get_even(6)))


#get the square root of a list
lst = [1, 3, 4]
result = (numbs ** 2 for numbs in lst)
print(next(result))

# to get all the names that start with  letter a 
lst2 = ['tunde', 'solape', 'Anthony', 'ake']
def gen_first_letter(lst2):
    for name in lst2:
        if name.lower()[0:1] == 'a':
            yield name

print(next(gen_first_letter(lst2)))