p1 = "Buy now"
p2 = "Click here"
p3 = "Offer for you"
p4 = "Sale of the year"

msg = input("Enter: ")


if((p1 in msg) or (p2 in msg) or (p3 in msg) or (p4 in msg)):
    print("This comment is spam")
else:
    print("Not spam")    