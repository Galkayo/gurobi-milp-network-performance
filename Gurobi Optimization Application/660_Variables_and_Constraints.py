from gurobipy import Model, GRB

def create_model():
    # Create a new model
    m = Model("integer_programming_model")

    # Number of variables and constraints (increased significantly)
    n = 660000  # Experiment with different values to achieve desired runtime

    # Create variables
    x = [m.addVar(vtype=GRB.INTEGER, name="x"+str(i)) for i in range(n)]
    y = [m.addVar(vtype=GRB.INTEGER, name="y"+str(i)) for i in range(n)]
    c = [m.addVar(vtype=GRB.INTEGER, name="c"+str(i)) for i in range(n)]

    # Set objective (Minimize the sum of squares and product of variables)
    # Set objective (Minimize a non-convex function)  # Not applicable here
    # Set objective (Minimize the sum of x and y variables)
    m.setObjective(sum(x[i] + y[i] for i in range(n)), GRB.MINIMIZE)

    # Add linear constraints (modified for denser structure)
    for i in range(n):
        m.addConstr(x[i] + y[i] == c[i])

        # Add additional constraints to create a denser linear system
        for j in range(max(0, i-5), min(n, i+5)):  # Consider variables within a window
            if i != j:
                m.addConstr(x[i] + y[j] <= c[i] + c[j] + 1)  # Add a constant offset (experiment with values)
                m.addConstr(x[j] + y[i] <= c[i] + c[j] + 1)

    return m


def solve_model(m):
    # Solve the model
    m.optimize()

    # Print the runtime
    print('The optimization took {} seconds.'.format(m.Runtime))

# Create and solve model
model = create_model()
solve_model(model)


# tried to make it as dense as possible: "The optimization took 0.004221200942993164 seconds."
