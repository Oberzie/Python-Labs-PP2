class Shape:
    def __init__(self):  
        self.length = int(input())  
        self.width = int(input())
    def Rectangle(self):
        print(self.length * self.width)  

area = Shape()
area.Rectangle()