# Sustainable Life Management (SLM)

A mixed-integer stochastic programming framework for optimal multi-period resource allocation under uncertainty.

[![DOI](https://img.shields.io/badge/DOI-10.2139/ssrn.5369435-blue)](https://dx.doi.org/10.2139/ssrn.5369435)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Overview

This repository contains a rigorous mathematical formulation and implementation for multi-period capital allocation over a 30-day planning horizon. The framework treats time allocation as a capital budgeting problem under uncertainty, incorporating stochastic recovery requirements and state-dependent decision making.

**Key Innovation**: Rolling horizon optimization with uncertainty in emotional recovery and state-tracking for critical long-term objectives.

## Features

- **Mixed-Integer Stochastic Programming**: Optimal allocation of time, energy, and emotional resources
- **Rolling Horizon Framework**: Daily re-optimization based on updated state information
- **Uncertainty Modeling**: Stochastic scenarios for emotional recovery requirements
- **State Tracking**: Immigration progress affects future allocations
- **Multi-Dimensional Returns**: Balances immigration, income, capital accumulation, and optionality
- **Computational Tractability**: Solvable with modern MILP solvers (Gurobi, CPLEX)

## Problem Formulation

### Task Categories

The model considers seven task categories:

| Task | Description | Energy/hr | Emotion/hr | Min hrs | Max hrs |
|------|-------------|-----------|------------|---------|---------|
| **GC** | Green card preparation | 15 | 12 | 1 | 6 |
| **JOB** | Job searching | 12 | 10 | 1 | 4 |
| **SCH** | School/teaching | 10 | 5 | 2 | 8 |
| **REST** | Rest and recovery | 0 | -5 | 1 | 4 |
| **RES** | PhD research | 12 | 8 | 1 | 6 |
| **SOC** | Social activities | 5 | -3 | 0 | 3 |
| **EX** | Exercise | 8 | -4 | 0 | 2 |

### Resource Constraints

- **Time Budget**: 16 usable hours per day
- **Energy Budget**: 100 units per day
- **Emotional Capacity**: 100 units per day

### Stochastic Recovery

When emotional load exceeds 80% of capacity, recovery is required with uncertain duration:
- 1 hour: 40% probability
- 2 hours: 30% probability
- 3 hours: 20% probability
- 4 hours: 10% probability

## Mathematical Model

### Objective Function

Maximize expected utility over the planning horizon:

$$\max \mathbb{E}_s \left[ \sum_t \delta^t \left( \sum_i U_{it}(h_{it}, g_t) \right) \right]$$

Where utility incorporates:
- Immigration progress return
- Income/employability return
- Long-term capital accumulation
- Optionality improvement
- Energy and emotional costs

### Key Constraints

1. **Time allocation**: Total hours + recovery $\leq 16$ hours/day
2. **Energy consumption**: Weighted by immigration security level
3. **Emotional load**: With stochastic recovery requirements
4. **Minimum requirements**: Weekly GC work, school obligations, daily rest
5. **State evolution**: Green card progress tracking

## Model Properties

### Computational Complexity

For typical parameters (7 tasks, 30 days, 4 scenarios):
- **Binary variables**: ~840
- **Continuous variables**: ~840
- **Constraints**: ~1,680

This is well within the capability of modern MILP solvers.

### Feasibility Guarantee

The model is feasible if and only if:

$$\sum_i h_i^{\min} + \max_s \beta_s \leq H^{\max}$$

## Implementation

### Algorithm: Rolling Horizon

```
For each decision day d:
    1. Update parameters based on completed work
    2. Solve optimization for days [d, d+29]
    3. Extract first-day decisions
    4. Implement decisions for day d
    5. Observe actual recovery requirement
    6. Update state and re-optimize
```

### Solver Configuration

Recommended Gurobi settings:
- **MIPGap**: 0.01 (1% optimality gap)
- **TimeLimit**: 60 seconds
- **Threads**: 4
- **MIPFocus**: 1 (emphasize feasibility)

## Repository Structure

```
SLM/
├── Formulation/
│   └── Formulation.tex          # Complete mathematical formulation
├── src/                         # Implementation code (coming soon)
├── config/                      # Parameter configuration files
├── tests/                       # Unit and integration tests
├── LICENSE                      # MIT License
└── README.md                    # This file
```

## Getting Started

### Prerequisites

- Python 3.8+
- Gurobi Optimizer (academic license available)
- NumPy, Pandas for data handling

### Installation

```bash
git clone https://github.com/mutingma123/SLM.git
cd SLM
pip install -r requirements.txt
```

### Basic Usage

```python
# Coming soon - implementation in progress
from slm import MultiPeriodOptimizer

optimizer = MultiPeriodOptimizer(
    horizon=30,
    initial_gc_completion=0.3,
    total_gc_hours=100
)

solution = optimizer.optimize()
daily_plan = solution.get_today_decisions()
```

## Model Extensions

The framework supports several extensions:

1. **Adaptive Learning**: Bayesian updating of recovery probabilities
2. **Multi-Stage Recourse**: Intraday reallocation based on actual energy levels
3. **Risk Measures**: CVaR optimization for risk-averse planning
4. **Multi-Agent**: Extension to household resource allocation

## Validation

### Sensitivity Analysis

Critical parameters for calibration:
- $\gamma$: Stress from incomplete GC work
- $\lambda_1, \lambda_2$: Energy and emotional cost weights
- $w_I^0$: Initial immigration priority weight
- Recovery scenario probabilities

### Solution Quality Metrics

- Green card completion trajectory
- Daily energy utilization rate
- Emotional load variance
- Weekly pattern stability

## Citation

If you use this framework in your research, please cite:

```bibtex
@article{ma2025sustainable,
  title={Multi-Period Capital Allocation Under Uncertainty: A Mixed-Integer Stochastic Programming Formulation},
  author={Ma, Muting (Don)},
  year={2025},
  doi={10.2139/ssrn.5369435},
  url={https://dx.doi.org/10.2139/ssrn.5369435}
}
```

## Documentation

For detailed mathematical formulation, see:
- [Formulation Document](Formulation/Formulation.tex) - Complete mathematical specification
- [SSRN Paper](https://dx.doi.org/10.2139/ssrn.5369435) - Published version

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Muting (Don) Ma, Ph.D.**

## Acknowledgments

- Framework inspired by capital budgeting and stochastic programming literature
- Recovery modeling based on empirical observations of cognitive load patterns

---

**Status**: Active Development | **Version**: 1.0 | **Last Updated**: 2025-12-23