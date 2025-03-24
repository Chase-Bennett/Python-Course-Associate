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
    if strng == '' or strng.isspace():
        return [ ]
    # prepare a list to return
    lst = []
    # prepare a word to build subsequent words
    word = ''
    # check if we are currently inside a word (i.e., if the string starts with a word)
    inword = not strng[0].isspace()
    # iterate through all the characters in the string
    for x in strng:
        # if we are currently inside a string...
        if inword:
            # ... and the current character is not a space...
            if not x.isspace():
                # ... update the current word
                word = word + x
            else:
                # ... otherwise, we've reached the end of the word so we need to append it to the list...
                lst.append(word)
                # ... and signal the fact that we are outside the word now
                inword = False
        else:
            # if we are outside the word and we've reached a non-white character...
            if not x.isspace():
                # ... it means that a new word has begun so we need to remember it and...
                inword = True
                # ... store the first letter of the new word
                word = x
            else:
                pass
    # if we've left the string and there is a non-empty string in the word, we need to update the list
    if inword:
        lst.append(word)
    # return the list to the invoker
    return lst


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))

s1 = 'Where are the snows of yesteryear?'
s2 = s1.split()
s3 = sorted(s2)

print(s3)'
'''
'''

digits = [ '1111110',  	# 0
	   '0110000',	# 1
	   '1101101',	# 2
	   '1111001',	# 3
	   '0110011',	# 4
	   '1011011',	# 5
	   '1011111',	# 6
	   '1110000',	# 7
	   '1111111',	# 8
	   '1111011',	# 9
	   ]


def print_number(num):
	global digits
	digs = str(num)
	lines = [ '' for lin in range(5) ]
	for d in digs:
		segs = [ [' ',' ',' '] for lin in range(5) ]
		ptrn = digits[ord(d) - ord('0')]
		if ptrn[0] == '1':
			segs[0][0] = segs[0][1] = segs[0][2] = '#'
		if ptrn[1] == '1':
			segs[0][2] = segs[1][2] = segs[2][2] = '#'
		if ptrn[2] == '1':
			segs[2][2] = segs[3][2] = segs[4][2] = '#'
		if ptrn[3] == '1':
			segs[4][0] = segs[4][1] = segs[4][2] = '#'
		if ptrn[4] == '1':
			segs[2][0] = segs[3][0] = segs[4][0] = '#'
		if ptrn[5] == '1':
			segs[0][0] = segs[1][0] = segs[2][0] = '#'
		if ptrn[6] == '1':
			segs[2][0] = segs[2][1] = segs[2][2] = '#'
		for lin in range(5):
			lines[lin] += ''.join(segs[lin]) + ' '
	for lin in lines:
		print(lin)




print_number(int(input("Enter the number you wish to display: ")))

'''
# Input the text you want to encrypt.
text = input("Enter message: ")

# Enter a valid shift value (repeat until it succeeds).
shift = 0

while shift == 0:
    try:    
        shift = int(input("Enter the cipher shift value (1..25): "))
        if shift not in range(1,26):
            raise ValueError
    except ValueError:
        shift = 0
    if shift == 0:
        print("Incorrect shift value!")

cipher = ''

for char in text:
    # Is it a letter?
    if char.isalpha():
        # Shift its code.
        code = ord(char) + shift
        # Find the code of the first letter (upper- or lower-case)
        if char.isupper():
            first = ord('A')
        else:
            first = ord('a')
        # Make correction.
        code -= first
        code %= 26
        # Append the encoded character to the message.
        cipher += chr(first + code)
    else:
        # Append the original character to the message.
        cipher += char

print(cipher)
    
    






