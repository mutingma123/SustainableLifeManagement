class State:
    def __init__(self, InitialGcCompletion, TotalGcHours):
        self.GcCompletion = InitialGcCompletion
        self.TotalGcHours = TotalGcHours
        self.CompletedHours = InitialGcCompletion * TotalGcHours
        self.SecurityLevel = self._CalculateSecurity()
    
    def UpdateGcProgress(self, HoursWorked):
        self.CompletedHours += HoursWorked
        self.GcCompletion = min(1.0, self.CompletedHours / self.TotalGcHours)
        self.SecurityLevel = self._CalculateSecurity()
    
    def _CalculateSecurity(self):
        BaseLevel = self.GcCompletion
        if self.GcCompletion > 0.5:
            BaseLevel += 0.2
        return min(1.0, BaseLevel)
    
    def GetStressFactor(self):
        return 1.0 - self.GcCompletion
