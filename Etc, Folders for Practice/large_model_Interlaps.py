from gurobipy import Model, GRB #future note, rewrite to be on, multiple lines.

# Create a model object
m = Model("2D_array_problem")

# Define the 2-D array
array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Add decision variables
variables = [[m.addVar(vtype=GRB.INTEGER, name=f"x{i}_{j}") for j in range(len(array[0]))] for i in range(len(array))]

# Set the objective function (maximize the sum of selected elements)
m.setObjective(sum(array[i][j]*variables[i][j] for i in range(len(array)) for j in range(len(array[0]))), GRB.MAXIMIZE)

# Add constraints (sum of elements in each row should be less than or equal to 10)
for i in range(len(array)):
    m.addConstr(sum(variables[i][j] for j in range(len(array[0]))) <= 20, f"row{i}")

# Add constraints (sum of elements in each column should be less than or equal to 15)
for j in range(len(array[0])):
    m.addConstr(sum(variables[i][j] for i in range(len(array))) <= 25, f"col{j}")

# Solve the optimization problem
m.optimize()

# Print the optimal values of the variables
if m.status == GRB.OPTIMAL:
    print("Optimal solution:")
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(f"x{i}_{j} =", variables[i][j].x)
    print("Objective value:", m.objVal)
else:
    print("The optimization problem was not solved successfully.")
