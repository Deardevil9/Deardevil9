from matplotlib.pyplot import *
from numpy import *
#Question-1
'''ax=axes(projection='3d')
ax.plot(90,25,55, 'dr')
ax.plot(-50,72,45, '*',color='brown')
ax.plot(70,82,95, '.',color='green')
xlabel("x")
ylabel("y")
ax.set_zlabel("z")
title("3D Plots")
show()'''

#Question-2
'''ax=axes(projection='3d')
z=linspace(10,20,100)
x=cos(2*z)
y=sin(2*z)
plot(x,y,z,'r')
xlabel('x-axes')
ylabel('y-axes')
ax.set_zlabel('z-axes')
title('graph of trigno')
show()'''

#Question-3
'''ax = axes(projection='3d')
x = linspace(1,20,100)
x1 = cos(x)
x2 = (cos(x))**2
plot(x,x1,x2,color='magenta')
xlabel('x')
ylabel('y')
ax.set_zlabel('z')
title('3D Line Graph')
show()'''

#Question-4
'''ax = axes(projection='3d')
x = [0,1,1,0,0]
y = [0,0,1,1,0]
z = [0,0,0,0,0]
ax.plot(x,y,z,color='green')
xlabel('x')
ylabel('y')
ax.set_zlabel('z')
title('3D Cube')
show()'''

#Question-5
'''def f(x,y):
    return(x**2+y**2)
x = linspace(-5,5,100)
y = linspace(-5,10,100)
X,Y = meshgrid(x,y)
Z = f(X,Y)
ax = axes(projection='3d')
ax.contour3D(X,Y,Z,50,cmap='Reds')
xlabel('x')
ylabel('y')
ax.set_zlabel('z')
title('Contour Plot')
show()'''

#Question-6
'''def f(x,y):
    return(x**2+y**2)
x = linspace(-5,5,100)
y = linspace(-5,10,100)
X,Y = meshgrid(x,y)
Z = f(X,Y)
ax = axes(projection='3d')
ax.plot_surface(X,Y,Z, color='magenta')
xlabel('x')
ylabel('y')
ax.set_zlabel('z')
title('Surface Plot')
show()'''

#Question-7
'''def f(x,y):
    return(log(x**2+y**2))
x=linspace(-5,5,100)
y=linspace(-5,5,100)
X,Y = meshgrid(x,y)
Z= f(X,Y)
ax=axes(projection='3d')
ax.plot_wireframe(X,Y,Z, color='orange')
xlabel('x')
ylabel('y')
ax.set_zlabel('z')
title('Wireframe Plot')
show()'''

#Question-8
'''def f(x,y):
    return(log(x**2+y**2))
x = linspace(-5,5,100)
y = linspace(-5,10,100)
X,Y = meshgrid(x,y)
Z = f(X,Y)
ax = axes(projection='3d')
ax.contour3D(X,Y,Z,25, cmap='Reds')
xlabel('x')
ylabel('y')
ax.set_zlabel('z')
title('Contour Plot')
show()'''

#Question-9
'''def f(x,y):
    return(e**-(x**2+y**2))
x=linspace(-2,2,100)
y=linspace(-2,2,100)
X,Y= meshgrid(x,y)
Z=f(X,Y)
ax=axes(projection='3d')
ax.plot_surface(X,Y,Z, color='r')
xlabel('x')
ylabel('y')
ax.set_zlabel('z')
title('Surface Plot')
show()'''

#Question-10
def f(x,y):
    return(e**-(x**2+y**2))
x=linspace(-2,2,100)
y=linspace(-2,2,100)
X,Y= meshgrid(x,y)
Z=f(X,Y)
ax=axes(projection='3d')
ax.plot_wireframe(X,Y,Z, color='green')
xlabel('x')
ylabel('y')
ax.set_zlabel('z')
title('Wireframe Plot')
show()


