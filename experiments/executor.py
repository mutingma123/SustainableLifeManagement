import sys
import os

sys.path.insert(0, os.path.expandvars("$HOME/Documents/SLM"))

import csv
import json
from datetime import datetime
import config
from src.model.task import Task
from src.model.state import State
from src.model.weights import Weights
from src.model.optimizer import Optimizer
from src.model.solver import Solver
from utils.logger import LoggerInstance


class ExperimentExecutor:
    def __init__(self):
        self.Results = []
        self.OutputDir = config.EXPERIMENT_DIR

    def RunScenario(self, Name, Params):
        Tasks = self._CreateTasks()
        StateObj = State(Params["GcCompletion"], Params["TotalGcHours"])
        WeightsObj = Weights(Params["Horizon"])

        Opt = Optimizer(Tasks, StateObj, WeightsObj)
        Opt.BuildModel()

        SolverObj = Solver(Opt)
        if SolverObj.Solve():
            Solution = self._ExtractFullSolution(SolverObj, Params["Horizon"])
            self._RecordResult(Name, Params, Solution, Opt.Model.ObjVal)

    def _CreateTasks(self):
        Tasks = []
        for TaskName, Params in config.TASKS.items():
            Tasks.append(
                Task(
                    TaskName,
                    Params["energy"],
                    Params["emotion"],
                    Params["min"],
                    Params["max"],
                )
            )
        return Tasks

    def _ExtractFullSolution(self, SolverObj, Horizon):
        Solution = {"DayOne": {}, "Weekly": {}, "AllDays": []}

        for Day in range(min(7, Horizon)):
            DayData = {}
            for TaskName in config.TASKS.keys():
                Var = SolverObj.Optimizer.H[TaskName, Day]
                if Var.X > 0.01:
                    DayData[TaskName] = round(Var.X, 2)
            Solution["AllDays"].append(DayData)

        Solution["DayOne"] = Solution["AllDays"][0] if Solution["AllDays"] else {}
        return Solution

    def _RecordResult(self, Name, Params, Solution, ObjVal):
        Result = {
            "Scenario": Name,
            "Description": Params.get("Description", ""),
            "InitialCompletion": Params["GcCompletion"],
            "TotalHoursRequired": Params["TotalGcHours"],
            "Horizon": Params["Horizon"],
            "ObjectiveValue": round(ObjVal, 4),
            "DayOnePlan": Solution["DayOne"],
            "WeeklyAggregate": self._AggregateWeekly(Solution["AllDays"]),
        }
        self.Results.append(Result)

    def _AggregateWeekly(self, AllDays):
        Weekly = {}
        for DayData in AllDays:
            for TaskName, Hours in DayData.items():
                Weekly[TaskName] = Weekly.get(TaskName, 0) + Hours
        return {K: round(V, 2) for K, V in Weekly.items()}

    def SaveResults(self):
        Timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        JsonPath = self.OutputDir / f"results_{Timestamp}.json"
        CsvPath = self.OutputDir / f"results_{Timestamp}.csv"

        with open(JsonPath, "w") as F:
            json.dump(self.Results, F, indent=2)

        self._SaveCsv(CsvPath)
        LoggerInstance.Info(f"Results saved to {JsonPath}")

    def _SaveCsv(self, Path):
        with open(Path, "w", newline="") as F:
            Writer = csv.writer(F)
            Headers = ["Scenario", "InitialCompletion", "ObjectiveValue"]
            Headers += [f"{T}_Hours" for T in config.TASKS.keys()]
            Writer.writerow(Headers)

            for R in self.Results:
                Row = [R["Scenario"], R["InitialCompletion"], R["ObjectiveValue"]]
                for TaskName in config.TASKS.keys():
                    Row.append(R["WeeklyAggregate"].get(TaskName, 0))
                Writer.writerow(Row)
