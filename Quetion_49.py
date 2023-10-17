# Write a Python function to check whether a number is in a given range


def check_givin_range(n):
    if n in range(1,30):
        print("Number is in given range")

    else:
        print("number is not in given range")
    
n = int(input("Enter Number : "))
check_givin_range(n)

