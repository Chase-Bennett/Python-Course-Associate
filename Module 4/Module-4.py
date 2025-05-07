
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


def make_closure(par):
    
    loc = par

    def power(p):
        return p ** loc
    return power


fsqr = make_closure(2)
fcub = make_closure(3)

for i in range(5):
    print(i, fsqr(i), fcub(i))

'''


'''
from os import strerror


try:
    character_counter = line_counter = 0

    #with open(file_path, 'rt', encoding='utf-8') as stream:
      for line in stream:
           line_counter += 1
            for char in line:
                print(char, end='')
                character_counter += 1

    print(f"\n\nCharacters in file: {character_counter}")
    print(f"Lines in file:      {line_counter}")

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
    




from os import strerror

try:
    ccnt = lcnt = 0
   # s = open(r"C:/Users/02CHASE.BENNETT/Chase Bennett/Python Cert/Python-Course-Associate/Python-Course-Associate/Module 4/text.txt", 'rt')
    lines = s.readlines(20)
    while len(lines) != 0:
        for line in lines:
            lcnt += 1
            for ch in line:
                print(ch, end='')
                ccnt += 1
        lines = s.readlines(10)
    s.close()
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
    
from os import strerror

try:
	file = open('newtextungabunga.txt', 'wt') # A new file (newtext.txt) is created.
	for i in range(10):
		s = "line #" + str(i+1) + "\n"
		for char in s:
			file.write(char)
	file.close()
except IOError as e:
	print("I/O error occurred: ", strerror(e.errno))
    


from os import strerror

try:
    file = open('newtext.txt', 'wt')
    for i in range(10000):
        file.write("line #" + str(i+1)+"#what's up\n")
    file.close()
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))



data = bytearray(100)

for i in range(len(data)):
    data[i] = 100 - i

for b in data:
    print(hex(b))


from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))



from os import strerror

data = bytearray(10)

try:
    binary_file = open('file.bin', 'rb')
    binary_file.readinto(data)
    binary_file.close()

    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))





try:
    binary_file = open('file.bin', 'rb')
    data = bytearray(binary_file.read(5))
    binary_file.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
  

from os import strerror

srcname = input("Enter the source file name: ")
try:
    src = open(srcname, 'rb')
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)	

dstname = input("Enter the destination file name: ")
try:
    dst = open(dstname, 'wb')
except Exception as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    src.close()
    exit(e.errno)	

buffer = bytearray(65536)
total  = 0
try:
    readin = src.readinto(buffer)
    while readin > 0:
        written = dst.write(buffer[:readin])
        total += written
        readin = src.readinto(buffer)
except IOError as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    exit(e.errno)	
    
print(total,'byte(s) succesfully written')
src.close()
dst.close()
      



from os import strerror




try:
    test= open("lab1.txt", 'rb')
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)




import sys
from os import strerror
from collections import Counter

# 1) Read file
try:
    with open("lab1.txt", "r", encoding="utf-8") as f:
        text = f.read()
except OSError as e:
    print("Cannot open file:", strerror(e.errno), file=sys.stderr)
    sys.exit(e.errno)
    
# Initialize empty dict to hold counts
counts = counts = Counter(ch.lower() for ch in text if ch.isalpha())



dict_array = [
    {"letter": letter, "count": counts[letter]}
    for letter in sorted(counts)]


# Suppose `text` is the string you want to analyze:

text = test.read()
for ch in text:
    if ch != "":               # only count letters
        key = ch        # normalize to lowercase
        counts[key] = counts.get(key, 0) + 1

print(counts)


from os import strerror

# Initialize 26 counters for each Latin letter.
# Note: we've used a comprehension to do that.
counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
#file_name = input("Enter the name of the file to analyze: ")
try:
    file = open("lab1.txt", "rt")
    for line in file:
        for char in line:
            # If it is a letter...
            if char.isalpha():
                # ... we'll treat it as lower-case and update the appropriate counter.
                counters[char.lower()] += 1
    file.close()
    # Let's output the counters.
    for char in counters.keys():
        c = counters[char]
        if c > 0:
            print(char, '->', c)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
    

# Open (or create) "lab1.hist" in write-text mode; ensure it’s closed automatically
with open("lab1.hist", "wt") as file:
    # Write the header line
    file.write("Letter\tCount\n")

    # Iterate over (letter, count) pairs sorted by count, descending
    for char, count in sorted(
        counters.items(),           # get (letter, count) pairs
        key=lambda item: item[1],   # sort by count value
        reverse=True                # highest counts first
    ):
        # Only write letters that appeared at least once
        if count > 0:
            # Write the letter and its count, separated by a tab
            file.write(f"{char}\t{count}\n")



from os import strerror

counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
file_name = input("Enter the name of the file to analyze: ")
try:
    # explicit UTF-8 reading, ignore invalid bytes
    file = open(file_name, "rt", encoding="utf-8", errors="ignore")
    for line in file:
        for char in line:
            if char.isalpha():
                counters[char.lower()] += 1
    file.close()

    # write out with explicit UTF-8 encoding
    file = open(file_name + '.hist', 'wt', encoding="utf-8")
    # Note: we've used a lambda to access the directory's elements and set reverse to get a valid order.
    for char in sorted(counters.keys(), key=lambda x: counters[x], reverse=True):
        c = counters[char]
        if c > 0:
            file.write(char + ' -> ' + str(c) + '\n')
    file.close()
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))

    


class StudentsDataException(Exception):
    """Base exception for student data errors."""
    pass

class BadLine(StudentsDataException):
    """Raised when a line in the input file is malformed."""
    def __init__(self, lineno: int, content: str):
        self.lineno = lineno
        self.content = content.rstrip('\n')
        super().__init__(f"Line {lineno}: cannot parse '{self.content}'")

class FileEmpty(StudentsDataException):
    """Raised when the input file contains no data lines."""
    def __init__(self, filename: str):
        super().__init__(f"File '{filename}' is empty")

def read_and_aggregate(filename: str):
    students = {}  # key: (first, last), value: total points
    with open(filename, 'r', encoding='utf-8', errors='replace') as f:
        lines = f.readlines()

    if not lines:
        raise FileEmpty(filename)

    any_data = False
    for lineno, raw in enumerate(lines, start=1):
        line = raw.strip()
        if not line:
            # treat blank lines as malformed
            raise BadLine(lineno, raw)
        parts = line.split()
        if len(parts) != 3:
            raise BadLine(lineno, raw)
        first, last, score_str = parts
        try:
            score = float(score_str)
        except ValueError:
            raise BadLine(lineno, raw)

        any_data = True
        students[(first, last)] = students.get((first, last), 0.0) + score

    if not any_data:
        raise FileEmpty(filename)

    return students

def print_report(students):
    # Sort by first name, then last name
    for (first, last), total in sorted(students.items(), key=lambda x: (x[0][0], x[0][1])):
        # Align columns with 8-character width for names
        print(f"{first:<8} {last:<8} {total:.1f}")

def main():
    filename = input("Enter Prof. Jekyll's data file name: ").strip()
    try:
        students = read_and_aggregate(filename)
    except StudentsDataException as e:
        # Propagate with clear message; no sugar-coating.
        print(f"Error: {e}")
        return
    except FileNotFoundError:
        print(f"Error: file '{filename}' not found")
        return

    print_report(students)

if __name__ == "__main__":

    main()

import platform
import os
os.mkdir("my_first_directory")
print(os.listdir())


import os

os.makedirs("my_first_directory/my_second_directory/my_third_directory/my_fourth_directory/deep.txt")
os.chdir("my_first_directory/my_second_directory/my_third_directory/my_fourth_directory/deep.txt")
open("deep.txt", "w").close()
print(os.listdir())
    




import os

os.makedirs("my_first_directory/my_second_directory")
os.chdir("my_first_directory")
print(os.getcwd())
os.chdir("my_second_directory")
print(os.getcwd())
    


import os


try:
    os.makedirs("my_first_directory")
except FileExistsError:
    print("Directory already exists")

finally:
    print(os.listdir())


os.rmdir("my_first_directory")
print(os.listdir())
import os
 
os.makedirs("my_first_directory/my_second_directory")
os.removedirs("my_first_directory/my_second_directory")
print(os.listdir())



import os

returned_value = os.system("mkdir my_first_directory")
print(returned_value)


import os

def find(path, dir_name):
    path = os.path.abspath(path)

    found = False
    for root, dirs, files in os.walk(path):
        if dir_name in dirs:
            print(os.path.abspath(os.path.join(root, dir_name)))
            found = True
    if not found:
        print("Directory not found")

# Example usage
path = "./tree"
dir_name = "python"
find(path, dir_name)





import os

class DirectorySearcher:
    def find(self, path, dir):
        try:
            os.chdir(path)
        except OSError:
            # Doesn't process a file that isn't a directory.
            return

        current_dir = os.getcwd()
        for entry in os.listdir("."):
            if entry == dir:
                print(os.getcwd() + "/" + dir)
            self.find(current_dir + "/" + entry, dir)


directory_searcher = DirectorySearcher()
directory_searcher.find("./tree", "python")
from datetime import date

today = date.today()

print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)



from datetime import date

today = date(202, 2, 9)
print(today)
    

print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)

from datetime import date
import time

timestamp = time.time()
print("Timestamp:", timestamp)

d = date.fromtimestamp(timestamp)
print("Date:", d)
 
from datetime import date

d = date(1991, 2, 5)
print(d)

d = d.replace(year=1992)
print(d)
 
from datetime import date
 
d = date(2019, 11, 4)
print(d.isoweekday())
   



from datetime import time

t = time(14, 53, 20, 1)

print("Time:", t)
print("Hour:", t.hour)
print("Minute:", t.minute)
print("Second:", t.second)
print("Microsecond:", t.microsecond)
  

import time
import math 

class Student:
    def take_nap(self, seconds):
        print("I'm very tired. I have to take a nap. See you later.")
        time.sleep(seconds)
        print("I slept well! I feel great!")

student = Student()
student.take_nap(math.sqrt(math.sqrt(math.pi * 20)))
    

import time

timestamp = 5728891811
print(time.ctime(timestamp))


import time
print(time.ctime(0))
import time
print(time.ctime(60*5*60))


import time

timestamp = 1572879180
print(time.gmtime())
print(time.localtime())
    


import time


st = time.gmtime()
print(time.gmtime())
print(time.asctime(st))
print(time.mktime((st)))''' 


from datetime import datetime

print("today:", datetime.today())
print("now:", datetime.now())
print("utcnow:", datetime.utcnow())