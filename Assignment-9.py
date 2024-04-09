from pulp import *
#Question-1

'''origin=["A","B","C"]
supply={"A":7,"B":9,"C":10}
ware=["d1","d2","d3","d4"]
demand={"d1":5,"d2":8,"d3":7,"d4":14}
costs=[[19,30,50,10],[70,30,40,60],[40,80,70,20]]
costs=makeDict([origin,ware],costs,0)
pro=LpProblem("Problem",LpMinimize)
route=[(w,b) for w in origin for b in ware]
vari=LpVariable.dicts("route:",(origin,ware),0,None)
pro+=(lpSum([vari[w][b]*costs[w][b] for (w,b) in route]))
for w in origin:
    pro+=(lpSum([vari [w][b] for b in ware])<=supply[w])

for b in ware:
    pro+=(lpSum([vari [w][b] for w in origin])>=demand[b])
pro.solve()
for v in pro.variables():
    print(v.name,"=", v.varValue)
print("objective:", value(pro.objective))'''

#Question-2
'''origin=["A","B","C"]
supply={"A":17,"B":12,"C":16}
ware=["d1","d2","d3"]
demand={"d1":14,"d2":8,"d3":23}
costs=[[13,15,16],[7,11,12],[19,20,9]]
costs=makeDict([origin,ware],costs,0)
pro=LpProblem("Problem",LpMinimize)
route=[(w,b) for w in origin for b in ware]
vari=LpVariable.dicts("route:",(origin,ware),0,None)
pro+=(lpSum([vari[w][b]*costs[w][b] for (w,b) in route]))
for w in origin:
    pro+=(lpSum([vari [w][b] for b in ware])<=supply[w])

for b in ware:
    pro+=(lpSum([vari [w][b] for w in origin])>=demand[b])
pro.solve()
for v in pro.variables():
    print(v.name,"=", v.varValue)
print("objective:", value(pro.objective))'''

#Question-3
origin=["A","B","C"]
supply={"A":12,"B":14,"C":4}
ware=["d1","d2","d3"]
demand={"d1":5,"d2":8,"d3":7}
costs=[[5,1,8],[2,4,0],[3,6,7]]
costs=makeDict([origin,ware],costs,0)
pro=LpProblem("Problem",LpMinimize)
route=[(w,b) for w in origin for b in ware]
vari=LpVariable.dicts("route:",(origin,ware),0,None)
pro+=(lpSum([vari[w][b]*costs[w][b] for (w,b) in route]))
for w in origin:
    pro+=(lpSum([vari [w][b] for b in ware])<=supply[w])

for b in ware:
    pro+=(lpSum([vari [w][b] for w in origin])>=demand[b])
pro.solve()
for v in pro.variables():
    print(v.name,"=", v.varValue)
print("objective:", value(pro.objective))
