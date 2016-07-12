Python 2.7.11 (v2.7.11:6d1b6a68f775, Dec  5 2015, 20:32:19) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> s = 'abcdefghijklmnopqrstuvwxyz'
>>> aString = s
>>> s
'abcdefghijklmnopqrstuvwxyz'
>>> aString
'abcdefghijklmnopqrstuvwxyz'
>>> aStr=s
>>> 
>>> aStr
'abcdefghijklmnopqrstuvwxyz'
>>> s
'abcdefghijklmnopqrstuvwxyz'
>>> s/2

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    s/2
TypeError: unsupported operand type(s) for /: 'str' and 'int'
>>> low = s[0]
>>> high = s[(len(s)]
	 
SyntaxError: invalid syntax
>>> high = s[len(s)]

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    high = s[len(s)]
IndexError: string index out of range
>>> high = s[len(s)-1]
>>> high
'z'
>>> len(s[0])
1
>>> middle = s[(len(s[0]) + len(s[len(s)-1]))/2]
>>> middle
'b'
>>> s[0]
'a'
>>> len(s[0])
1
>>> s[len(s)-1]
'z'
>>> middle=''
>>> middle = s((len(s[0]) + len(s))/2)

Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    middle = s((len(s[0]) + len(s))/2)
TypeError: 'str' object is not callable
>>> middle = s[((len(s[0]) + len(s))/2)]
>>> middle
'n'
>>> low
'a'
>>> low < middle
True
>>> middle > high
False
>>> middle
'n'
>>> 
>>> test = 'q'
>>> 
>>> test
'q'
>>> middle < test
True
>>> 
>>> def isIn(char, aStr):
	if char == test:
		print 'Correct,' char, 'is the character!'
		
SyntaxError: invalid syntax
>>> def isIn(char, aStr):
	if char == test:
		return char
	else:
		s = aStr
		low = s[0]
		high = s[len(s)-1]
		middle = s[(len(s[0]) + len(s))/2]
		if char < test
		
SyntaxError: invalid syntax
>>> 
>>> 
>>> def isIn(char, aStr):
	s = aStr
	low = s[0]
	high = s[(len(s) - 1)]
	middle = s[((len(s[0]) + len(s))/2)]
	
	if char == test:
		return char
	else:
		if char < test
		
SyntaxError: invalid syntax
>>> 
>>> len(s[0])
1
>>> len(s)
26
>>> s[len(s)]

Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    s[len(s)]
IndexError: string index out of range
>>> s[len(s)-1]
'z'
>>> s[1:]
'bcdefghijklmnopqrstuvwxyz'
>>> start = len(s[0])
>>> finish = len(s)
>>> start
1
>>> finish
26
>>> beginning = start
>>> end = finish
>>> mid = (beginning+end)/2
>>> mid
13
>>> s[13:]
'nopqrstuvwxyz'
>>> s[:13]
'abcdefghijklm'
>>> 
>>> s1 = s
>>> s1
'abcdefghijklmnopqrstuvwxyz'
>>> return 3
SyntaxError: 'return' outside function
>>> s_low = s[13:]
>>> s_low
'nopqrstuvwxyz'
>>> s_low = s[:13]
>>> s_low
'abcdefghijklm'
>>> s1
'abcdefghijklmnopqrstuvwxyz'
>>> s1 = s[:(len(s)/2)]
>>> s1
'abcdefghijklm'
>>> s1 = s[:(len(s1)/2)]
>>> s1
'abcdef'
>>> s1 = s[:(len(s1)/2)]
>>> s1
'abc'
>>> 
