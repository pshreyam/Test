def power(n):
    return lambda x: x ** n

i = 4

cube = power(3)
fourth = power(4)

print(cube(i))
print(fourth(i))