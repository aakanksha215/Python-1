
import sys

# In python recursion limit is 1000

print(sys.getrecursionlimit())

# But we can set recursion 
sys.setrecursionlimit(2000)


def greet():
    print('Hello')
    greet()


greet()    