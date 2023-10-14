# Write a Python function to check whether a number is perfect or not.

n = int(input("Enter Number : "))
def is_perfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n
print(is_perfect(n))