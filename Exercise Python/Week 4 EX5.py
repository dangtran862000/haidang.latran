n=int(input("Triangular number: "))

def print_triangular_numbers(n):
    Sum=0
    for i in range(1,n+1):
        Sum=Sum+i
        print(i, end="\t")
        print(Sum)

print_triangular_numbers(n)
