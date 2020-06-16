def num(a):
    print('The Orginal list is:',a)
    return sum(i**3 for i in a)
b=[3,5,7]
print('Sum Of List Cube Is:',num(b))