class Vector3:

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def isCloserThan(self, z):
        return self.z < z

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f'Vector3: (x={self.x}, y={self.y}, z={self.z})'
