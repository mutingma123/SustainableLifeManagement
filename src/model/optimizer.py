import gurobipy as gp
from gurobipy import GRB
from utils.logger import LoggerInstance
import config

class Optimizer:
    def __init__(self, Tasks, State, Weights):
        self.Tasks = Tasks
        self.State = State
        self.Weights = Weights
        self.Model = gp.Model("SLM")
        self._SetSolverParams()
    
    def _SetSolverParams(self):
        self.Model.setParam("TimeLimit", config.SOLVER_TIMELIMIT)
        self.Model.setParam("MIPGap", config.SOLVER_MIPGAP)
        self.Model.setParam("Threads", config.SOLVER_THREADS)
        self.Model.setParam("OutputFlag", 0)
    
    def BuildModel(self):
        self._AddVariables()
        self._AddConstraints()
        self._SetObjective()
        LoggerInstance.Info("Model built successfully")
    
    def _AddVariables(self):
        # Implemented in variables.py
        from src.model.variables import AddVariables
        AddVariables(self)
    
    def _AddConstraints(self):
        # Implemented in constraints.py
        from src.model.constraints import AddConstraints
        AddConstraints(self)
    
    def _SetObjective(self):
        # Implemented in objective.py
        from src.model.objective import SetObjective
        SetObjective(self)
