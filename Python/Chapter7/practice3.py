# program for factorial

n = int(input("Enter : "))

prod = 1
for i in range(1, n+1):
    prod = prod * i

print(prod)    