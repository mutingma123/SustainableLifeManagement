import math

class Weights:
    def __init__(self, Horizon):
        self.Horizon = Horizon
        self.BaseWeights = {
            "I": 10.0, "Y": 5.0, "K": 3.0, "O": 2.0,
            "Energy": 0.1, "Emotion": 0.15
        }
        self.GrowthRates = {
            "I": -0.05, "Y": 0.03, "K": 0.02, "O": 0.01
        }
    
    def GetWeight(self, Type, Day, GcCompletion=0):
        Base = self.BaseWeights.get(Type, 0)
        if Type == "I":
            TimeDecay = math.exp(self.GrowthRates["I"] * Day / self.Horizon)
            return Base * (1 - GcCompletion) * TimeDecay
        elif Type in ["Y", "K", "O"]:
            Growth = self.GrowthRates.get(Type, 0)
            return Base * (1 + Growth * Day / self.Horizon)
        elif Type == "Emotion":
            StressFactor = 1 + 0.5 * (1 - GcCompletion)
            return Base * StressFactor
        return Base
