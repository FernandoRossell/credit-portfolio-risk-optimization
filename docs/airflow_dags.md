# Diseño de DAGs de Airflow

## Principios
- Los DAGs solo definen orquestación.
- La lógica pesada vive en `src/` y `scripts/`.
- Tareas atómicas y reejecutables.
- Retries configurados por tarea y/o DAG.

## DAGs incluidos
- `data_ingestion_dag`
- `data_preparation_dag`
- `training_dag`
- `scoring_dag`
- `monitoring_dag`
