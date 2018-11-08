from color import Color
from vector import Vector3
from zbuffer import zbuffer
from warnock import warnock
from pprint import pprint
import json
import sys

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

def render(renderFunction, polygons, screen):
    return renderFunction(polygons, screen)

screen = render(zbuffer if sys.argv[1].lower() == 'zbuffer' else warnock,
                polygons,
                screen)

print_screen()
