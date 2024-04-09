from sympy import *
#Question-1
'''A = Point(4,4)
B = Point(6,7)
C = Point(4,2)
x = [A.x,B.x,C.x,A.x]
y = [A.y,B.y,C.y,A.y]
M = Matrix([[cos(-pi), sin(-pi), 0], [-sin(-pi), cos(-pi), 0], [0,0,1]])
A1 = A.transform(M)
B1 = B.transform(M)
C1 = C.transform(M)

from matplotlib.pyplot import *
P = [10,-10]
Q = [0,0]
plot(P,Q,label='x-axis',color='k')
plot(Q,P,label='y-axis',color='k')
plot(x,y,"r")
x1 = [A1.x, B1.x, C1.x, A1.x]
y1 = [A1.y, B1.y, C1.y, A1.y]
plot(x1,y1)
legend()
show()'''

#Question-2
'''T = Triangle(Point(2,0), Point(2,-1), Point(-1,3))
A,B,C = Point(2,0), Point(2,-1), Point(-1,3)
M = Matrix([[-1,0,0],[0,1,0],[6,0,1]])
A1 = A.transform(M)
B1 = B.transform(M)
C1 = C.transform(M)
T1 = Triangle(A1,B1,C1)
V = T1.vertices
print(V)
x = [2,2,-1,2]
y = [0,-1,3,0]
from matplotlib.pyplot import *
plot(x,y)
X1 = [V[0][0],V[1][0],V[2][0],V[0][0]]
Y1 = [V[0][1],V[1][1],V[2][0],V[0][1]]
plot(X1,Y1,'r')
show()'''

#Question-3
'''R = Polygon(Point(1,1),Point(1,4),Point(5,4),Point(5,1))
T = R.scale(3,3)
V = T.vertices
print(V)
X = [1,1,5,5,1]
Y = [1,4,4,1,1]
from matplotlib.pyplot import *
plot(X,Y,'b')
X1 = [V[0].x,V[1].x,V[2].x,V[3].x,V[0].x]
Y1 = [V[0].y,V[1].y,V[2].y,V[3].y,V[0].y]
plot(X1,Y1,'r')
show()'''

#Question-4
'''R = Polygon(Point(0,0),Point(3,0),Point(4,3),Point(3,1))
T = R.rotate(pi/2)
V = T.vertices
print(V)
X = [0,3,4,3,0]
Y = [0,0,3,1,0]
from matplotlib.pyplot import *
plot(X,Y,'b')
X1 = [V[0][0],V[1][0],V[2][0],V[3][0],V[0][0]]
Y1 = [V[0][1],V[1][1],V[2][1],V[3][1],V[0][1]]
plot(X1,Y1,'r')
legend()
show()'''

#Question-5
'''R = Polygon(Point(3,3),Point(4,5),Point(3,5),Point(2,2))
T = R.translate(2,5)
V = T.vertices
print(V)
x = [3,4,3,2,3]
y = [3,5,5,2,3]
from matplotlib.pyplot import *
plot(x,y,'b')
X1 = [V[0][0],V[1][0],V[2][0],V[3][0],V[0][0]]
Y1 = [V[0][1],V[1][1],V[2][1],V[3][1],V[0][1]]
plot(X1,Y1,'r')
show()'''

#Question-6
'''R = Polygon(Point(2,0),Point(2,5),Point(4,5),Point(4,0))
T = R.rotate(pi/2, Point(0,0))
V = T.vertices
print(V)
X = [2,2,4,4,2]
Y = [0,5,5,0,0]
from matplotlib.pyplot import *
X1 = [V[0][0],V[1][0],V[2][0],V[3][0],V[0][0]]
Y1 = [V[0][1],V[1][1],V[2][1],V[3][1],V[0][1]]
plot(X1,Y1,'r')
show()'''

#Question-7
'''R = Polygon(Point(1,3),Point(4,5),Point(5,4),Point(4,3),Point(2,2))
T = R.translate(3,1)
V = T.vertices
print(V)
X = [1,4,5,4,2,1]
Y = [3,5,4,3,2,3]
from matplotlib.pyplot import *
plot(X,Y,'b')
X1 = [V[0][0],V[1][0],V[2][0],V[3][0],V[4][0],V[0][0]]
Y1 = [V[0][1],V[1][1],V[2][1],V[3][1],V[4][1],V[0][1]]
plot(X1,Y1,'r')
show()'''

#Question-8
'''P = Polygon(Point(4,4),Point(4,2),Point(2,2),Point(2,4))
R = P.scale(3,3)
V = R.vertices
print(V)
from matplotlib.pyplot import *
X1 = [4,4,2,2,4]
Y1 = [4,2,2,4,4]
plot(3,3,'black')
X2 = [V[0][0],V[1][0],V[2][0],V[3][0],V[0][0]]
Y2 = [V[0][1],V[1][1],V[2][1],V[3][1],V[0][1]]
plot(X2,Y2,color='m')
show()'''

#Question-9
'''T = RegularPolygon(Point(0,0),3,7)
print(T)
V = T.vertices
print(V)
X1 = [V[0][0],V[1][0],V[2][0],V[3][0],V[4][0],V[5][0],V[6][0],V[0][0]]
Y1 = [V[0][1],V[1][1],V[2][1],V[3][1],V[4][1],V[5][1],V[6][1],V[0][1]]
from matplotlib.pyplot import *
plot(X1,Y1,'r')
plot(0,0,'g')
show()'''

#Question-10
'''T = RegularPolygon(Point(1,3),1,20)
n = eval(input("Number Of Vertices ==> "))
print(T)
V = T.vertices
print(V)
X1 = []
Y1 = []
for i in range(0,n):
    X1.append(V[i].x)
    Y1.append(V[i].y)
X1.append(X1[0])
Y1.append(Y1[0])
from matplotlib.pyplot import *
plot(X1,Y1,'r')
show()'''
