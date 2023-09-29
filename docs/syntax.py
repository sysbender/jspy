
# statements------------------------------------ 

# statement separator-terminator : = new line
# second separator-terminator : For multiple statements on one line = semicolon

for i in range(5): print('foo'); print('bar')

# line continuation
for i in \
    range(5):
    print(i)

# package import
'''


'''
from pprint import *  # from module import *
import pprint  # import module
from pprint import pprint # import class or function
# block ----------------------------------------------
# indentation

# inline comment
# block comment /docstring
''' BlockComment '''
""" BlockComment """
# (Documentation string when first line of module, class, method, or function) 
# - available in __doc__ attribute and help function

"""The module's docstring"""

class MyClass:
    """The class's docstring"""

    def my_method(self):
        """The method's docstring"""

def my_function():
    """The function's docstring"""

