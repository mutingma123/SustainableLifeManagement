class Task:
    def __init__(self, Name, Energy, Emotion, MinHours, MaxHours):
        self.Name = Name
        self.Energy = Energy
        self.Emotion = Emotion
        self.MinHours = MinHours
        self.MaxHours = MaxHours
        self.Returns = self._SetReturns()
    
    def _SetReturns(self):
        ReturnMap = {
            "GC": {"I": 1.0, "Y": 0.1, "K": 0.2, "O": 0.1},
            "JOB": {"I": 0.0, "Y": 1.0, "K": 0.3, "O": 0.4},
            "SCH": {"I": 0.0, "Y": 0.5, "K": 0.5, "O": 0.2},
            "REST": {"I": 0.0, "Y": 0.0, "K": 0.0, "O": 0.0},
            "RES": {"I": 0.0, "Y": 0.2, "K": 0.8, "O": 0.3},
            "SOC": {"I": 0.0, "Y": 0.1, "K": 0.1, "O": 0.5},
            "EX": {"I": 0.0, "Y": 0.0, "K": 0.2, "O": 0.3}
        }
        return ReturnMap.get(self.Name, {"I": 0, "Y": 0, "K": 0, "O": 0})
