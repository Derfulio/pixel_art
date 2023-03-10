from colorama import init, Back, Style

init(autoreset=True)


# test your code here
BLACK = Back.BLACK + '  '
RED = Back.RED + '  '
GREEN = Back.GREEN + '  '
YELLOW = Back.YELLOW + '  '
BLUE = Back.BLUE + '  '
MAGENTA = Back.MAGENTA + '  '
CYAN = Back.CYAN + '  '
WHITE = Back.WHITE + '  '

COLORS_DICT = {
  'black' : BLACK,
  'red' : RED,
  'green' : GREEN,
  'yellow' : YELLOW,
  'blue' : BLUE,
  'magenta' : MAGENTA, 
  'cyan' : CYAN,
  'white' : WHITE
}

class Image():
  """
  The Image class is the main vehicle for creating pixel art. 
  Create a constructor that takes a width and height for the pixel art image. 
  If no arguments are passed, default to 7 and 7. 
  The width and height attributes are assigned their respective parameters. 
  The img attribute takes its value from the init_list method.
  """
  def __init__(self, w=7, h=7):
    self.width = w
    self.height = h
    self.img = self.init_list()

  def init_list(self):
    """
    The pixel art is nothing more than a two-dimensional list. 
    Each element in the list will be a "pixel". 
    Create an empty list. 
    Create a loop that runs as many times as the height attribute. 
    Append an empty list to lst each time the loop runs. 
    Return lst which becomes the initial value for the img attribute.
    """
    lst = []
    for row in range(self.height):
      lst.append([])
    return lst

  def display(self):
    """
    The display() method is going to draw everything to the terminal. 
    Iterate over the img attribute. 
    Take each inner-list (row) and pass it to the display_row() method.
    """
    for row in self.img:
      self.display_row(row)

  def display_row(self, row):
    """
    In Python, if you print a list it will print the square brackets with each element separated by a comma. 
    We want just the pixels. 
    Moreover, we want each pixel in the list to appear next to one another. 
    As you iterate over the list, print the pixel without the newline character (end=''). 
    After the loop runs, print a newline character. 
    This way you are ready for the next row of pixels.
    """
    for pixel in row:
      print(pixel, end='')
    print()

  def convert_color(self, str_clr):
    """
    The convert_color() method takes a string that represents a color and returns the associated Colorama object. 
    If the string is not found in COLORS_DICT then return a black pixel. 
    convert_color() is a helper method for adding pixels to the image.
    """
    return COLORS_DICT.get(str_clr, BLACK)

  def add_row(self, *args):
    """
    The last method in the Image class is add_row(). 
    This method takes an integer as the first parameter. 
    This represents the row of pixels (first row, second row, etc.). 
    After the integer comes an indefinite number of strings. 
    That is why *args is used as the parameter; we don’t know how many parameters there will be. 
    If the width attribute is 7, then there should be eight parameters. 
    The first is the integer designating the row, followed by seven strings for the colors of the pixels.
    """
    if len(args) == 2:
      #If the user wants to add a row of pixels all with the same color, it would not be a good user experience if we made them type the same color again and again. 
      #If there are only two elements in args then the user passed an integer and a string. 
      #Use a comprehension to create a Colorama object with convert_color(). 
      #The comprehension should iterate as many times as the width attribute.
      colors = [self.convert_color(args[1]) for i in range(self.width)]
      self.img[args[0]] = colors

    else:
      #If more than two parameters are passed, separate all of the colors from the integer by slicing args from the first element to the end of the list. 
      #Using a comprehension, transform each color string into its Colorama object with the convert_color() method. 
      #Finally, use the integer (args[0]) to update the row with the list of colors.
      color_params = args[1:]
      colors = [self.convert_color(arg) for arg in color_params]
      self.img[args[0]] = colors


