

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
# find the factorial of the number 5
number= 5
print(f"The factorial of {number} is: {factorial(number)}")