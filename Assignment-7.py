from sympy import *
#import numpy as np
#Question-
'''P=Point(6,-3)
L=Line(Point(0,0), Point(10,0))
print(P.reflect(L))
print(P.rotate(pi))
print(P.scale(x=2, y=4))
m=Matrix([[1,2,0],[3,1,0],[0,0,1]])
print(P.transform(m))'''

#Question-2
'''A,B,C=Point(2,2),Point(4,2),Point(3,6)
t=Triangle(Point(2,2),Point(4,2),Point(3,6))
print(t.translate(x=2))
print(t.scale(x=4, y=5))
m=Matrix([[1,-3,0],[0,1,0],[0,0,1]])
A1=A.transform(m)
B1=B.transform(m)
C1=C.transform(m)
T1=Triangle(A1,B1,C1)
print(T1)'''

#Question-3
'''t=Triangle(Point(2,2),Point(4,2), Point(3,6))
print(t.scale(5,5))
L=Line(Point(0,0), Point(10,0))
print(t.reflect(L))
print(t.rotate(pi))
print(t.rotate(pi/3, Point(6,6)))'''

#Question-4
'''S=Segment(Point(2,3), Point(4,-1))
print(S.rotate(pi/2))'''

#Question-5
'''X,Y=symbols('x,y')
L=Line(X-2*Y+4)
P=Point(3,6)
print(P.reflect(L))'''

#Question-6
'''x,y = symbols('x,y')
L = Line(3*x-2*y+4)
A,B = Point(5, -3), Point(1, 4)
S = Segment(A,B)
a = A.reflect(L)
b = B.reflect(L)
S1 = Segment(a,b)
print(S1)'''

#Question-7
'''A,B = Point(-3, 5), Point(3, 5)
S = Segment(A,B)
T = Matrix([[1,3,0], [4,1,0], [0,0,1]])
A1 = A.transform(T)
B1 = B.transform(T)
S1 = Segment(A1, B1)
print(S1.slope)
print(S1.midpoint)'''

#Question-8
'''P1,P2,P3,P4,P5 = Point(1,2), Point(3,5), Point(5,4), Point(4,2), Point(3,0)
P = Polygon(P1,P2,P3,P4,P5)
print(P.rotate(pi/3, Point(1,3)))'''

#Question-9
'''A,B = Point(4,-1), Point(5,0)
S = Segment(A,B)
T1 = Matrix([[1,0,0],[0,9,0],[0,0,1]])
A1 = A.transform(T1)
B1 = B.transform(T1)
S1 = Segment(A1,B1)
S1 = S1.rotate(pi)
S1 = S1.scale(x=2)
x,y = symbols('x,y')
L = Line(y-x)
S1 = S1.reflect(L)
print(S1)'''

#Question-10
'''A,B = Point(3,-2), Point(5,0)
L = Segment(A,B)
L1 = L.rotate(pi/4)
m = Matrix([[1,3.5,0], [0,1,0], [0,0,1]])
a1,b1 = Point(5*sqrt(2)/2, sqrt(2)/2), Point(5*sqrt(2)/2, 5*sqrt(2)/2)
a2 = a1.transform(m)
b2 = b1.transform(m)
S1 = Segment(a2, b2)
S1 = S1.scale(y=2)
x,y = symbols('x,y')
d = Line(y+x)
S1.reflect(d)
print(S1)'''

#Question-11
'''x,y = symbols('x,y')
T = Matrix([[1,2], [3,2]])
A = Matrix([2,4])
B = Matrix([3,-1])
t1 = T*A
t2 = T*B
slope = (t2[1]-t1[1])/(t2[0]-t1[0])
I = t1[1] - slope * t1[0]
print(slope*x+I)'''

#Question-12
'''x,y = symbols('x,y')
eqn = Eq(2*x+y, 3)
x1 = -4
y1 = 3
se = eqn.subs({x:x+x1*y, y:y+y1*x})
tl = solve(se, y)
print(tl)'''

#Question-13
'''point = np.array([1,0,0])
angle = np.radians(90)
rm = np.array([[np.cos(angle), -np.sin(angle), 0], [np.sin(angle), np.cos(angle), 0], [0,0,1]])
rp = np.dot(rm, point)
print(point)
print(rp)'''

#Question-14
'''point = np.array([1,2,3])
angle = np.radians(180)
rm = np.array([[np.cos(angle), 0, np.sin(angle)], [0,1,0], [-np.sin(angle), 0, np.cos(angle)]])
rp = np.dot(rm, point)
print(point)
print(rp)'''

#Question-15
A,B = Point(5,-2), Point(3,2)
L = Segment(A,B)
L1 = L.rotate(pi/4)
m = Matrix([[1,5,0], [0,1,0], [0,0,1]])
a1,b1 = Point(5*sqrt(2)/2, sqrt(2)/2), Point(5*sqrt(2)/2, 5*sqrt(2)/2)
a2 = a1.transform(m)
b2 = b1.transform(m)
S1 = Segment(a2, b2)
S1 = S1.scale(y=4)
x,y = symbols('x,y')
d = Line(y-x)
S1.reflect(d)
print(S1)
