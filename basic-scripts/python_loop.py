# using for loop
n = int(input('Enter the number: '))

for i in range(1, n+1):
    for j in range(1, i+1):
        print('*', end='')
    print()

# use of if & elif statements
print('-' * 50)

if n%5 == 0 and n != 5:
    print(f'{n} is a multiple of 5.')
elif n%5 == 0 and n == 5:
    print(f'{n} is not a multiple of 5 but 5 itself.')
else:
    print(f'{n} is neither a multiple of 5 nor 5.')