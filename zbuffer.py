from color import Color
from vector import Vector3

def zbuffer(polygons, screen):
    for polygon in polygons:
        for pixel in polygon['pixels']:
            position = Vector3(*pixel['position'])
            if position.is_closer_than(screen[position.x][position.y][1]):
                screen[position.x][position.y] = (Color(*pixel['color']), 
                                                position.z, 
                                                screen[position.x][position.y][2])

    return screen
