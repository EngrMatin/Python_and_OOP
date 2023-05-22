class Distance:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def calcDistance(self):
        return ((self.point2[0]-self.point1[0])**2 + (self.point2[1]-self.point1[1])**2)**0.5

point1 = [2, 4]
point2 = [5, 8]
distObj = Distance(point1, point2)
distance = distObj.calcDistance()
print(distance)