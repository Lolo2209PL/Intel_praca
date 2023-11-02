from dataclasses import dataclass


@dataclass
class Rectangle:
    # TODO: Propose data format to hold rectangle information
    
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def contains(self, other: "Rectangle") -> bool:
        # TODO: Implement
        
        return (self.x <= other.x and
                self.y <= other.y and
                self.x + self.width >= other.x + other.width and
                self.y + self.height >= other.y + other.height)

    def intersect(self, other: "Rectangle") -> bool:
        # TODO: Implement
        
        return (self.x < other.x + other.width and
                self.x + self.width > other.x and
                self.y < other.y + other.height and
                self.y + self.height > other.y)
