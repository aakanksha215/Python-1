f = open("file.txt")
lines = f.readlines()
print(lines, type(lines))

f.close()

# same cab be writtern using statement like:

with open("file.txt") as f:
    print(f.read())