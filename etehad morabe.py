print('(x + y)**2')

x = (input('enter the number(x): '))

y = (input('enter the number(y): '))

z = int(input('1_(x + y) 2_(x - y)? '))

q = x[0]
w = x[1:]

intq = int(q)

e = y[0]
r = y[1:]

inte = int(e)

a = intq ** 2
t = inte ** 2
u = 2 * intq * inte
if z == 1:
    print(a,w,'**2 +',t,r,'**2 +',u,w,r)

else:
     print(a,w,'**2 +',t,r,'**2 -',u,w,r)


