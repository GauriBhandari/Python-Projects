class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'

        pic = '*' * self.width + '\n'
        pic = pic * self.height
        return pic

    def get_amount_inside(self, shape):
        return (self.width // shape.width) * (self.height // shape.height)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return f'Square(side={self.width})'

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)

    def get_picture(self):
        if self.width > 50:
            return 'Too big for picture.'

        pic = '*' * self.width + '\n'
        pic = pic * self.width
        return pic

# Create instances of Rectangle and Square
rect = Rectangle(10, 5)
sq = Square(5)

# Test methods of Rectangle
print(rect.get_area())  # Get area of the rectangle
rect.set_height(3)  # Change height of the rectangle
print(rect.get_perimeter())  # Get perimeter of the rectangle
print(rect)  # Print string representation of the rectangle
print(rect.get_picture())  # Print picture representation of the rectangle
print(rect.get_amount_inside(sq))  # Get amount of squares inside the rectangle

# Test methods of Square
sq.set_side(4)  # Change side length of the square
print(sq.get_diagonal())  # Get diagonal of the square
print(sq)  # Print string representation of the square
print(sq.get_picture())  # Print picture representation of the square

# Additional tests
rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))  # Get amount of squares inside the modified rectangle
