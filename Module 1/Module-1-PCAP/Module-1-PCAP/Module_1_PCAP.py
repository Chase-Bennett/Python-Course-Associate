"""
from math import sin, pi

print(sin(pi / 2))

pi = 3.14


def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


print(sin(pi / 2))


pi = 3.14


def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


print(sin(pi / 2))

from math import sin, pi

print(sin(pi / 2))

import math

# for name in dir(math):
# print(name, end="\t")

print(math.factorial(10))


from math import e, exp, log

print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0))

"""
# 1,2,4 selected functions from random module
"""

from random import random

for i in range(0):
    print(random())


from random import random, seed, randrange

#seed(3223)

from random import randrange, randint

print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 1))

from random import randint

for i in range(1000):
    print(randint(1, 1000), end=',')


from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]



print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))





from platform import platform
 
print(platform())
print(platform(1))
print(platform(0, 1))

from platform import machine
 
print(machine())


from platform import processor
 
print(processor())




from platform import system
 
print(system())

from platform import version
 
print(version())



from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr)
"""
    #1.3 

print("Hello, World!")

