from math import *
from matplotlib.pyplot import *
from numpy import *
import numpy as np
#Question-1
'''plot(10, 25, 'go')
plot(15, 90, 'dr')
plot(-35, 59, marker='^', color='maroon')
plot(125, 24, marker='^', color='magenta')
plot(65, 34, marker='*', color='black')
plot(3, 10, marker='.', color='brown')
xlabel('X-axis')
ylabel('Y-axis')
title('Plotting Points')
show()'''

#Question-2
'''x = [1,2,5,7]
y = [1,8,12,4]
plot(x, y)
xlabel('X Values')
ylabel('Y Values')
title('Graph Of X Verses Y')
show()'''

#Question-3
'''x = linspace(-10, 10)
y = x**3
figure(figsize = (6, 6))
plot(x, y, color='blue')
xlabel('X Values')
ylabel('X^3')
title('graph of plot f(x)')
show()'''

#Question-4
'''x = linspace(-7, 10)
y = 2*x**4+2*x+10
plot(x, y, color='red')
xlabel('X Values')
ylabel('Y Values')
title('Graph of X & Y')
show()'''

#Question-5
'''x = linspace(1, 10)
y = log(3*x**2)
plot(x, y, color='black')
xlabel('X')
ylabel('Y')
title('Graph Of X & Y')
show()'''

#Question-6
'''x = [2, 14]
y = [7, 16]
plot(x, y, color='brown')
xlabel('X')
ylabel('Y')
title('Graph Of X & Y')
show()'''

#Question-7
'''x = linspace(-2*pi, 2*pi, 50)
y = sin(x)
plot(x, y)
xlabel('X')
ylabel('Y')
title('Graph Of X & Y')
show()'''

#Question-8
'''x = linspace(0, pi/2, 1000)
y = cos(x)
plot(x, y)
title('Graph Of X & Y')
x1 = linspace(0, pi/2, 1000)
z = tan(x1)
plot(x1, z)
xlabel('C')
ylabel('D')
title('Graph of X & Z')
show()
show()'''

#Question-9
'''x=linspace(-5,5)
a=x**2
b=x**3
c=exp(x)
y=4*x+5
subplot(2,2,1)
plot(x,a)
subplot(2,2,2)
plot(x,b)
subplot(2,2,3)
plot(x,c)
subplot(2,2,4)
plot(x,y)
xlabel('X')
ylabel('Y')
title('Graph Of X and Y')
legend()
show()'''

#Question-10

