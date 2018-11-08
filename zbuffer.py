from color import Color
from vector import Vector3
from pprint import pprint
import json

WIDTH = 5                     # for testing purposes
HEIGHT = 5

DEFAULT_COLOR = Color()         # default is black (0, 0, 0)
DEFAULT_DEPTH = float('Inf')

def load_polygons():
    with open("polygons.json", "r") as file:
        data = json.load(file)

    return data['polygons']

screen = [[(DEFAULT_COLOR, DEFAULT_DEPTH, f'x={row}, y={column}')
           for column in range(WIDTH)]
           for row in range(HEIGHT)]

def print_screen():
    print('current screen:')
    pprint(screen)
    print('-------------------------------------------')

polygons = load_polygons()
print_screen()

for polygon in polygons:
    for pixel in polygon['pixels']:
        position = Vector3(*pixel['position'])
        print(position)
        print(screen[position.x])
        if position.isCloserThan(screen[position.x][position.y][1]):
            screen[position.x][position.y] = (Color(*pixel['color']), 
                                              position.z, 
                                              screen[position.x][position.y][2])

print_screen()
