alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" in alphabet) # this is in the alphabet- true
print("F" in alphabet)# this is not in the alphabet- false
print("1" in alphabet) # this is not in the alphabet- false
print("ghi" in alphabet) # this specific sequince is in alphabet- true
print("Xyz" in alphabet) # this sequence is in the alphabet, but not with a cap X -false




alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" not in alphabet) # this is in the alphabet- false
print("F" not in alphabet) # this is not in the alphabet- true
print("1" not in alphabet) # this is not in the alphabet- true
print("ghi" not in alphabet) # this specific sequince is in alphabet- false
print("Xyz" not in alphabet)# this sequence is in the alphabet, but not with a cap X -true
'''
alphabet = "abcdefghijklmnopqrstuvwxyz"
del alphabet[0] # this will not work because strings are immutable
alphabet.append("A") # this will not work because strings are immutable'
'''
'''


# Demonstrating min() - Example 1: ~A~lowest ASCII value
print(min("aAbByYzZ"))


# Demonstrating min() - Examples 2 & 3: ~[ ] ~ 0~lowest ASCII value
t = 'The Knights Who Say "Ni!"'
print('[' + min(t) + ']')

t = [0, 1, 2]
print(min(t))

# Demonstrating max() - Example 1: ~z~highest ASCII value
print(max("aAbByYzZΔω φ"))
print(max("aAbByYzZ")) 

# Demonstrating max() - Examples 2 & 3: ~Y~2~ highest ASCII value
t = 'The Knights Who Say "Ni!"'
print('[' + max(t) + ']')

t = [0, 1, 2]
print(max(t))




# Demonstrating the index() method:
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))
#print("aAbByYzZaA".index("Z", 5, 6)) # this will not work because the index is out of range~~ from 5 to 6



# Demonstrating the list() function:
print(list("abcabc"))

'''
# Demonstrating the count() method:
print("abcabc".count("b"))
print('abcabc'.count("d"))
#2.3 section 3

# Demonstrating the capitalize() method:
print('aBcD'.capitalize())



print("Alpha".capitalize())
print('ALPHA'.capitalize())
print(' Alpha'.capitalize())
print('123'.capitalize())
print( "abgd" . capitalize  ())
print("αΒΓδ".capitalize())

def mysplit(strng):
# return [] if string is empty or contains whitespaces only
    
    # prepare a list to return

    # prepare a word to build subsequent words

    # check if we are currently inside a word (i.e., if the string starts with a word)

    # iterate through all the characters in the string

        # if we are currently inside a string...

            # ... and the current character is not a space...

                # ... update the current word

                # ... otherwise, we've reached the end of the word so we need to append it to the list...

                # ... and signal the fact that we are outside the word now

            # if we are outside the word and we've reached a non-white character...

                # ... it means that a new word has begun so we need to remember it and...

                # ... store the first letter of the new word

    # if we've left the string and there is a non-empty string in the word, we need to update the list

    # return the list to the invoker


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
print("Hello world")