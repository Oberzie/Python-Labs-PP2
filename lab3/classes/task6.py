def filter(x):
    if x < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if x % i == 0:
            return False
    return True

# List of numbers to filter
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Use filter() with a lambda to filter prime numbers
prime_numbers = list(filter(lambda x: is_prime(x), numbers))

# Output the result
print("Prime numbers in the list are:", prime_numbers)
