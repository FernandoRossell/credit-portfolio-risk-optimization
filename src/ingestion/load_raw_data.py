"""Carga de datos raw."""
from pathlib import Path
import pandas as pd


def load_csv(path: str | Path) -> pd.DataFrame:
    return pd.read_csv(path)


def main(*args, **kwargs):
    raise NotImplementedError("Pendiente de implementar la carga coordinada de tablas raw")
