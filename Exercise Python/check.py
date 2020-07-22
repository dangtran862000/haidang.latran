n=int(input("Input n "))
print("Number | Steps")
for i in range(n+1):
    print(i, end="\t")
    flag = 0
    while i > 1:
        flag=flag+1
        if i % 2 == 0:
           i = i / 2
        else:
           i = i * 3 + 1
    print(" \t",flag)