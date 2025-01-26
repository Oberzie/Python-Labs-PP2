#1
def recipe():
    amount_of_grams = int(input("how much gram do you want: "))
    ounc = amount_of_grams * 28.3495231
    print(f"It will be {ounc} ounces")
    
#2
def temperature():
    F = int(input("What is the temperature today?(in Farenheits): "))
    C = (F - 32) * (5/9)
    print(f"This will be {C}C")

#3
def solve(numheads, numlegs):
    print("We count 35 heads and 94 legs among the chickens and rabbits in a farm.")
    print("How many rabbits and how many chickens do we have?")
    #r + c = 35
    #4r + 2c = 94
    #4r - 2r + 2c - 2c = 94 - 70
    r = int(24 / 2)
    c = int(numheads - r) 
    print(f"Answers are {r} rabbits and {c} chickens")

#4 
def filter_prime():
    numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
    for i in numbers:
        if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
            print(i)
     






#filter_prime()
#solve(35, 94)
#temperature()
#recipe()










