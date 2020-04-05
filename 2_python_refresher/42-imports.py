"""
    Notice that now we called __name__ from another module,
    and it didnt execute as __main__, because only the current
    file is the __main__.

    The file you run is __main__, and as soon as you import other files,
    Python will name them according to their path.

    How does python know where mymodule.py is? Does it just look in the current folder?
    The answer is with ```import sys  print(sys.path)```.
    So sys.path import paths where python will look in order to find files to import.
"""

from mymodule import divide

print(__name__)
