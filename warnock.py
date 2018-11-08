from color import Color
from vector import Vector3

DEFAULT_COLOR = Color()         # default is black (0, 0, 0)

def warnock(polygons, screen):
    def get_polygons_that_cover_region(begin, end):
        # TODO: return polygons that cover given region
        return []

    def paint_screen(begin, end, color):
        # TODO: paint screen region with color
        pass

    def check_region(begin, end):
        polygons = get_polygons_that_cover_region(begin, end)
        if len(polygons) == 0:          # no polygon covers region
            paint_screen(begin, end, DEFAULT_COLOR)
        elif len(polygons) == 1:        # 1 polygon in the region
            paint_screen(begin, end, polygons[0])
        else:
            regions = Vector3.subdivide_region(begin, end)
            check_region(*regions[0])
            check_region(*regions[1])
            check_region(*regions[2])
            check_region(*regions[3])


    return screen
