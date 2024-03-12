from gurobipy import Model, GRB

# Model Setup
num_functions = 5
capacity = 100 

function_latency = {1: 20, 2: 30, 3: 15, 4: 40, 5: 25}
resource_usage = {1: 30, 2: 20, 3: 15, 4: 45, 5: 25}

# Linear Approximation for Latency (Less Complexity)
def latency_cost(usage):
    cost_per_unit = 0.2  # A single slope for the cost
    return cost_per_unit * usage

# Gurobi Model Creation
model = Model("Network Function Placement")

x = {}  # Regular decision variables for function placement
for i in range(1, num_functions + 1):
    x[i] = model.addVar(vtype=GRB.BINARY, name=f"x_{i}")

# Simplified Objective: Minimize total latency cost 
model.setObjective(sum(x[i] * function_latency[i] for i in range(1, num_functions + 1)), GRB.MINIMIZE)

# Capacity Constraint 
model.addConstr(sum(x[i] * resource_usage[i] for i in range(1, num_functions + 1)) <= capacity, name="capacity_constraint")

# Solve and Print Results 
model.optimize()

