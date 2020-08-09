
print(str("x").rjust(2), end="")


def mutiplication_table(n):
    for i in range(0, n+1):
        print(str(i).rjust(2), end="")
        for a in range(0, n+1):
            print(str(i*a).rjust(5), end="")
        print()


n = 12
for i in range(0, n+1):
    print(str(i).rjust(5), end="")
print()
mutiplication_table(n)
