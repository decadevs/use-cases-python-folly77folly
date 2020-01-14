# Document at least 3 use cases of iterators
ls=[1,2,4,5]
def print_each(ls):
    abc = iter(ls)
    while True:
        try:
            xxy=next(abc)
        except StopIteration :
            break
        else:
            print(xxy)

print_each(ls)



