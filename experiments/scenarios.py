SCENARIOS = {
    "baseline": {
        "GcCompletion": 0.3,
        "TotalGcHours": 100,
        "Horizon": 30,
        "Description": "Baseline: 30% initial completion",
    },
    "early_stage": {
        "GcCompletion": 0.1,
        "TotalGcHours": 100,
        "Horizon": 30,
        "Description": "Early stage: 10% initial completion",
    },
    "mid_stage": {
        "GcCompletion": 0.5,
        "TotalGcHours": 100,
        "Horizon": 30,
        "Description": "Mid stage: 50% initial completion",
    },
    "late_stage": {
        "GcCompletion": 0.8,
        "TotalGcHours": 100,
        "Horizon": 30,
        "Description": "Late stage: 80% initial completion",
    },
    "high_workload": {
        "GcCompletion": 0.3,
        "TotalGcHours": 150,
        "Horizon": 30,
        "Description": "High workload: 150 hours total required",
    },
    "short_horizon": {
        "GcCompletion": 0.3,
        "TotalGcHours": 100,
        "Horizon": 14,
        "Description": "Short planning: 14-day horizon",
    },
}
