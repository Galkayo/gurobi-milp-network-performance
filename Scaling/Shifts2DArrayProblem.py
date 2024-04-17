from gurobipy import Model, GRB

# Sample data
# Sets of days and workers
Shifts = ["Mon1", "Tue2", "Wed3", "Thu4", "Fri5", "Sat6",
          "Sun7", "Mon8", "Tue9", "Wed10", "Thu11", "Fri12", "Sat13",
          "Sun14"]
Workers = ["Amy", "Bob", "Cathy", "Dan", "Ed", "Fred", "Gu"]

nShifts = len(Shifts)
nWorkers = len(Workers)

# Number of workers required for each shift
shiftRequirements = [3, 2, 4, 4, 5, 6, 5, 2, 2, 3, 4, 6, 7, 5]

# Amount each worker is paid to work one shift
pay = [10, 12, 10, 8, 8, 9, 11]

# Worker availability: 0 if the worker is unavailable for a shift
availability = [[0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
                [1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0],
                [0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                [0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1],
                [1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1],
                [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Model
m = Model("assignment")

# Assignment variables: x[w][s] == 1 if worker w is assigned
# to shift s. Since an assignment model always produces integer
# solutions, we use continuous variables and solve as an LP.
x = [[m.addVar(0, availability[w][s], pay[w], GRB.CONTINUOUS,
               Workers[w] + "." + Shifts[s]) for s in range(nShifts)] for w in range(nWorkers)]

# The objective is to minimize the total pay costs
m.setObjective(sum(x[w][s] for w in range(nWorkers) for s in range(nShifts)), GRB.MINIMIZE)

# Constraint: assign exactly shiftRequirements[s] workers
# to each shift s
for s in range(nShifts):
    m.addConstr(sum(x[w][s] for w in range(nWorkers)) == shiftRequirements[s], Shifts[s])

# Optimize
m.optimize()

status = m.status
if status == GRB.UNBOUNDED:
    print("The model cannot be solved because it is unbounded")
elif status == GRB.OPTIMAL:
    print("The optimal objective is", m.objVal)
elif status != GRB.INF_OR_UNBD and status != GRB.INFEASIBLE:
    print("Optimization was stopped with status", status)

# Do IIS
if status == GRB.INFEASIBLE:
    print("The model is infeasible; computing IIS")
    removed = []

    # Loop until we reduce to a model that can be solved
    # while True:
    #     m.computeIIS()
    #     print("\nThe following constraint cannot be satisfied:")
    #     for c in m.getConstrs():
    #         if c.IISConstr:
    #             print(c.ConstrName)
    #             # Remove a single constraint from the model
    #             removed.append(c.ConstrName)
    #             m.remove(c)
    #             break

        print()
        m.optimize()
        status = m.status

        if status == GRB.UNBOUNDED:
            print("The model cannot be solved because it is unbounded")
            break
        elif status == GRB.OPTIMAL:
            print("The optimal objective is", m.objVal)
            break
