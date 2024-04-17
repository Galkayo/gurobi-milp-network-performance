from gurobipy import Model, GRB

# Create a model object
m = Model("complex_model")

# Add integer decision variables (tighter bounds)
x = m.addVar(lb=1, ub=24, vtype=GRB.INTEGER, name="x")
y = m.addVar(lb=1, ub=15, vtype=GRB.INTEGER, name="y")
z = m.addVar(lb=1, ub=14, vtype=GRB.INTEGER, name="z")

# Set the objective function (linear)
m.setObjective(30*x + 20*y + 40*z, GRB.MINIMIZE)

# linear constraints with larger coefficients and tighter bounds
m.addConstr(20*x + 25*y + 30*z <= 100, "const1")  # Relaxed const1
m.addConstr(18*x - 12*y + 9*z >= 10, "const2")  # Relaxed const2
m.addConstr(8*x + 10*y - 5*z <= 50, "const3")  # Relaxed const3
# m.addConstr(5*x - 3*y + 6*z >= 5, "const4")  # Relaxed const4
m.addConstr(12*x + 6*y + 12*z <= 60, "const5")  # Relaxed const5
m.addConstr(7*x + 5*y + 8*z >= 15, "const6")  # Relaxed const6
m.addConstr(4*x + 3*y + 6*z <= 40, "const7")  # Relaxed const7
m.addConstr(11*x + 13*y + 17*z <= 80, "const8")  # Relaxed const8
m.addConstr(9*x - 7*y + 5*z >= 10, "const9")  # Relaxed const9
m.addConstr(6*x + 8*y - 4*z <= 40, "const10")  # Relaxed const10

# Update the model (optional)
m.update()

# Solve the optimization problem
m.optimize()

# Print the solution status
status = m.status
print("Optimization status:", status)

# Print the optimal values of the variables
if status == GRB.OPTIMAL:
    print("x =", x.x)
    print("y =", y.x)
    print("z =", z.x)
    print("Objective value:", m.objVal)
    print('The optimization took {} seconds.'.format(m.Runtime))
else:
    print("The optimization problem was not solved successfully.")
