

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)



x = 5
ans = fact(x)

print(ans)