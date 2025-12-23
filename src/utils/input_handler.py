from utils.logger import LoggerInstance

class InputHandler:
    def GetUserInputs(self):
        LoggerInstance.Info("Getting user inputs")
        
        Inputs = {}
        Inputs["GcCompletion"] = self._GetFloat("Current GC completion (0-1)", 0, 1, 0.3)
        Inputs["TotalGcHours"] = self._GetFloat("Total GC hours needed", 50, 200, 100)
        Inputs["Horizon"] = self._GetInt("Planning horizon (days)", 7, 60, 30)
        
        return Inputs
    
    def _GetFloat(self, Prompt, Min, Max, Default):
        while True:
            try:
                Value = input(f"{Prompt} [{Default}]: ").strip()
                if not Value:
                    return Default
                Value = float(Value)
                if Min <= Value <= Max:
                    return Value
            except ValueError:
                pass
    
    def _GetInt(self, Prompt, Min, Max, Default):
        return int(self._GetFloat(Prompt, Min, Max, Default))
