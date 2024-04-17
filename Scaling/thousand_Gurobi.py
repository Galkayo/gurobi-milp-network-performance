from gurobipy import Model, GRB

# Create a model object
m = Model("large_model")

# Add a large number of integer decision variables
variables = [m.addVar(lb=1, ub=1000, vtype=GRB.INTEGER, name=f"x{i}") for i in range(1, 10001)]

# Set the objective function (linear)
m.setObjective(sum(variables), GRB.MINIMIZE)

# Add a large number of linear constraints
for i in range(1, 10001):
    m.addConstr(sum(variables[j] for j in range(i)) >= i, f"const{i}")

# Update the model (optional)
m.update()

# Solve the optimization problem
m.optimize()

# Print the solution status
status = m.status
print("Optimization status:", status)

# Print the optimal values of the variables
if status == GRB.OPTIMAL:
    for var in variables:
        print(f"{var.VarName} =", var.x)
    print("Objective value:", m.objVal)
    print('The optimization took {} seconds.'.format(m.Runtime))
else:
    print("The optimization problem was not solved successfully.")
