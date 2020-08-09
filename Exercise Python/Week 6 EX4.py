n = str(input("Input "))

def reverse_string():
    string_len = len(n)
    string_digit = string_len
    string_len = 0
    for i in range(0, string_digit):
        string_len = string_len-1
        print(n[string_len].ljust(5), end="")

reverse_string()