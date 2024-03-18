import gurobipy as gp

# Data (Adjust this!)
tasks = ['T1', 'T2']
agents = ['A1', 'A2']
performance = {('T1', 'A1'): 10, ('T2', 'A1'): 15, ('T1', 'A2'): 12, ('T2', 'A2'): 8}


# Model
model = gp.Model('2-RAP')

# Adding Decision Variables
assign = model.addVars(tasks, agents, vtype=gp.GRB.BINARY, name='assign')

# Objective (Minimize Cost)
model.setObjective(gp.quicksum(performance[i, j] * assign[i, j] for i in tasks for j in agents), gp.GRB.MAXIMIZE)

# Task Assignment Constraints
model.addConstrs(gp.quicksum(assign[i, j] for j in agents) == 1 for i in tasks)


# Solve
model.optimize()

# Print Solution (if found)
if model.status == gp.GRB.Status.OPTIMAL:
    print('Total Cost:', model.objVal)
    for i in tasks:
        for j in agents:
            if assign[i, j].x > 0.5:
                print(f'Task {i} assigned to Agent {j}')
else:
    print('No feasible solution found.')