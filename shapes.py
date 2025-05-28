class Shape:

    x = 0
    y = 0
    colour = ""

    def getArea(self):
        """Calculate the area of the shape 
        and return the value."""
        pass

    def getPerimeter(self):
        """Calculate the perimeter of the shape 
        and return the value."""
        pass

    def draw(self):
        """Draw the shape using the position, 
        size and colour."""
        pass

class Square(Shape):

    def __init__(self, x, y, length, colour):
        self.x = x
        self.y = y
        self.length = length
        self.colour = colour

    def getArea(self):
        return self.length * self.length
    
    def getPerimeter(self):
        return self.length * 4
    
    def draw(self):
        for i in range(self.length):
            print ("* " * self.length)