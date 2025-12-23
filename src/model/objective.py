import config
from gurobipy import quicksum

def SetObjective(Optimizer):
    Objective = 0
    
    for Day in range(config.HORIZON):
        DayUtility = 0
        GcProgress = Optimizer.State.GcCompletion
        
        for Task in Optimizer.Tasks:
            Hours = Optimizer.H[Task.Name, Day]
            
            # Return components
            for ReturnType in ["I", "Y", "K", "O"]:
                Weight = Optimizer.Weights.GetWeight(ReturnType, Day, GcProgress)
                Return = Task.Returns.get(ReturnType, 0)
                DayUtility += Weight * Return * Hours
            
            # Cost components
            EnergyCost = Optimizer.Weights.GetWeight("Energy", Day)
            EmotionCost = Optimizer.Weights.GetWeight("Emotion", Day, GcProgress)
            DayUtility -= EnergyCost * Task.Energy * Hours
            DayUtility -= EmotionCost * max(0, Task.Emotion) * Hours
        
        # Expected value over scenarios
        for Scen in range(config.SCENARIOS):
            Prob = config.RECOVERY_PROBS[Scen]
            Objective += Prob * (0.95 ** Day) * DayUtility
    
    Optimizer.Model.setObjective(Objective, sense=-1)  # Maximize
