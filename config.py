from pathlib import Path

# Paths
BASE_DIR = Path(__file__).parent
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)
EXPERIMENT_DIR = OUTPUT_DIR / "experiments"
EXPERIMENT_DIR.mkdir(exist_ok=True)

# Time horizon
HORIZON = 30
SCENARIOS = 4

# Resource budgets
MAX_HOURS = 16
MAX_ENERGY = 100
MAX_EMOTION = 100

# Task parameters with anonymized names
TASKS = {
    "Task1": {"energy": 15, "emotion": 12, "min": 1, "max": 6},
    "Task2": {"energy": 12, "emotion": 10, "min": 1, "max": 4},
    "Task3": {"energy": 10, "emotion": 5, "min": 2, "max": 8},
    "Task4": {"energy": 0, "emotion": -5, "min": 1, "max": 4},
    "Task5": {"energy": 12, "emotion": 8, "min": 1, "max": 6},
    "Task6": {"energy": 5, "emotion": -3, "min": 0, "max": 3},
    "Task7": {"energy": 8, "emotion": -4, "min": 0, "max": 2},
}

# Task descriptions for academic presentation
TASK_DESCRIPTIONS = {
    "Task1": "High-priority time-critical task",
    "Task2": "Career development activity",
    "Task3": "Obligatory scheduled task",
    "Task4": "Recovery and restoration",
    "Task5": "Long-term capital building",
    "Task6": "Social engagement",
    "Task7": "Physical maintenance",
}

# Recovery scenarios
RECOVERY_HOURS = [1, 2, 3, 4]
RECOVERY_PROBS = [0.4, 0.3, 0.2, 0.1]

# Solver settings
SOLVER_TIMELIMIT = 60
SOLVER_MIPGAP = 0.01
SOLVER_THREADS = 4
