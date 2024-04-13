def summ(num1, num2):
    res = num1 + num2
    print(res)

summ(50, 30)

name = 'Julia'
def hi(name, age):
    print('Hi I am ' + name + ' and I am ' + age)

hi(name, '32')

age = 32

if age == 32:
    print('I am 32')
elif age>28:
    print('My age more than 32')
else:
    print('My age less than 32')

if 'l' in name:
    print('I am Julia')
else:
    print('It is not my name')

pin = 1234
print('input your pin, please')
user_pin = int(input())

if pin == user_pin:
    print('What amount do you want to withdraw?')
else:
    print('Wrong pin, 2 tries left')
    user_pin = int(input())
    if pin == user_pin:
        print('What amount do you want to withdraw?')
    else:
        user_pin = int(input())
        print('Wrong pin, 1 try left')
        if pin == user_pin:
            print('What amount do you want to withdraw?')
        else:
            print('Card have been blocked, please, call your bank')


