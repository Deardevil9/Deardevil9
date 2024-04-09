from sympy import *
#Question-1
'''b0,b1,b2=Point(5,1),Point(3,4),Point(7,2)
def px(t):
    return((1-t)**2*b0.x+2*t*(1-t)*b1.x+(t**2)*b2.x)
def py(t):
    return((1-t)**2*b0.y+2*t*(1-t)*b1.y+(t**2)*b2.y)
x = []
y = []
i = 0
while i<=1:
    x.append(px(i))
    y.append(py(i))
    i = i+0.01
from matplotlib.pyplot import *
bx = [b0.x,b1.x,b2.x]
by = [b0.y,b1.y,b2.y]
plot(bx,by,"-rd",label="Polygon")
plot(x,y,label="B Curve")
legend()
show()'''


#Question-2
'''b0,b1,b2=Point(1,1),Point(5,5),Point(8,-2)
def px(t):
    return((1-t)**2*b0.x+2*t*(1-t)*b1.x+(t**2)*b2.x)
def py(t):
    return((1-t)**2*b0.y+2*t*(1-t)*b1.y+(t**2)*b2.y)
x = []
y = []
i = 0
while i<=1:
    x.append(px(i))
    y.append(py(i))
    i = i+0.01
from matplotlib.pyplot import *
bx = [b0.x,b1.x,b2.x]
by = [b0.y,b1.y,b2.y]
plot(bx,by,"-rd",label="Polygon")
plot(x,y,label="B Curve")
legend()
show()'''

#Question-3
b0,b1,b2,b3=Point(-1,-1),Point(1,4),Point(6,4),Point(7,0)
def px(t):
    return((1-t)**3*b0.x+3*t*(1-t)**2*b1.x+3*t**2*(1-t)*b2.x+t**3*b3.x)
def py(t):
    return((1-t)**3*b0.y+3*t*(1-t)**2*b1.y+3*t**2*(1-t)*b2.y+t**3*b3.y)
x = []
y = []
i = 0
while i<=2:
    x.append(px(i))
    y.append(py(i))
    i = i+0.01
from matplotlib.pyplot import *
bx = [b0.x,b1.x,b2.x,b3.x]
by = [b0.y,b1.y,b2.y,b3.y]
plot(bx,by,"-rd",label="Polygon")
plot(x,y,label="B Curve")
legend()
show()

