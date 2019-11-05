# https://code.tutsplus.com/articles/understanding-args-and-kwargs-in-python--cms-29494
"""
What Are Args?

*args are used to pass non-keyword arguments. 
Examples of non-keyword arguments are fun(3,4), fun("foo","bar").

*args are usually used as a measure to prevent the program from crashing 
if we don’t know how many arguments will be passed to the function. 
This is used in C++ as well as other programming languages.
"""

"""
 What Are Kwargs?

**kwargs is a dictionary of keyword arguments. 
The ** allows us to pass any number of keyword arguments. 
A keyword argument is basically a dictionary.

An example of a keyword argument is fun(foo=2,bar=7).

**kwargs are just like *args except you declare the variables 
and the amount within the function arguments.
"""


def both(*args, **kwargs):
    print(args)
    print(kwargs)


both(1, 3, 5, name="Bob", age=25)


def myfunction(**kwargs):
    print(kwargs)


myfunction(**{"name": "flango", "age": 9999})

""" 
Exemplo Util
>>
def post(url, data=None, json=None, **kwargs):
    return request('post', url, data=data, json=json, **kwargs)
"""
