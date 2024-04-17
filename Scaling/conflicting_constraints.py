import gurobipy as gp
from gurobipy import GRB

# Create a Gurobi model
model = gp.Model("InfeasibleExample1")

# Add variables x and y
x = model.addVar(name="x")
y = model.addVar(name="y")

# Add conflicting constraints
model.addConstr(x + y == 5, name="constraint1") 
model.addConstr(x + y == 10, name="constraint2") 

# Set objective (irrelevant for infeasibility demonstration) 
model.setObjective(x + y, GRB.MINIMIZE) 

# Attempt to solve the model
model.optimize()

# print(model.status)  # This will output GRB.INFEASIBLE