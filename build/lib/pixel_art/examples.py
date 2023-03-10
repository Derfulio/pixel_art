#import pixels
import pixel_art.pixels as pixels


# We need to convey the available colors to the user. 
# We want a sample of the color as well as the string needed to invoke it. 
# The colors function does not have any parameters. 
# In an f-string, print each color constant from the pixels module followed by the color’s name in string form. 
# The {pixels.Back.REST} resets the background color so only the pixel is colored. 
# The rest of the output should be in the normal terminal.

def colors():
  print(f"{pixels.BLACK}{pixels.Back.RESET} - 'black'")
  print(f"{pixels.RED}{pixels.Back.RESET} - 'red'")
  print(f"{pixels.GREEN}{pixels.Back.RESET} - 'green'")
  print(f"{pixels.YELLOW}{pixels.Back.RESET} - 'yellow'")
  print(f"{pixels.BLUE}{pixels.Back.RESET} - 'blue'")
  print(f"{pixels.MAGENTA}{pixels.Back.RESET} - 'magenta'")
  print(f"{pixels.CYAN}{pixels.Back.RESET} - 'cyan'")
  print(f"{pixels.WHITE}{pixels.Back.RESET} - 'white'")


def house():
  img = pixels.Image()
  img.add_row(0, 'cyan')
  img.add_row(1, 'cyan', 'yellow', 'cyan', 'red', 'cyan', 'cyan', 'cyan')
  img.add_row(2, 'cyan', 'cyan', 'red', 'red', 'red', 'cyan', 'cyan')
  img.add_row(3, 'cyan', 'red', 'red', 'red', 'red', 'red', 'cyan')
  img.add_row(4, 'cyan', 'white', 'white', 'white', 'white', 'white', 'cyan')
  img.add_row(5, 'cyan', 'white', 'white', 'black', 'white', 'white', 'cyan')
  img.add_row(6, 'green')
  img.display()


def notes():
  img = pixels.Image(16, 14)
  img.add_row(0, 'magenta')
  img.add_row(1, 'magenta', 'magenta', 'magenta', 'magenta',
                 'magenta', 'magenta', 'black', 'black',
                 'black', 'black', 'black', 'black',
                 'black', 'black', 'black', 'magenta')
  img.add_row(2, 'magenta', 'magenta', 'magenta', 'magenta',
                 'magenta', 'black', 'white', 'white',
                 'white', 'white', 'white', 'white',
                 'white', 'white', 'black', 'magenta')
  img.add_row(3, 'magenta', 'magenta', 'magenta', 'magenta',
                 'black', 'white', 'white', 'white',
                 'white', 'white', 'white', 'white',
                 'white', 'white', 'black', 'magenta')
  img.add_row(4, 'magenta', 'magenta', 'magenta', 'magenta',
                 'black', 'white', 'black', 'black',
                 'black', 'black', 'black', 'black',
                 'black', 'white', 'black', 'magenta')
  img.add_row(5, 'magenta', 'magenta', 'magenta', 'magenta',
                 'black', 'white', 'black', 'magenta',
                 'magenta', 'magenta', 'magenta', 'magenta',
                 'black', 'white', 'black', 'magenta')
  img.add_row(6, 'magenta', 'magenta', 'magenta', 'magenta',
                 'black', 'white', 'black', 'magenta',
                 'magenta', 'magenta', 'magenta', 'magenta',
                 'black', 'white', 'black', 'magenta')
  img.add_row(7, 'magenta', 'magenta', 'magenta', 'magenta',
                 'black', 'white', 'black', 'magenta',
                 'magenta', 'magenta', 'magenta', 'magenta',
                 'black', 'white', 'black', 'magenta')
  img.add_row(8, 'magenta', 'magenta', 'black', 'black',
                 'black', 'white', 'black', 'magenta',
                 'magenta', 'magenta', 'black', 'black',
                 'black', 'white', 'black', 'magenta')
  img.add_row(9, 'magenta', 'black', 'white', 'white',
                 'white', 'white', 'black', 'magenta',
                 'magenta', 'black', 'white', 'white',
                 'white', 'white', 'black', 'magenta')
  img.add_row(10, 'magenta', 'black', 'white', 'white',
                  'white', 'white', 'black', 'magenta',
                  'magenta', 'black', 'white', 'white',
                  'white', 'white', 'black', 'magenta')
  img.add_row(11, 'magenta', 'black', 'white', 'white',
                  'white', 'white', 'black', 'magenta',
                  'magenta', 'black', 'white', 'white',
                  'white', 'white', 'black', 'magenta')
  img.add_row(12, 'magenta', 'magenta', 'black', 'black',
                  'black', 'black', 'magenta', 'magenta',
                  'magenta', 'magenta', 'black', 'black',
                  'black', 'black', 'magenta', 'magenta')
  img.add_row(13, 'magenta')
  img.display()

# test your code here
if __name__ == '__main__':
  #colors()
  #house()
  notes()
