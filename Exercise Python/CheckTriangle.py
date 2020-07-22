a=int(input("The length A of triangle: "))
b=int(input("The length B of triangle: "))
c=int(input("The length C of triangle: "))

if a+b+c>2*max(a,b,c):
    if a==b==c:
        print("A Triangle of side X =",a,",Y =",b,",Z =",c, "is Equilateral Triangle")
    elif a==b or a==c or b==c:
        print("A Triangle of side X =",a,",Y =",b,",Z =",c, "is Isosceles Triangle")
    elif a*a+b*b+c*c==2*max(a*a,b*b,c*c):
        print("A Triangle of side X =",a,",Y =",b,",Z =",c, "is Right Triangle")
    else:
        print("A Triangle of side X =",a,",Y =",b,",Z =",c, "is Scalene Triangle")
else:
    print("NO TRIANGLE CAN BE FORMED")
