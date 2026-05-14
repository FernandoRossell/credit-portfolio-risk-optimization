"""Registro lógico de datasets."""
from datetime import datetime


def build_dataset_metadata(file_name: str) -> dict:
    return {"file_name": file_name, "loaded_at": datetime.utcnow().isoformat()}


def main(*args, **kwargs):
    raise NotImplementedError("Pendiente de implementar versionado lógico del dataset")
