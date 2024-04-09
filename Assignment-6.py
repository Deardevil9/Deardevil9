from scipy.optimize import linprog
#Question-1
'''C = [-5,-3]
A = [[1,1],[2,5]]
B = [7,1]
x0_bnd = (0, None)
x1_bnd = (0, None)
result = linprog(C, A_ub=A, b_ub=B, bounds=(x0_bnd, x1_bnd), method="simplex")
print("Result:-")
print(result)'''

#Question-2
'''C = [-3,-5,-4]
A = [[2,3,0],[2,0,5],[3,2,4]]
B = [8,10,15]
x0_bnd = (0, None)
x1_bnd = (0, None)
x2_bnd = (0, None)
result = linprog(C, A_ub=A, b_ub=B, bounds=(x0_bnd, x1_bnd, x2_bnd), method="simplex")
print("Result:-")
print(result)'''

#Question-3
'''C = [1,2,1]
A = [[1,1/2,1/2],[-3/2,-2,-2]]
B = [1,-8]
x0_bnd = (0, None)
x1_bnd = (0, None)
x2_bnd = (0, None)
result = linprog(C, A_ub=A, b_ub=B, bounds=(x0_bnd, x1_bnd, x2_bnd), method="simplex")
print("Result:-")
print(result)'''

#Question-4
'''C = [-4,-1,-3,-5]
A = [[-4,-6,5,4],[-3,-2,4,1],[-8,-3,3,2]]
B = [20,10,20]
x0_bnd = (0, None)
x1_bnd = (0, None)
x2_bnd = (0, None)
x3_bnd = (0, None)
result = linprog(C, A_ub=A, b_ub=B, bounds=(x0_bnd, x1_bnd, x2_bnd, x3_bnd), method="simplex")
print("Result:-")
print(result)'''

#Question-5
'''C = [4,1]
A = [[-3,-1],[-4,-3],[1,2]]
B = [-3,-6,3]
x0_bnd = (0, None)
x1_bnd = (0, None)
result = linprog(C, A_ub=A, b_ub=B, bounds=(x0_bnd, x1_bnd), method="simplex")
print("Result:-")
print(result)'''
