n = str(input("Input "))


for i in n:
    print(i.ljust(5), end="")
print()


def reverse_string():
    abc = len(n)
    flag = abc
    abc = 0
    for i in range(0, flag):
        abc = abc-1
        print(n[abc].ljust(5), end="")

reverse_string()