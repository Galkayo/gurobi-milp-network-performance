import gurobipy as gp
from gurobipy import GRB

# tested with Gurobi v9.0.0 and Python 3.7.0

# Parameters
budget = 30
regions, population = gp.multidict({
    0: 800, 1: 950, 2: 600,
    3: 1400, 4: 1700, 5: 1200,
    6: 550, 7: 1350, 8: 1300
})

sites, coverage, cost = gp.multidict({
    0: [{0,1,2}, 6.3],
    1: [{3,4,5}, 8.7],
    2: [{1,6,7}, 7.4],
    3: [{0,2,3,4}, 7.8],
    4: [{5,6,7,8}, 9.5],
    5: [{0,1,8}, 11.1]
})

m = gp.Model("cell_tower")

build = m.addVars(len(sites), vtype=GRB.BINARY, name="Build")
is_covered = m.addVars(len(regions), vtype=GRB.BINARY, name="Is_covered")

m.addConstrs((gp.quicksum(build[t] for t in sites if r in coverage[t]) >= is_covered[r]
                        for r in regions), name="Build2cover")
m.addConstr(build.prod(cost) <= budget, name="budget")

m.setObjective(is_covered.prod(population), GRB.MAXIMIZE)

m.optimize() 


# display optimal values of decision variables

for tower in build.keys():
    if (abs(build[tower].x) > 1e-6):
        print(f"\n Build a cell tower at location Tower {tower}.")




# References
# [1] Richard Church and Charles R. Velle. "The Maximal Covering Location Problem". Papers in Regional Science, 1974, vol. 32, issue 1, 101-118.
        
# Overall, it seems that the algorithm has determined that building cell towers at these specific locations (Tower 0, Tower 1, and Tower 4) would result in the best outcome according to the specified objective function and constraints.