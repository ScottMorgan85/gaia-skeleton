import pandas as pd
from pathlib import Path

DATA_DIR = Path("data/demo")

def _read_csv(name: str) -> pd.DataFrame:
    path = DATA_DIR / name
    if not path.exists():
        raise FileNotFoundError(f"Missing demo dataset: {path}. See README for setup.")
    return pd.read_csv(path)

def load_demo_clients() -> pd.DataFrame:
    return _read_csv("client_data.csv")

def load_demo_transactions() -> pd.DataFrame:
    return _read_csv("client_transactions.csv")

def load_demo_returns() -> pd.DataFrame:
    return _read_csv("strategy_returns.csv")
