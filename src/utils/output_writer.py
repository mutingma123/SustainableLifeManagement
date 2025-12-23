import csv
from datetime import datetime
import config
from utils.logger import LoggerInstance

class OutputWriter:
    def __init__(self):
        self.OutputDir = config.OUTPUT_DIR
    
    def WriteDailyPlan(self, Solution, Day=1):
        Filename = self.OutputDir / f"daily_plan_{datetime.now():%Y%m%d_%H%M%S}.csv"
        
        with open(Filename, 'w', newline='') as File:
            Writer = csv.writer(File)
            Writer.writerow(["Task", "Hours", "Energy", "Emotion"])
            
            for TaskName, Hours in Solution.items():
                Task = config.TASKS[TaskName]
                Energy = Task["energy"] * Hours
                Emotion = Task["emotion"] * Hours
                Writer.writerow([TaskName, Hours, Energy, Emotion])
        
        LoggerInstance.Info(f"Daily plan written to {Filename}")
    
    def WriteWeeklySchedule(self, WeeklyPlan):
        Filename = self.OutputDir / f"weekly_schedule_{datetime.now():%Y%m%d}.csv"
        
        with open(Filename, 'w', newline='') as File:
            Writer = csv.writer(File)
            Headers = ["Day"] + list(config.TASKS.keys())
            Writer.writerow(Headers)
            
            for Day, Tasks in enumerate(WeeklyPlan, 1):
                Row = [f"Day {Day}"] + [Tasks.get(T, 0) for T in config.TASKS.keys()]
                Writer.writerow(Row)
