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
pass
#list
personal = ['Alex', 'Julia', 'Ivan']
print(personal[1])

nums = [1, 2, 4, 88, 13]
print(nums[1] + nums[4])

personal.append('Oleg')
print(personal)
pn = []
pn.append(personal)
pn.append(nums)
print(pn)

#cycles

students = ['Alexandr', 'Juliana', 'Ivana']

for f in students:
    if f == 'Juliana':
        var = 'Engineer ' + f
        print(var)
        print(f)
        print(len(f))

a = 10
while a > 1:
    #print(a) endless cycle
    ab = a-1
    #print(ab) endless cycle

range(0, 10, 2)
#start, stop, step
r = list(range(10))
print(r)

for f in range(10):
    print(f) # same

#list
fam = ['Anna', 'Kira', 'Jane']
print(fam)

#set
fam1 = {'Olga', 'Andrew', 'Mark'}
print(fam1)

#dict key:value

fam3 = {'father':'Konstantin', 'mother':'Yulia', 'son':'Kirill'}
print(fam3)
print(fam3['father'])

for k, v in fam3.items():
    print(k)
    print(v)
    print(k+' — '+v)







