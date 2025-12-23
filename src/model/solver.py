from utils.logger import LoggerInstance

class Solver:
    def __init__(self, Optimizer):
        self.Optimizer = Optimizer
        self.Model = Optimizer.Model
    
    def Solve(self):
        LoggerInstance.Info("Starting optimization")
        self.Model.optimize()
        
        if self.Model.Status == 2:  # Optimal
            LoggerInstance.Info(f"Optimal solution found. Objective: {self.Model.ObjVal:.2f}")
            return True
        elif self.Model.Status == 9:  # Time limit
            LoggerInstance.Warning("Time limit reached")
            return self.Model.SolCount > 0
        else:
            LoggerInstance.Error(f"Optimization failed. Status: {self.Model.Status}")
            return False
    
    def ExtractSolution(self):
        Solution = {}
        for (TaskName, Day), Var in self.Optimizer.H.items():
            if Day == 0:  # First day decisions
                if Var.X > 0.01:
                    Solution[TaskName] = round(Var.X, 2)
        return Solution
