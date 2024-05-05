def print_odd_squares(num):
    for i in range(num):
        if i % 2 != 0:  
            print(i ** 2) 

number = int(input("Enter a value for n: ")) 

if number >= 0:
    print_odd_squares(number)
else:
    print("Invalid value for n. Please enter a non-negative number.") 
