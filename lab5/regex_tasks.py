import re
#1
def match():
    text = input()
    pattern = "a*b"
    m1 = re.match(pattern, text)

    if m1:
        print("Matches" )
    else :
        print("Doesn't match")
#2
def match2():
    text = input()
    pattern = "abb"
    m1 = re.match(pattern, text)

    if m1:
        print("Matches" )
    else :
        print("Doesn't match")
#3        
def find_lowercase_sequences():
    text = input()
    print(re.findall(r'\b[a-z]+_[a-z]+\b', text))

#4
def find_upper_lower_sequences():
    text = input()
    print(re.findall(r'\b[A-Z][a-z]+\b', text))

#5    
def match3():
    text = input()
    pattern = "a.*b"
    m1 = re.match(pattern, text)

    if m1:
        print("Matches" )
    else :
        print("Doesn't match")

#6
def replace():
    text = input()
    x = re.sub("[,]", ":", text)
    y = re.sub("[.]", ":", x)
    z = re.sub("[ ]", ":", y)
    print(z)
    
#7
def cases():
    text = input()
    x = re.sub('_([a-z])', lambda x: x.group(1).upper(), text)
    print(x)

#8
def split():
    text = input()
    print(re.split('([A-Z])', text))
    
#9
def space_insert():
    text = input()    
    x = re.sub(r'(?=[A-Z])', " " , text)
    print(x)
    
#10
def camelToSnake():
    text = input()
    x = re.sub(r'(?=[A-Z])', '_', text).lower()  
    print(x)
 
    
#camelToSnake()    
#space_insert()
#split()    
#cases()
#replace()
#match3()
#find_upper_lower_sequences()
#find_lowercase_sequences()           
#match2()        
#match()