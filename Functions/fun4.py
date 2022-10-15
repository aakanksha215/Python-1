# keywords variable length arguments

def person(name,**data):
    print(name)

    for i,j in data.items():
        print(i,j)


person('urvi',agr=22,city='Delhi',mob=94129476)    