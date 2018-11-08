class Vector3:

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def is_closer_than(self, z):
        return self.z < z

    @staticmethod
    def subdivide_region(begin, end):
        return [
            (Vector3(begin.x, begin.y, begin.z),
             Vector3(end.x // 2, end.y // 2, end.z)),
            (Vector3((begin.x + end.x)//2 + 1, begin.y, begin.z),
             Vector3(end.x, end.y // 2, end.z)),
            (Vector3(begin.x, (begin.y + end.y)//2 + 1, begin.z),
             Vector3(end.x // 2, end.y, end.z)),
            (Vector3((begin.x + end.x)//2 + 1, (begin.y + end.y)//2 + 1, begin.z),
             Vector3(end.x, end.y, end.z))
        ]

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f'Vector3: (x={self.x}, y={self.y}, z={self.z})'
