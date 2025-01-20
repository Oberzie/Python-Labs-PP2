class Sentence:
    def __init__(self): # we use the __init__() function to assign values to object properties
        self.str = "" # later we can store in this place input
    
    def getString(self):
        self.str = input("Enter a string: ")
    
    def printString(self):
        print(self.str.upper())

sentence = Sentence()  # Создаём объект класса Sentence
sentence.getString()   
sentence.printString() 