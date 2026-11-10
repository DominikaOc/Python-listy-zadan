import matplotlib.pyplot as plt

class Triangle:

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3


    def distance(self, x1, y1, x2, y2):
        return ((x1 - x2)**2 + (y1 - y2)**2)**0.5


    # Obwód
    def circumference(self):
        a = self.distance(self.x1, self.y1, self.x2, self.y2)
        b = self.distance(self.x2, self.y2, self.x3, self.y3)
        c = self.distance(self.x3, self.y3, self.x1, self.y1)

        return a+b+c


    # Pole
    def area(self):
        # korzystamy ze wzoru Herona
        p = 0.5*(self.circumference())
        a = self.distance(self.x1, self.y1, self.x2, self.y2)
        b = self.distance(self.x2, self.y2, self.x3, self.y3)
        c = self.distance(self.x3, self.y3, self.x1, self.y1)

        return (p*(p-a)*(p-b)*(p-c))**0.5


    # Czy punkt (x,y) zawiera się w trójkącie?
    # inny sposób:
    # dla trójkątów dodatnio zorientowanych: det(x - p1, p2-p1) , det(x - p2, p3-p2), det(x-p3, p1-p3)
    # gdy wszystkie det są dodatnie, to x jest w trójkącie
    def contains_point(self, x, y):
        pole = self.area()

        t1 = Triangle(x, y, self.x1, self.y1, self.x2, self.y2)
        t2 = Triangle(x, y, self.x2, self.y2, self.x3, self.y3)
        t3 = Triangle(x, y, self.x3, self.y3, self.x1, self.y1)

        pole2 = t1.area() + t2.area() + t3.area()

        return abs(pole - pole2) < 10**(-8)



    def contains(self, other_triangle):
        # Czy other_triangle zawiera się w self?
        # Tak, jeśli wierzchołki other_triangle zawierają się w self

        return( self.contains_point(other_triangle.x1, other_triangle.y1)
            and self.contains_point(other_triangle.x2, other_triangle.y2)
            and self.contains_point(other_triangle.x3, other_triangle.y3) )


    def contained_in(self, other_triangle):
        # czy self zawiera się w other_triangle?
        return other_triangle.contains(self)



    def draw(self):
        x_wek = [self.x1, self.x2, self.x3, self.x1]
        y_wek = [self.y1, self.y2, self.y3, self.y1]
        plt.plot(x_wek, y_wek)
        plt.show()





t1 = Triangle(0,2,1,10,4,3)
print(t1.area())
print(t1.circumference())
t1.draw()
#print(t1.contains_point(1, 0.5))
t2 = Triangle(0,0, 2, 0, 1, 0.5)
#print(t1.contains(t2))
#print(t1.contained_in(t2))
