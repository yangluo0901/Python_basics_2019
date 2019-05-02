# single line comment#
''' multi-lines comment'''
a = 10 #  int
b = "hello world" # string
c= True # boolean   bool
d = 10.01 # float
e = None
print(e)

# string formmat 1
print("%6.2f" % (a+d))

# string format 2:
print("{0:6.2f}".format(a+d))

# concatenate string with int 1:
print("hello world {0}".format(c))

# concatenate string with int 2:
print("hello world "+ str(a))

# raw string
print("hello\nworld")
print(r"hello\nworld")

# type casting
print(".................type cast................")
f = "4"
print(a+int(f))

# logic operator

print("...............logic operator.............")
print("and = &&, or = ||, not = !")
