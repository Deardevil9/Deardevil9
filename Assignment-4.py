from sympy import*
from matplotlib.pyplot import*

#1
"""
p=Point(1,2)
q=Point(3,8)
print(type(p))
print(type(q))
plot(p.x,p.y,'.r')
plot(q.x,q.y,'*b')
show()"""

#2
#a
"""
a=Point(0,2)
b=Point(5,2)
c=Point(3,0)
print(Point.is_collinear(a,b,c))
x=[0,5]
y=[2,2]
plot(x,y)
x1=[5,3]
y1=[2,0]
plot(x1,y1)
show()

#b
a=Point(5,2)
b=Point(5,-2)
c=Point(5,0)
print(Point.is_collinear(a,b,c))
x=[5,5]
y=[2,-2]
plot(x,y)
x1=[5,5]
y1=[-2,0]
plot(x1,y1)
show()

#3

a=Point(0,7)
b=Point(5,7)
print(a.distance(b))

a2=Point(3,0)
b2=Point(0,-2)
print(a2.distance(b2))

a3=Point(3,2)
b3=Point(5,6)
print(a3.distance(b3))

#4
a,b=Point(2,3),Point(4,1)
l=Line(a,b)
print(type(l))
print(l.slope)
print(l.equation())
print(l.coefficients)
o=Point(0,0)
print(l.distance(o))


#5
s=Segment(Point(1,2),Point(7,2))
print(s.length)
print(s.slope)
print(s.midpoint)
o=Point(5,0)
print(s.distance(o))
x=[1,7]
y=[2,2]
plot(x,y,color='blue')
plot(4,2,'*r')
show()

#6
a,b=Point(1,3),Point(4,0)
l=Line(a,b)
s=Segment(Point(2,1),Point(6,4))
print(l.angle_between(s))
o=Point(1,1)
print(l.distance(o))
print(s.distance(o))


#7
a,b=Point(2,2),Point(5,7)
r=Ray(a,b)
print(r.length)
print(r.slope)
s=Segment(Point(1,2),Point(7,2))
print(r.angle_between(s))


#8
x,y=symbols('x y')
l1=Line(x+y-2)
l2=Line(3*x+2*y-1)
print(l1.intersection(l2))
print(l1.slope)
print(l2.slope)


#9
ax=axes(projection='3d')

a=Point(0,2,0)
b=Point(5,2,0)
c=Point(2,2,2)
d=Point(5,-2,5)
print(Point.are_coplanar(a,b,c,d))
plot(0,2,0,'*r')
plot(5,2,0,'*b')
plot(2,2,2,'*k')
plot(5,-2,5,'*g')
show()"""


#10
l=Point(2,1,3)
m=Point(5,1,4)
n=Point(-2,1,7)
p=Point(1,1,-7)
print(Point.are_coplanar(l,m,n,p))
k=Line(l,m,n)
print(k.equation())
p2=Plane(l,m,n)
print(p2.equation())









