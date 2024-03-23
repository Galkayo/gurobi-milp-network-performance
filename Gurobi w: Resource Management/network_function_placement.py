from gurobipy import Model, GRB # scalling problems, how many constraints, and values, produce the why, less on the specfic, reach a point where its unsolvable, feasibility ,
# how do we know its correct, before adding complexity see it is correct. Verfiy before moving on, write brute force method.
# write simplier problems. 

num_functions = 2
num_nodes = 2 
performance_gain = { (0, 0): 5, (0, 1): 8, (1, 0): 3, (1, 1): 2 } 


m = Model("Simplified_Network_Placement")

# Decision variables (directly named)
func1_node1 = m.addVar(vtype=GRB.BINARY, name="func1_node1")
func1_node2 = m.addVar(vtype=GRB.BINARY, name="func1_node2")
func2_node1 = m.addVar(vtype=GRB.BINARY, name="func2_node1")
func2_node2 = m.addVar(vtype=GRB.BINARY, name="func2_node2")

# Objective: maximize total performance
m.setObjective(5 * func1_node1 + 8 * func1_node2 + 3 * func2_node1 + 2 * func2_node2, GRB.MAXIMIZE)

# Constraints: each function placed on one node
m.addConstr(func1_node1 + func1_node2 == 1, "Func1_placement")
m.addConstr(func2_node1 + func2_node2 == 1, "Func2_placement")

# Different implementation of solved and Printd Results
m.optimize()

if m.status == GRB.OPTIMAL:
    print("Optimal Solution:")
    if func1_node1.x > 0.99:
        print("Function 1 placed on Node 1")
    else:
        print("Function 1 placed on Node 2")

    if func2_node1.x > 0.99:
        print("Function 2 placed on Node 1")
    else:
        print("Function 2 placed on Node 2")

    print(f"Total Performance: {m.objVal:.2f}")
else:
    print("No solution found") 




# Explored 0 nodes (0 simplex iterations) in 0.00 seconds (0.00 work units)
#Explored 0 nodes (0 simplex iterations) in 0.00 seconds (0.00 work units)
# Thread count was 1 (of 8 available processors)

# Solution count 1: 11 

# Optimal solution found (tolerance 1.00e-04)
# Best objective 1.100000000000e+01, best bound 1.100000000000e+01, gap 0.0000%
# Optimal Solution:
# Function 1 placed on Node 2
# Function 2 placed on Node 1
# Total Performance: 11.00
    
