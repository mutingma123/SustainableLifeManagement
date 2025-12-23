import config
from gurobipy import GRB

def AddVariables(Optimizer):
    M = Optimizer.Model
    T = config.HORIZON
    S = config.SCENARIOS
    
    # Binary task selection
    Optimizer.X = {}
    for Task in Optimizer.Tasks:
        for Day in range(T):
            Name = f"x_{Task.Name}_{Day}"
            Optimizer.X[Task.Name, Day] = M.addVar(vtype=GRB.BINARY, name=Name)
    
    # Hours allocated
    Optimizer.H = {}
    for Task in Optimizer.Tasks:
        for Day in range(T):
            Name = f"h_{Task.Name}_{Day}"
            Optimizer.H[Task.Name, Day] = M.addVar(lb=0, name=Name)
    
    # Recovery hours per scenario
    Optimizer.R = {}
    for Day in range(T):
        for Scen in range(S):
            Name = f"r_{Day}_{Scen}"
            Optimizer.R[Day, Scen] = M.addVar(lb=0, ub=4, name=Name)
    
    # Emotional exhaustion indicators
    Optimizer.Z = {}
    for Day in range(T):
        for Scen in range(S):
            Name = f"z_{Day}_{Scen}"
            Optimizer.Z[Day, Scen] = M.addVar(vtype=GRB.BINARY, name=Name)
