Python 3.15.0 (tags/v3.15.0:d220409, Oct  9 2026, 11:55:56) [MSC v.1951 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
A = 10
type (a)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    type (a)
NameError: name 'a' is not defined. Did you mean: 'A'?
>>> type (A)
<class 'int'>
>>> b= 12.2
>>> type(b)
<class 'float'>
>>> c= 1+22j
>>> type(c)
<class 'complex'>
>>> string "varshith"
SyntaxError: invalid syntax
>>> string=" varshith"
>>> type(string)
<class 'str'>
>>> list=[1,2,3,4]
>>> type(list)
<class 'list'>
>>> t=(1,2,3,40
...    T
...    
SyntaxError: '(' was never closed
>>> t=(1,2,3,4)
...    
>>> id
...    
<built-in function id>
>>> id(1)
...    
140704507716880
>>> id(2)
...    
140704507716912
>>> s={34,1243,333333,34213,443,23,23,23,23,23}
...    
>>> s
...    
{34, 34213, 333333, 23, 443, 1243}
>>> type(s)
...    
<class 'set'>
d={1:"one",2134:[1,2,3],5:(1,2,3)}
   
d
   
{1: 'one', 2134: [1, 2, 3], 5: (1, 2, 3)}
