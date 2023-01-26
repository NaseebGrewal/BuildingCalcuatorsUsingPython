class Rectangle:

  def __init__(self,width, height):
    self.width = width
    self.height = height

  def set_width(self,width):
    self.width = width

  def set_height(self,height):
    self.height = height

  def get_area(self):
    return self.width*self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."

    return ("*"*self.width + '\n')*self.height

  def __repr__(self):
        return f"<Test a:{self.a} b:{self.b}>"

  def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
  
  def get_amount_inside(self, shape):
    shape_area = shape.width*shape.height
    area = self.get_area()
    return area//shape_area

class Square(Rectangle):

  def __init__(self,length):
    self.width = length
    self.height = length

  def set_side(self,side):
    self.width = side
    self.height = side

  def __str__(self):
        return f"Square(side={self.width})"

  
    