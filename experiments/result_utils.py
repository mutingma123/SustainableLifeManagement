import json
from datetime import datetime
import config


class ExperimentExecutor:
    # Continuation of executor.py _RecordResult and SaveResults methods
    pass


def RecordResult(Self, Name, Params, Solution, ObjVal):
    Result = {
        "Scenario": Name,
        "Description": Params.get("Description", ""),
        "GcCompletion": Params["GcCompletion"],
        "TotalGcHours": Params["TotalGcHours"],
        "Horizon": Params["Horizon"],
        "ObjectiveValue": round(ObjVal, 4),
        "DayOnePlan": Solution["DayOne"],
        "WeeklyAggregate": _AggregateWeekly(Solution["AllDays"]),
    }
    return Result


def _AggregateWeekly(AllDays):
    Weekly = {}
    for DayData in AllDays:
        for TaskName, Hours in DayData.items():
            Weekly[TaskName] = Weekly.get(TaskName, 0) + Hours
    return {K: round(V, 2) for K, V in Weekly.items()}
