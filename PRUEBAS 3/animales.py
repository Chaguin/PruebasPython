# -*- coding: utf-8 -*-
class Animal:

    def __init__(self, age, weight):
        self.age = age
        self.__weight = weight

    def __privateMethod(self):
        print (self.weight)

    def getWeight(self):
        return self.__weight

    def eat(self, kmg):
        self.__weight += kmg
        print ("The animal weights: ",self.__weight, "after eating.")

class Bird(Animal):

    def fly(self):
        print ("I fly as a bird!")

class Mammal(Animal):
    def fly(self):
        print ("I can not tly, I am a mammal")

class Ostrich(Animal, Bird):
    def fly(self):
        print ("I can no fly, I am a Ostrich.")

class Platypus1(Mammal, Bird):
        pass

class Platypus2(Bird, Mammal):
        pass

animal1 = Animal(3,0.5)
animal1.eat(0.1)

canary = Bird(1, 0.45)
canary.eat(10)
canary.fly()

ostrich = Ostrich(5,30)
ostrich.fly()

platypus = Platypus1(2,3)
platypus.fly()

#print bear.getWeight()
#bear.__privateMethod()
