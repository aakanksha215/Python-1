n = int(input("Enter number : "))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")


l = ["Tini", "Shrey", "Rahul", "Rohit"] 

for name in l:
    if(name.startswith("R")):
        print(f"Hello {name}")