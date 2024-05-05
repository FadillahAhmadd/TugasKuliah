def print_odd_squares(n):
    for i in range(n):
        if i % 2 != 0:  
            print(i ** 2)


def print_even_squares(n):
    for i in range(n):
        if i % 2 == 0:  
            print(i ** 2)


n = int(input("Enter the value of n: "))
type = input("Enter type (odd/even): ")

if 1 <= n <= 20:  
    if type == "odd":
        print_odd_squares(n)
    elif type == "even":
        print_even_squares(n)
    else:
        print("Invalid type entered. Please enter 'odd' or 'even'.")
else:
    print("Invalid value of n. Please enter a value between 1 and 20.")
