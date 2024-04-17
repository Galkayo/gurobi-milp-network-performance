from gurobipy import Model, GRB

def create_model():
    # Create a new model
    m = Model("integer_programming_model")

    # Number of variables and constraints (significantly increased)
    n = 10000  # Experiment with larger values (e.g., 20000)

    # Create variables
    x = [m.addVar(vtype=GRB.INTEGER, name="x"+str(i)) for i in range(n)]
    y = [m.addVar(vtype=GRB.INTEGER, name="y"+str(i)) for i in range(n)]
    c = [m.addVar(vtype=GRB.INTEGER, name="c"+str(i)) for i in range(n)]

  
    m.setObjective(sum(x[i] + y[i] for i in range(n)), GRB.MAXIMIZE) # made it maximized

    # Add linear constraints (modified for denser structure)
    for i in range(n):
        m.addConstr(x[i] + y[i] == c[i])

        # Add additional constraints to create a denser linear system
        for j in range(max(0, i-10), min(n, i+10)):  # Consider variables within a wider window
            if i != j:
                m.addConstr(x[i] + y[j] <= c[i] + c[j] + 10)  # Increased constant offset
                m.addConstr(x[j] + y[i] <= c[i] + c[j] + 10)

    return m


def solve_model(m):
    # Solve the model
    m.optimize()

    # Print the runtime
    print('The optimization took {} seconds.'.format(m.Runtime))

# Create and solve model
model = create_model()
solve_model(model)
