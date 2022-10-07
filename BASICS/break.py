av = 10

x = int(input("Enter the number of candies"))

i=1

while i<=x:
    if i>av:
        print('Out of stock')
        break
    print('Candy')
    i=i+1

print("Thank you")