import gurobipy as gp # updated the requirements #update this to be in the github #also look into the paper.
from gurobipy import GRB

# Define the problem parameters
num_cores = 4
num_flow_classes = 4
flow_sizes = [128, 256, 512, 1024]  # in bytes
max_core_load = 1024 * 1024  # Maximum load a core can handle (1 MB)  #The load on a core is calculated by summing up the sizes of all the flows assigned to that core. 
max_core_traffic = 1000  # Maximum traffic a core can handle (1000 flows)
throughput_threshold = 500  # Safety threshold for throughput (500 flows)

# !TODO: Define the weights for the weighted average throughput weighted_throughput_avg = (∑ wixi) / (∑wi)


# Define the old configuration (n_old) #  how the flows are assigned to the different cores before the optimization process.
n_old = [
    [100, 50, 20, 10],  # Core 0 AN ASIDE: tries to find a new, optimized configuration that satisfies all the constraints while minimizing the required changes from the initial state.
    [80, 60, 30, 15],   # Core 1
    [70, 40, 25, 20],   # Core 2
    [90, 55, 15, 5]     # Core 3
]

# Create a new model
model = gp.Model("Flow Allocation")

# Define decision variables
# n[i, j] represents the number of flows of class j assigned to core i
n = model.addVars(num_cores, num_flow_classes, vtype=GRB.INTEGER, name="n") # flow sizes

# Define the objective function (minimize the cost)
cost = 0
for i in range(num_cores):
    for j in range(num_flow_classes):
        cost += abs(n[i, j] - n_old[i][j]) # fix this for linear expression
model.setObjective(cost, GRB.MINIMIZE)

# Add constraints
# Constraint 1: Maximum load constraint
for i in range(num_cores):
    load = 0
    for j in range(num_flow_classes):
        load += n[i, j] * flow_sizes[j]
    model.addConstr(load <= max_core_load, name=f"load_constraint_{i}")

# Constraint 2: Maximum traffic constraint
traffic = 0
for i in range(num_cores):
    for j in range(num_flow_classes):
        traffic += n[i, j] * 2 ** j # to the of n
    model.addConstr(traffic <= max_core_traffic, name=f"traffic_constraint_{i}")

# Constraint 3: Safety throughput constraint for each core


# # !TODO: Constraint 4: Safety weighted average throughput constraint


# # !TODO: Constraint 5: Reactivity constraint
# (Assuming a maximum change of 10 flows per step)

#configuration for n number of steps, 


# Solve the model
model.optimize()

# model needed to be updated in the form of x+y = c

# Print the optimal solution
if model.status == GRB.OPTIMAL:
    print("Optimal solution found:")
    for i in range(num_cores):
        for j in range(num_flow_classes):
            print(f"n[{i}, {j}] = {int(n[i, j].x)}")
else:
    print("No optimal solution found")


