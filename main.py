class line:
    def __init__(self, X1, Y1, X2, Y2):
        self.x1 = X1
        self.y1 = Y1
        self.x2 = X2
        self.y2 = Y2

    def setX1(self, X1):
        self.x1 = X1

    def setY1(self, Y1):
        self.y1 = Y1

    def setX2(self, X2):
        self.x2 = X2

    def setY2(self, Y2):
        self.y2 = Y2

    def getX1(self):
        return self.x1

    def getY1(self):
        return self.y1

    def getX2(self):
        return self.x2

    def getY2(self):
        return self.y1

    def xCross(self):
        if not self.x2 == self.x1:
            m = (self.y2 - self.y1) / (self.x2 - self.x1)
            if not m == 0:
                return self.x1 - self.y1 / m
            else:
                # horizontal line = no intersection
                raise ValueError("Error, slope can't be zero i.e. no intersection with X-axis")
        else:
            #  if x1=x2 then it is a vertical line
            return self.x1

    def yCross(self):
        if not self.x2 == self.x1:
            m = (self.y2 - self.y1) / (self.x2 - self.x1)
            y = self.y1 - m * self.x1
        else:
            # vertical line so no intersection
            raise ValueError("Error, x1 and x2 can't be the same value i.e. no intersection with Y-axis")


class point(line):
    def __int__(self, X1, Y1):
        super().__init__(X1, Y1, X1, Y1)

    def xCross(self):
        pass

    def yCross(self):
        pass


def askLine():
    lines = []
    while True:
        try:
            x1 = float(input("x1: "))
            y1 = float(input("y1: "))
            x2 = float(input("x2: "))
            y2 = float(input("y2: "))
            theLine = line(x1, y1, x2, y2)
            lines.append(theLine)
        except:
            return lines


def checkLines(lines, x, y):
    for line in lines:
        if line.xCross() == x or line.yCross() == y:
            return True
    return False


def makeLine(point1, point2):
    return line(point1.getX1(), point1.getY1(), point2.getX2(), point2.getY2())
