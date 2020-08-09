year = int(input("Input the year: "))


def leap_year():
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    else:
        if year % 4 == 0:
            return True
        else:
            return False


if leap_year():
    print("This is a leap year")
else:
    print("This is not a leap year")
