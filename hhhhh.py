def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))
print("Factorial of", num, "is:", factorial(num))





# def fibonacci(n):
#     if n <= 1:
#         return n
    
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# terms = int(input("Enter number of terms: "))
# print("Fibonacci series:")


# for i in range(terms):
    
#     print(fibonacci(i), end=" ")