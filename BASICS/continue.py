# continue will skip only that iteration

for i in range(1,101):
    if i%3==0 and i%5==0:
        continue
    print(i)

print('Bye')