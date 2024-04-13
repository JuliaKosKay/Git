class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('person have been created')

    def sing(self):
        print(self.name + ' is singing')

    def dance(self):
        print(self.name + ' is dancing')

man = Person('Petro', 25)
print(man.name)
print(man.age)
man.dance()

woman = Person('Alice', 22)
print(woman.name)
print(woman.age)
woman.sing()


