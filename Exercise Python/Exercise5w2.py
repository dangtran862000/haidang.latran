n=12
r=0.08

#Input the principal amount
P=float(input("Input the principal amount (initial investment): "))
T=float(input("Input the number of year (The length that money will be compounded for: "))

A=P*pow((1+(r/n)),n*T)

print("The final amount ",A,"after",T,"year")
