class Cylinder:
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
    def volume(self):
        return 3.14 * self.radius**2 * self.height
    def surface_area(self):
        return (2)*(3.14)*(self.radius)*(self.height) + (2)*(3.14)*(self.radius**2)
       
 
myc = Cylinder(2,3)

print(myc.volume())
print(myc.surface_area())


import math
class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        
        return math.sqrt((self.coor2[0] - self.coor1[0])**2  + (self.coor2[1] - self.coor1[1])**2)
    
    def slope(self):
        return (self.coor2[1] - self.coor1[1])/(self.coor2[0] - self.coor1[0])

coordinate1 = (3,2)
coordinate2 = (8,10)
10


myli = Line(coordinate1,coordinate2)

print(myli.distance())

print(myli.slope())
    