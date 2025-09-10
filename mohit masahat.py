print('1_متوازي الاضلاع')
print('2_ذوذنقه')
print('3_لوزي')
print('4_مثلث')
print('5_دايره')
print('6_مستطيل')
print('7_مربع')

print('--------------------------------')
x = int(input('کدام؟ '))

if x == 1:
    m = int(input('1_محيط 2 مساحت: '))

    if m == 2:
        s = int(input('اندازه ضلع کوچک: '))
        a = int(input('اندازه ضلع بزرگ: '))
        print('(محيط =', (s + a) * 2,')')
    else:
        s = int(input('قاعده: '))
        a = int(input('ارتفاع: '))
        print('(مساحت =', s * a,')')
if x == 2:
    print('محيط = مجموع چهار ضلع')
    s = int(input('اندازه قاعده کوچک: '))
    a = int(input('اندازه قاعده بزرگ: '))
    h = int(input('ارتفاع: '))
    print('(مساحت = ',(s + a) * h / 2,')')
    
if x == 3:
    m = int(input('1_محيط 2 مساحت: '))

    if m == 2:
        s = int(input('اندازه ضلغ: '))
        print('(محيط = ', s * 4,')')

    else:
        s = int(input(' قطر بزرگ: '))
        a = int(input('قطر کوچک: '))

        print('(مساخت = ',s * a / 2,')')

if x == 4:
    print('محيط = مجموع سه ضلع')

    s = int(input('قاعده: '))
    a = int(input('ارتفاع: '))

    print('(مساحت = ',s * a / 2,')')

if x == 5:
    m = int(input('1_محيط 2 مساحت: '))

    if m == 2:
        s = int(input('قطر: '))
        print('(محيط = ',s * 3.14,')')
    else:
        s = int(input('شعاع: '))
        print('(مساحت = ',s * s * 3.14,')')

if x == 6:
    s = int(input('طول: '))
    a = int(input('عرض: '))

    print('(محيط = ',(a + s) * 2,')')
    print('(مساحت = ', a * s,')')

if x == 7:
    a = int(input('ضلع: '))

    print('(محيط = ',a * 4,')')
    print('(مساحت = ', a * a,')')
    
