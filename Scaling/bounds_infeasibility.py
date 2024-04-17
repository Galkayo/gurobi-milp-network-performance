import gurobipy as gp
from gurobipy import GRB

model = gp.Model("InfeasibleExample2")

x = model.addVar(lb=2, ub=4, name="x")  # x constrained to be between 2 and 4
y = model.addVar(lb=6, ub=8, name="y")  # y constrained to be between 6 and 8

model.addConstr(x + y == 7, name="constraint")

model.setObjective(x + 2*y, GRB.MAXIMIZE)  # Any objective will do

model.optimize()

print(model.status)  # This will also output GRB.INFEASIBLE