#Input the starting day number and length of your stay
StartDay= int(input("What is the starting day number: "))
LengthDay=int(input("What is the length of your stay: "))

#Sum of the the day of
SumDay=StartDay+LengthDay

#Divide the SumDay with 7 ( 7 days of the week )
ReturnDay=SumDay%7

#output the number of day of the week
print("The number of day of the week you will return on is ",ReturnDay)
