print('to finish: -1')
n = 0
sum = 0

while True:
    number = float(input('enter number: '))
    if number == -1:
        break
    else:
        sum += number
        n += 1

print('average is:', sum / n)
