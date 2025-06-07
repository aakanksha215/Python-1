# c = 5 * (f-32)/9

def f_to_c(temp):
    return 5*(temp-32)/9

temp = int(input("Enter : "))

print(f_to_c(temp))