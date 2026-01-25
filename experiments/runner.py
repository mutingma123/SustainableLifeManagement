import sys
import os

sys.path.insert(0, os.path.expandvars("$HOME/Documents/SLM"))

from experiments.scenarios import SCENARIOS
from experiments.executor import ExperimentExecutor
from utils.logger import LoggerInstance


def RunAllExperiments():
    LoggerInstance.Info("Starting experiment suite")
    Executor = ExperimentExecutor()

    for Name, Params in SCENARIOS.items():
        LoggerInstance.Info(f"Running scenario: {Name}")
        Executor.RunScenario(Name, Params)

    Executor.SaveResults()
    LoggerInstance.Info("All experiments complete")


if __name__ == "__main__":
    RunAllExperiments()
