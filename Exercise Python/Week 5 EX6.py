n = int(input("Input the number: "))

def is_prime(i):
    if i < 2:
        return False
    elif i == 2:
        return True
    else:
        for a in range(2, i-1):
            if i % a == 0:
                return False
        return True


for i in range(0, n+1):
    if is_prime(i):
        print(i)
