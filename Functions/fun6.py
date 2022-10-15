# count even and odd numbers in list 

lst = [1,2,3,4,5,6,7,8,9]


def countList(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1    
    return even,odd        


evenNum,oddNum = countList(lst)
print(evenNum)
print(oddNum)    

print("Even : {} and Odd : {}".format(evenNum,oddNum))