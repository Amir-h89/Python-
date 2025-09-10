print('puthagoras')

a = input('big side or small side? ')

x = int(input('enter big side size: '))

z = int(input('enter side size: '))

if a == 'big':    
    f = x**2 + z**2
    h = f**0.5
else:
    f = x**2 - z**2
    h = f**0.5

print('answer:', h)
