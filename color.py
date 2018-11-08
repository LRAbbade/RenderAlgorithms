class Color:
    
    def __init__(self, r=0, g=0, b=0):
        self.r = self._check_value(r)
        self.g = self._check_value(g)
        self.b = self._check_value(b)

    def _check_value(self, val):
        return 0 if val < 0 else 255 if val > 255 else val

    def __eq__(self, c2):
        return self.r == c2.r and self.g == c2.g and self.b == c2.b

    def __add__(self, c2):
        return Color(self.r + c2.r, self.g + c2.g, self.b + c2.b)

    def __neg__(self):
        return Color(255 - self.r, 255 - self.g, 255 - self.b)

    def __sub__(self, c2):
        return Color(self.r - c2.r, self.g - c2.g, self.b - c2.b)

    def __gt__(self, c2):
        return (self.r + self.g + self.b) > (c2.r + c2.g + c2.b)

    def __le__(self, c2):
        return not self.__gt__(c2)

    def __ge__(self, c2):
        return (self.r + self.g + self.b) >= (c2. r + c2.g + c2.b)

    def __lt__(self, c2):
        return not self.__ge__(c2)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f'Color (r={self.r}, g={self.g}, b={self.b})'
