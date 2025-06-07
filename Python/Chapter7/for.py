for i in range(5):
    print(i)


for i in range(0, 10, 2):
    print("Hi")
    print(i)


# for loop with else

l = [12,67,23,96]

for item in l:
    print(item)
else:
    print("Nothing")


# break -> exit loop now

for i in range(50):
    if(i == 15):
        break
    print(i)    


# continue -> skip this iteration

for i in range(50):
    if(i == 15):
        break
    print(i)  