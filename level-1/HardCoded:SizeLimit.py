from gurobipy import Model, GRB

def create_model():
    # Create a new model
    m = Model("large_linear_model")

    # Number of variables and constraints
    n = 667

    # Create variables and constraints
    for i in range(n):
        # Create variables
        x = m.addVar(vtype=GRB.CONTINUOUS, name="x"+str(i))
        y = m.addVar(vtype=GRB.CONTINUOUS, name="y"+str(i))
        c = m.addVar(vtype=GRB.CONTINUOUS, name="c"+str(i))

        # Set objective
        m.setObjective(x + y - c, GRB.MINIMIZE)

        # Add constraint: x + y = c
        m.addConstr(x + y == c, "c"+str(i))

    return m

def solve_model(m):
    # Solve the model
    m.optimize()

    # Print the runtime
    print('The optimization took {} seconds.'.format(m.Runtime))

# Create and solve model
model = create_model()
solve_model(model)
