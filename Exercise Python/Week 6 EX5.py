n = str(input("Input "))


def check_palindrome(n):
    if len(n) % 2 == 0:
        return False
    else:
        for i in range(0, (len(n) % 2)+1):
            if str(n[i]) == n[len(n)-i-1]:
                return True
            else:
                return False


if check_palindrome(n):
    print("This ia a palindrome string")
else:
    print("This is not a palindrome string")


