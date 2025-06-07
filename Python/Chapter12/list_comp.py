l = [1, 5, 7, 11, 4, 9]

squareList = []

for item in l:
    squareList.append(item * item)

print(squareList)    

# using other method:-

squareList = [i*i for i in l]

print(squareList)