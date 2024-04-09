from pulp import *
#Question-1
'''Z = LpProblem('LPP', LpMaximize)
X = LpVariable('X', 0, None, cat=LpInteger)
Y = LpVariable('Y', 0, None, cat=LpInteger)
Z += 150*X+75*Y
Z += 4*X+6*Y<=24
Z += 5*X+3*Y<=15
print(Z)
Z.solve()
print("Status:-", LpStatus[Z.status])'''

#Question-2
'''Z = LpProblem('LPP', LpMinimize)
X = LpVariable('X', 0, None, cat=LpInteger)
Y = LpVariable('Y', 0, None, cat=LpInteger)
Z += 3-5*X+2*Y
Z += X+Y>=5
Z += X>=5
Z += Y<=2
print(Z)
Z.solve()
print("Status", LpStatus[Z.status])'''

#Question-3
'''Z = LpProblem('LPP', LpMaximize)
X = LpVariable('X', 0, None, cat=LpInteger)
Y = LpVariable('Y', 0, None, cat=LpInteger)
Z += 2*X+3*Y
Z += -3*X+Y<=4
Z += X-Y<=2
print(Z)
Z.solve()
print("Status", LpStatus[Z.status])'''

#Question-4
'''Z=LpProblem('LPP', LpMinimize)
X=LpVariable('X', 0, None, cat=LpInteger)
Y = LpVariable('Y', 0, None, cat=LpInteger)
Z += X+Y
Z += X>=6
Z += Y>=6
Z += X+Y<=11
print(Z)
Z.solve()
print("Status", LpStatus[Z.status])'''

#Question-5
'''Z=LpProblem('LPP', LpMaximize)
X1=LpVariable('X1', 0, None, cat=LpInteger)
X2 = LpVariable('X2', 0, None, cat=LpInteger)
X3 = LpVariable('X3', 0, None, cat=LpInteger)
Z += 3*X1+5*X2+4*X3
Z += 2*X1+3*X2<=8
Z += 2*X2+5*X3<=10
Z += 3*X1+2*X2+4*X3<=15
print(Z)
Z.solve()
print("Status", LpStatus[Z.status])'''
