class Shape:
    def __init__(self):  
        self.length = int(input())  
    
    def Square(self):
        print(self.length ** 2)  

area = Shape()
area.Square()