# Write a Python program to returns sum of all divisors of a number 

def sum_off_division(n):
    divisors = [i for i in range(1, n+1) if n % i == 0]
    return sum(divisors)


n = 10

print(sum_off_division(n))