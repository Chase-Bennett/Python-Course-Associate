
'''
class Fib:
    def __init__(self, nn):
        print("__init__")
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("__iter__")
        return self

    def __next__(self):
        print("__next__")		
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret


for i in Fib(10):
    print(i)

def fun(n):
      for i in range(n):
         yield i

print(fun(10))

def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2
 
 
for v in powers_of_2(8):
    print(v)

def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2
 
 
t = [x for x in powers_of_2(5)]
print(t)


def powers_of_2(n):
    
    Generator that yields successive powers of two:
    2⁰, 2¹, …, 2ⁿ⁻¹.
    (Similar to the previous example.)
    
    power = 1               # Start at 2⁰
    for _ in range(n):      # Loop n times
        yield power         # Return current power
        power *= 2          # Advance to the next power

# As in the last version, but here we use list() to gather results for n=3
t = list(powers_of_2(3))
print(t)                   # Prints: [1, 2, 4]

def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2
 
 
for i in range(20):
    if i in powers_of_2(4):
        print(i)





def fibonacci(count):
    """
    Generator that yields the first `count` numbers of the Fibonacci sequence:
    1, 1, 2, 3, 5, ….
    """
    # Initialize the first two Fibonacci numbers
    first_number = 1
    second_number = 1

    for index in range(count):
        if index < 2:
            # The sequence always starts with two 1’s
            yield 1
        else:
            # Compute the next Fibonacci number
            next_number = first_number + second_number 
            # Shift the window: discard the oldest, keep the newest two
            first_number, second_number = second_number, next_number
            yield next_number

# Build and print the first 10 Fibonacci numbers
fibonacci_sequence = list(fibonacci(6))
print(fibonacci_sequence)  # Outputs: [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


the_list = []

for x in range(100):
    the_list.append(1 if x % 3 == 0 else 0)

print(the_list)

for v in [1 if x % 2 == 0 else 0 for x in range(10)]:
    print(v, end=" ")
print()
 
for v in (1 if x % 2 == 0 else 0 for x in range(10)):
    print(v, end=" ")
print()

two = lambda: 2
sqr = lambda x: x * x
pwr = lambda x, y: x ** y
 
for a in range(-2, 30):
    print(sqr(a), end=" ")
    print(pwr(a, two()))
    
def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')


def poly(x):
    return 2 * x**2 - 4 * x + 2


print_function([x for x in range(-20, 30)], poly)



list_1 = [x for x in range(30)]
list_2 = list(map(lambda x: 2 ** x, list_1))
print(list_2)

for x in map(lambda x: (x * x)/(4.34*x), list_2):
    print(x, end=' ')
print()
from random import seed, randint

seed()
data = [randint(-100,100) for x in range(50)]
filtered = list(filter(lambda x: x > 0 and x % 4 == 0, data))

print(data)
print(filtered)

def outer(par):
    loc = par
 
 
var = 1
outer(var)
 
#print(par)
#print(loc)
'''

def make_closure(par):
    
    loc = par

    def power(p):
        return p ** par
    return power


fsqr = make_closure(2)
fcub = make_closure(3)

for i in range(5):
    print(i, fsqr(i), fcub(i))