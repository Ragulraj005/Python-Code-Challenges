def fibonacci(n):
    fib_sequence = [0, 1]  # Initialize with the first two Fibonacci numbers
    while len(fib_sequence) < n:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    return fib_sequence

n = int(input("Enter the number of Fibonacci numbers to generate: "))
if n <= 0:
    print("Please enter a positive integer.")
else:
    result = fibonacci(n)
    print("Fibonacci sequence of the first", n, "numbers:", result)
