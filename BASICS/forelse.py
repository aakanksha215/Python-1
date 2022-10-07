# for-else in python
#It will work only when we mention break

nums = [12,11,14,15,16,20,18]

for num in nums:
    if num%5==0:
        print(num)
        break
else:
    print('Not Found')    