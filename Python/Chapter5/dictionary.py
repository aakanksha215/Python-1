# dictionary is the collection of key-value pairs

# It is unordered
# It is mutable
# It cannot contain duplicate keys

d = {} # empty dictionary

marks = {
    "Tini" : 99,
    "Piyush" : 89,
    "Shrey" : 78
}

print(marks, type(marks))

print(marks["Piyush"])

# methods of dictionary --->

print(marks.items())

print(marks.keys())
print(marks.values())

marks.update({"Tini":97, "Pooja":77})
print(marks)

print(marks.get("Tini"))
print(marks["Tini"])

print(marks.get("Tini7")) # prints None
print(marks["Tini7"])  # Returns error