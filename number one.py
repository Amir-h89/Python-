num = int(input('enter number: '))
print('counters:')
sum = 0
for n in range(1,num+1):
    if num % n == 0:
        sum += 1
        print(n)

if sum == 2:
    print('number one')
else:
    print('morakab')
