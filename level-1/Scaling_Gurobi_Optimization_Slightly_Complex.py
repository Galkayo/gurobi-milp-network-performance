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

# Objective function
# We want to penalize deviations from an ideal distribution of variables
# We'll calculate a score based on how close each variable is to its expected value
# Ideal distribution: y > x > z > w > u > v > a > b > c > d
# Penalize deviation from this order
m.setObjective(
    (1000 * (y - x)) + (1000 * (x - z)) + (1000 * (z - w)) + (1000 * (w - u)) +
    (1000 * (u - v)) + (1000 * (v - a)) + (1000 * (a - b)) + (1000 * (b - c)) + (1000 * (c - d)),
    GRB.MINIMIZE
)

# Constraints
m.addConstr(w >= 0)
m.addConstr(x >= 0)
m.addConstr(y >= 0)
m.addConstr(z >= 0)
m.addConstr(u >= 0)
m.addConstr(v >= 0)
m.addConstr(a >= 0)
m.addConstr(b >= 0)
m.addConstr(c >= 0)
m.addConstr(d >= 0)
m.addConstr(w <= 10)
m.addConstr(x <= 5)
m.addConstr(y <= 15)
m.addConstr(z <= 30)
m.addConstr(u + v <= 20)
m.addConstr(a + b + c + d <= 25)

# Additional constraints
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
    print(f"Total Penalty: {m.objVal:.2f}")
else:
    print("No solution found")
