#!/usr/bin/env python
# -*- coding: utf-8 -*-

###################################



###################################




###################################



###################################




###################################



###################################




###################################



###################################
# 面向对象编程

'''
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print '%s: %s' %(self.name, self.score)

lihua = Student('lihua', 95)

lihua.print_score()
'''

class Animal(object):
    def run(self):
        print 'Animal is running...'

class Dog(Animal):
    def run(self):
        print 'Dog is running...'

class Cat(Animal):
    def run(self):
        print 'Cat is running...'

def run_twice(animal):
    animal.run()
    animal.run()

dog = Dog()
run_twice(dog)

###################################
# 装饰器

def now():
    print '2017-3-5'





###################################
# 匿名函数

# print map(lambda x: x*x, [1,2,3,4,5,6,7,8]);


###################################

'''
def f():
    fs=[]
    for i in range(1,4):
        def g(n):
            def g1():
                return n*n
            return g1
        fs.append(g(i))
    return fs

f1,f2,f3 = f()

print f1(), f2(), f3()
'''

###################################

'''
def clac_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

print clac_sum(*(1,2,3,4,5))
'''

###################################

'''
def fn(a, b):
    return 10*a + b

def char2num(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]

def str2num(s):
    return reduce(fn, map(char2num, s))

def lowup(s):
    return s[:1].upper() + s[1:].lower()


print map(lowup, ['adam', 'LISA', 'barT'])
'''

###################################

'''
def odd(n):
    return n % 2 == 0

print filter(odd, [1,2,3,4,5,6,7,8])
'''

###################################

'''
def su(n):
    for i in range(2, n):
        if n % i == 0:
            return True
    return False

print filter(su, range(1,101))
'''

###################################
