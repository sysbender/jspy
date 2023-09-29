
import pytest

# single asignment

# value of an assignment  -  assignment statements are not expressions and thus do not have a value

# chained assignment
def f():
    return 5
arr=list(range(10))
i = arr[i] = f()


# parallet assignment : js and py
a, b = 0, 1
assert a==0
assert b==1

# unpacking/destructuring assignmeng - if right-hand side of the assignment is a single variable, 
pair = [10, 20]
a, b = pair

# swaps the value of a and b
a, b = b , a
a, b = b, a+1 # use the init value of a to compute b

# equality - relational operator 
a == b

#colon equals (:=)  Walrus Operator. py3.8 

a = 10
if a == 10:
    print("yes")

if (a := 10) == 10:
    print("Yes")

assert 1 ==2

