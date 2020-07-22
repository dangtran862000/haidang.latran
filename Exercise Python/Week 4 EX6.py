n=int(input("Input n: "))

def positive_n():
    for i in range(1,n+1):
        print(i," ",end="")

for i in range(1,n+1):
    positive_n()
    print("")
    n = n - 1