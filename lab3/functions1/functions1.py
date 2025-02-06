import math
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
    numbers = list(map(int, input().split()))
    for i in numbers:
        if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
            print(i)
#5     
def permute(s, l, r):
    if l == r:
        print("".join(s))  
    else:
        for i in range(l, r + 1):
            s[l], s[i] = s[i], s[l]  
            permute(s, l + 1, r)  
            s[l], s[i] = s[i], s[l]  
        string = input("Enter a string: ")

            
#6
def string_reversed():
    arr = list(input("Enter a sentence: ").split())
    arr_reversed = list(reversed(arr))
    for i in arr_reversed:
        print(i)
        
#7
def has_33():
    liston = list(map(int, input().split()))
    for i in range(len(liston) - 1):
        if liston[i] == 3 and liston[i + 1] == 3:
            return True    
    return False

            
#8
def spy_game():
    listop = list(map(int, input().split()))
    code = [0, 0, 7]
    index = 0

    for i in listop:
        if i == code[index]:  
            index += 1  
        if index == len(code):
            return True

    return False 

       
#9
def volume():
    radius =  int(input("radius:"))
    volume = int((4 / 3) * math.pi * pow(radius,3))
    print(volume)
 
#10 
def remove_duplicates():
    unique_list = []
    listik = (list(map(int, input().split())))
    for i in listik:
        if i not in unique_list:
            unique_list.append(i)
    print(unique_list)

#11
def is_palindrome():
    s = input()
    if s == s[::-1]: 
        print("It is a palindrome!")
    else:
        print("Not a palindrome.")
   
#12
def histogram():
    lis = list(map(int, input().split()))
    for i in lis:
        print('*' * i)
#13
import random  
def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    number = random.randint(1, 20)
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    attempts = 0
    while True:
        print("Take a guess.")
        guess = int(input()) 
        attempts += 1

        if guess < number:
            print("\nYour guess is too low.")
        elif guess > number:
            print("\nYour guess is too high.")
        else:
            print(f"\nGood job, {name}! You guessed my number in {attempts} guesses!")
            break

#guess_the_number()
#histogram()  
#is_palindrome()           
#remove_duplicates()      
#volume()
#spy_game()
#has_33()        
#string_reversed()
#permute(list(string), 0, len(string) - 1)
#filter_prime()
#solve(35, 94)
#temperature()
#recipe()










