x = str("x")
print(x.rjust(2), end="")


def mutiple(n):
    for i in range(0, n+1):
        string = str(i)
        print(string.rjust(2), end="")
        for a in range(0, n+1):
            result = str(i*a)
            print(result.rjust(5), end="")
        print()


n = 12
for i in range(0, n+1):
    b = str(i)
    print(b.rjust(5), end="")
print()
mutiple(n)
