

a = 5
b = 4



try:
    print(a/b)
    k = int(input("Enter the value"))
except ZeroDivisionError as e:
    print("Can not divide number by 0")
    print(e)
except ValueError as e:
    print("Invalid input")
    print(e)
except Exception as e:
    print("Exception")
    print(e)        
finally:
    print("In finally block")    