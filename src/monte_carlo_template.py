"""Small portfolio-safe Monte Carlo template."""
import numpy as np
import pandas as pd

def simulate_profit(n=100_000, seed=42):
    rng = np.random.default_rng(seed)
    demand = rng.triangular(left=800, mode=1000, right=1400, size=n)
    unit_margin = rng.normal(loc=24, scale=3, size=n)
    fixed_cost = 18000
    profit = demand * unit_margin - fixed_cost
    return pd.Series(profit, name="profit")

def summarize(series):
    return {
        "mean": float(series.mean()),
        "std": float(series.std()),
        "p05": float(series.quantile(.05)),
        "median": float(series.median()),
        "p95": float(series.quantile(.95)),
        "probability_loss": float((series < 0).mean()),
    }
