** start of main.py **

class Rectangle:
    def __init__(self, width, height):
        self.set_width(width)
        self.set_height(height)

    def __str__(self):
        arg_list = [f'{key}={val}' for key, val in vars(self).items()]
        args = ', '.join(arg_list)
        return f'{self.__class__.__name__}({args})'

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return sum([2 * self.width, 2 * self.height])
    
    def get_diagonal(self):
        return sum([self.width ** 2, self.height ** 2]) ** 0.5
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        
        width_string = self.width * '*' + '\n'
        output_string = width_string * self.height
        return output_string

    def get_amount_inside(self, other):
        if not isinstance(other, (Square, Rectangle)):
            raise TypeError('Argument must be a Square or Rectangle')
        if type(other) == Square:
            return (self.width // other.width) * 2
        return self.width // other.width
        

class Square(Rectangle):
    def __init__(self, side):
        self.set_side(side)

    def __str__(self):
        arg_list = [f'{key}={val}' for key, val in vars(self).items() if key == 'side']
        args = ', '.join(arg_list)
        return f'{self.__class__.__name__}({args})'
    
    def set_side(self, side):
        self.side = side
        self.set_width(side)
        self.set_height(side)

    def set_width(self, side):
        self.side = side
        self.width = side
        self.height = side

    def set_height(self, side):
        self.side = side
        self.width = side
        self.height = side

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())
# sq.set_width(5)
# print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))

** end of main.py **

