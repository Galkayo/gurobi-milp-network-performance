import gurobipy as gp
from gurobipy import Model, GRB

# Constants
size = 3  # Size of the Tic-Tac-Toe grid

# Function to generate potential winning lines 
lines = []
for i in range(size):
    for j in range(size):
        for k in range(size):
            if i == 0:
                lines.append(((0, j, k), (1, j, k), (2, j, k)))  # Horizontal lines
            if j == 0:
                lines.append(((i, 0, k), (i, 1, k), (i, 2, k)))  # Vertical lines
            if k == 0:
                lines.append(((i, j, 0), (i, j, 1), (i, j, 2)))  # Depth lines
            if i == 0 and j == 0:
                lines.append(((0, 0, k), (1, 1, k), (2, 2, k)))  # Diagonals
            if i == 0 and j == 2:
                lines.append(((0, 2, k), (1, 1, k), (2, 0, k)))  # Diagonals
            # ... (similar logic for other diagonals)

# Special 3D diagonals 
lines.append(((0, 0, 0), (1, 1, 1), (2, 2, 2)))
lines.append(((2, 0, 0), (1, 1, 1), (0, 2, 2)))
lines.append(((0, 2, 0), (1, 1, 1), (2, 0, 2)))
lines.append(((0, 0, 2), (1, 1, 1), (2, 2, 0)))

# Gurobi model setup
model = gp.Model('Tic_Tac_Toe')
isX = model.addVars(size, size, size, vtype=GRB.BINARY, name="isX")  # Tracks placement of X's
isLine = model.addVars(lines, vtype=GRB.BINARY, name="isLine")   # Indicates if a line is complete with X's

# Constraint: Exactly 14 X's on the board
x14 = model.addConstr(isX.sum() == 14)

# Constraints: Enforce winning line logic
for line in lines:
    model.addGenConstrIndicator(isLine[line], False, isX[line[0]] + isX[line[1]] + isX[line[2]] >= 1)  # At least one X on a line
    model.addGenConstrIndicator(isLine[line], False, isX[line[0]] + isX[line[1]] + isX[line[2]] <= 2)  # No O's on the line

# Objective: Maximize the number of complete lines (for X)
model.setObjective(isLine.sum())

model.optimize()