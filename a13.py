# generate multiplication table of a number uaing while loop
n = int(input('Enter a number : '))

i = 1
while i <= 10:
    k = n * i
    print(f'{n} x {i} = {k}')
    i += 1