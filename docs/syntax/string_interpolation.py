age = 30
result = 'he is 30'
# f-string
assert f"he is {age}" == result
# .format method
assert "he is {age}".format(age=age) == result
# old style % operator
# https://docs.python.org/3/library/stdtypes.html#old-string-formatting
assert "he is %(age)d" % {'age': age} == result