import math
class Pointer:
    def __init__(self):
        self.cord1x = int(input("Enter the first x coordinate: "))
        self.cord1y = int(input("Enter the first y coordinate: "))
        self.cord2x = int(input("Enter the second x coordinate: "))
        self.cord2y = int(input("Enter the second y coordinate: "))
    def show(self):
        print(f"coordinates of the first point is {self.cord1x}:{self.cord1y}")
        print(f"coordinates of the second point is {self.cord2x}:{self.cord2y}")
    def move(self):
        self.newcord1x = int(input("Enter the new first x coordinate: "))
        self.newcord1y = int(input("Enter the new first y coordinate: "))
        self.newcord2x = int(input("Enter the new second x coordinate: "))
        self.newcord2y = int(input("Enter the new second y coordinate: "))
        print("New coordinates of the points: ")
        print(f"first point: {self.newcord1x}:{self.newcord1y}, second point: {self.newcord2x}:{self.newcord2y}")
    def dist(self):
        ds = math.sqrt(pow((self.cord2x - self.cord1x),2) + pow((self.cord2y - self.cord1y),2))
        print(f"distance between the first and second points is {ds}")
        
        
point = Pointer()
print("choose what do you want to know:")
print("1) show coordinates of the points")
print("2) change coordinates of the points")
print("3) find distance between the points")

option = int(input())
if option == 1:
    point.show()
elif option == 2:
    point.move()
else:
    point.dist()
        

    




