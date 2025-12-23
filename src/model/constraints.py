import config
from gurobipy import quicksum

def AddConstraints(Optimizer):
    _AddTimeConstraints(Optimizer)
    _AddLogicalConstraints(Optimizer)
    _AddResourceConstraints(Optimizer)
    _AddRecoveryConstraints(Optimizer)
    _AddMinimumRequirements(Optimizer)

def _AddTimeConstraints(Opt):
    for Day in range(config.HORIZON):
        for Scen in range(config.SCENARIOS):
            HourSum = quicksum(Opt.H[T.Name, Day] for T in Opt.Tasks)
            Opt.Model.addConstr(HourSum + Opt.R[Day, Scen] <= config.MAX_HOURS)

def _AddLogicalConstraints(Opt):
    for Task in Opt.Tasks:
        for Day in range(config.HORIZON):
            Opt.Model.addConstr(Opt.H[Task.Name, Day] >= Task.MinHours * Opt.X[Task.Name, Day])
            Opt.Model.addConstr(Opt.H[Task.Name, Day] <= Task.MaxHours * Opt.X[Task.Name, Day])

def _AddResourceConstraints(Opt):
    for Day in range(config.HORIZON):
        EnergySum = quicksum(T.Energy * Opt.H[T.Name, Day] for T in Opt.Tasks)
        EmotionSum = quicksum(T.Emotion * Opt.H[T.Name, Day] for T in Opt.Tasks)
        SecurityBonus = 1 + 0.2 * Opt.State.SecurityLevel
        Opt.Model.addConstr(EnergySum <= config.MAX_ENERGY * SecurityBonus)
        Opt.Model.addConstr(EmotionSum <= config.MAX_EMOTION * SecurityBonus)

def _AddRecoveryConstraints(Opt):
    for Day in range(config.HORIZON):
        EmotionSum = quicksum(T.Emotion * Opt.H[T.Name, Day] for T in Opt.Tasks if T.Emotion > 0)
        for Scen in range(config.SCENARIOS):
            Opt.Model.addConstr(EmotionSum >= 0.8 * config.MAX_EMOTION - 1000 * (1 - Opt.Z[Day, Scen]))
            Opt.Model.addConstr(Opt.R[Day, Scen] >= config.RECOVERY_HOURS[Scen] * Opt.Z[Day, Scen])

def _AddMinimumRequirements(Opt):
    # Weekly GC minimum
    for Week in range(config.HORIZON // 7 + 1):
        DayStart = Week * 7
        DayEnd = min((Week + 1) * 7, config.HORIZON)
        GcSum = quicksum(Opt.H["GC", Day] for Day in range(DayStart, DayEnd))
        Opt.Model.addConstr(GcSum >= 10)
