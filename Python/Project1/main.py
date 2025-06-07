# snake - water - gun game
import random

computer = random.choice([-1, 0, 1])

youstr = input("Enter your choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

you = youDict[youstr]

print(f"You Choose {reverseDict[you]}\nComputer Chose {reverseDict[computer]}")

if(computer == you):
    print("Its a draw")
else:
    if(computer == -1 and you == 1):
        print("You Win")
    elif(computer == -1 and you == 0):
        print("You Loose")
    elif(computer == 1 and you == -1):
        print("You loose")
    elif(computer == 1 and you == 0):
        print("YOu Loose")
    elif(computer == 0 and you == -1):
        print("You Loose")
    elif(computer == 0  and you == 1):
        print("You Win")
    else:
        print("Something went wrong")               