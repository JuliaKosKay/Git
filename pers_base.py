# This file is module for import class and func to ken.py

class People():
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def descr(self):
        descr = self.name + ', he is ' + str(self.age) + ' and his height is ' + str(
            self.height) + ', also his weight is ' + str(self.weight)
        print('his name is ' + descr)
        return descr  # same as print

    def get_weight(self):
        print('Person weight is: ' + str(self.weight))

    def upd_weight(self, kg):
        self.weight = kg

guy = People('Killian', 35, 195, 94)
guy.upd_weight(78)
guy.descr()