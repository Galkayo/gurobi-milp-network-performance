from gurobipy import Model, GRB

m = Model("Complex_Scaling_Gurobi")

# Decision variables
w = m.addVar(vtype=GRB.INTEGER, name="w")
x = m.addVar(vtype=GRB.INTEGER, name="x")
y = m.addVar(vtype=GRB.INTEGER, name="y")
z = m.addVar(vtype=GRB.INTEGER, name="z")
u = m.addVar(vtype=GRB.INTEGER, name="u")
v = m.addVar(vtype=GRB.INTEGER, name="v")
a = m.addVar(vtype=GRB.INTEGER, name="a")
b = m.addVar(vtype=GRB.INTEGER, name="b")
c = m.addVar(vtype=GRB.INTEGER, name="c")  # New variable
d = m.addVar(vtype=GRB.INTEGER, name="d")  # New variable

# Objective function: Minimize the total value of all decision variables
m.setObjective(w + x + y + z + u + v + a + b + c + d, GRB.MAXIMIZE)

# Constraints
m.addConstr(w >= 0)  # Ensure non-negativity for all variables
m.addConstr(x >= 0)
m.addConstr(y >= 0)
m.addConstr(z >= 0)
m.addConstr(u >= 0)
m.addConstr(v >= 0)
m.addConstr(a >= 0)
m.addConstr(b >= 0)
m.addConstr(c >= 0)
m.addConstr(d >= 0)
m.addConstr(w <= 10)  # Upper bound for w
m.addConstr(x <= 5)   # Upper bound for x
m.addConstr(y <= 15)  # Upper bound for y
m.addConstr(z <= 30)  # Upper bound for z
m.addConstr(u + v <= 20)  # Upper bound for u + v
m.addConstr(a + b + c + d <= 25)  # Upper bound for a + b + c + d

# Additional constraints to make the problem feasible
m.addConstr(w + x + y + z + u + v + a + b + c + d >= 1)

m.optimize()

if m.status == GRB.OPTIMAL:
    print("Optimal Solution:")
    print(f"- w: {w.x:.0f}")
    print(f"- x: {x.x:.0f}")
    print(f"- y: {y.x:.0f}")
    print(f"- z: {z.x:.0f}")
    print(f"- u: {u.x:.0f}")
    print(f"- v: {v.x:.0f}")
    print(f"- a: {a.x:.0f}")
    print(f"- b: {b.x:.0f}")
    print(f"- c: {c.x:.0f}")
    print(f"- d: {d.x:.0f}")
    print(f"Total Value: {m.objVal:.2f}")
else:
    print("No solution found")
