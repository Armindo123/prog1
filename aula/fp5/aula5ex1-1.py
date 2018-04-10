#criar cubo


class Point():
    def __init__ (self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__ (self):
        return "Point: ({}x{}x{})".format(self.x, self.y, self.z)




class Cubo():
    def __init__(self, point, size):
        self.point = point
        self.size = size
        self.p2 = (point.x, point.y, point.z + size)
        self.p3 = (point.x, point.y + size, point.z)
        self.p4 = (point.x + size, point.y + size, point.z + size)
        self.p5 = (point.x + size, point.y, point.z + size)
        self.p6 = (point.x, point.y, point.z + size)
        self.p7 = (point.x + size, point.y + size, point.z)
        self.p8 = (point.x + size, point.y, point.z)

                
    def __str__(self):
        return "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n size {}".format(self.point, self.p2, self.p3, self.p4, self.p5, self.p6, self.p7, self.p8, self.size)




size = 5
p1 = Point(0, 0, 0)
#p2 = (a, b, c + size)
#p3 = (a, b + size, c + size)
#p4 = (a + size, b + size, c + size)
#p5 = (a + size, b, c + size)
#p6 = (a, b + size, c)
#p7 = (a + size, b + size, c)
#p8 = (a + size, b, c)

cubo = Cubo(p1, size)

print(cubo)