from src.model.task import Task
from src.model.state import State
from src.model.weights import Weights
from src.model.optimizer import Optimizer
from src.model.solver import Solver
from src.utils.input_handler import InputHandler
from src.utils.output_writer import OutputWriter
from utils.logger import LoggerInstance
import config

def Main():
    LoggerInstance.Info("Starting SLM Optimization")
    
    # Get user inputs
    InputH = InputHandler()
    UserInputs = InputH.GetUserInputs()
    
    # Initialize tasks
    Tasks = []
    for Name, Params in config.TASKS.items():
        Tasks.append(Task(Name, Params["energy"], Params["emotion"], 
                         Params["min"], Params["max"]))
    
    # Initialize state and weights
    StateObj = State(UserInputs["GcCompletion"], UserInputs["TotalGcHours"])
    WeightsObj = Weights(UserInputs["Horizon"])
    
    # Build and solve model
    Opt = Optimizer(Tasks, StateObj, WeightsObj)
    Opt.BuildModel()
    
    SolverObj = Solver(Opt)
    if SolverObj.Solve():
        Solution = SolverObj.ExtractSolution()
        
        # Write outputs
        Writer = OutputWriter()
        Writer.WriteDailyPlan(Solution)
        
        LoggerInstance.Info("Optimization complete")
    else:
        LoggerInstance.Error("Failed to find solution")

if __name__ == "__main__":
    Main()
