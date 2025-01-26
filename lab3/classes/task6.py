def filt(n):
    if n <= 1:  
        return False
    for i in range(2, int(n ** 0.5) + 1):  
        if n % i == 0: 
            return False
    return True  
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
prime_numbers = list(filter(lambda x: filt(x), numbers))
print("Prime numbers in the list are:", prime_numbers)
