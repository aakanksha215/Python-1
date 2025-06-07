s = set()

s.add(20)
s.add(20.0)
s.add('20')

# floting point == int for same numerical values in python

print(s)
print(len(s))