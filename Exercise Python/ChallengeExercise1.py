n=int(input("Input n "))
i=0
a=n
for i in range(n+1):
    flag = 0
    while a>1:
       print(i)
       if a%2==0:
         a=a/2
       else:
         a=a*3+1
       flag=flag+1
    print(flag,"step")