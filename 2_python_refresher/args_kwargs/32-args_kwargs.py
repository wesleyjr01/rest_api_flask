"""
https://docs.python.org/3/glossary.html
----------------------------------------------------------------------------------
keyword argument: an argument preceded by an identifier (e.g. name=) in a 
function call or passed as a value in a dictionary preceded by **. For 
example, 3 and 5 are both keyword arguments in the following calls to complex():

# Ex1:
complex(real=3, imag=5)
complex(**{'real': 3, 'imag': 5})

# Ex2:
# Python program to illustrate 
# **kwargs for variable number of keyword arguments 

def myFun(**kwargs): 
	for key, value in kwargs.items(): 
		print ("%s == %s" %(key, value)) 

# Driver code 
myFun(first ='Geeks', mid ='for', last='Geeks')	 
# Output:
last == Geeks
mid == for
first == Geeks
----------------------------------------------------------------------------------
positional argument: an argument that is not a keyword argument. Positional 
arguments can appear at the beginning of an argument list and/or be passed as 
elements of an iterable preceded by *. For example, 3 and 5 are both positional 
arguments in the following calls:

# Ex1:
complex(3, 5)
complex(*(3, 5))

# Ex2:
# Python program to illustrate 
# *args for variable number of arguments 
def myFun(*argv): 
	for arg in argv: 
		print (arg) 
	
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks') 
# Output:
Hello
Welcome
to
GeeksforGeeks
----------------------------------------------------------------------------------
"""


def somefunc(day, *args, **kwargs):
    print(f"\nday : {day}")
    for arg in args:
        print(f"arg: {arg}")
    for key, val in kwargs.items():
        print(f"key: {key}, val:{val}")


# somefunc call without positional argument 'day'
# somefunc()

# somefunc call with positional argument 'day'
# somefunc("Thursday")

# somefunc call with positional argument 'day', and *args
# somefunc("Thursday", "blabla", "pingpong")


# somefunc call with positional argument 'day', and *args
# All implementations below are equal
args = ("blabla", "pingpong")
kwargs = {"Name": "SaltyMan", "Age": 21}
somefunc("Thursday", "blabla", "pingpong", **{"Name": "SaltyMan", "Age": 21})
somefunc("Thursday", "blabla", "pingpong", Name="SaltyMan", Age=21)
somefunc("Thursday", *("blabla", "pingpong"), Name="SaltyMan", Age=21)
somefunc("Thursday", *("blabla", "pingpong"), **{"Name": "SaltyMan", "Age": 21})
somefunc("Thursday", *args, **kwargs)
