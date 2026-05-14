# Credit Portfolio Optimization & Default Prediction Platform

Proyecto esqueleto para construir un sistema end-to-end de predicción de default y optimización de portafolio de crédito usando el dataset **Home Credit Default Risk**.

> **Propósito del repositorio**
> Este proyecto está diseñado como **ejercicio de portafolio** para demostrar habilidades de data science, data engineering y MLOps.
> No está pensado como sistema productivo final ni requiere licencias empresariales o servicios de pago.

---

## Qué demuestra este proyecto
- Data science aplicada a riesgo de crédito
- Data engineering y diseño de pipelines
- Orquestación con Airflow
- Experiment tracking y model registry con MLflow
- Data quality y governance
- Serving batch/API y monitoreo
- Testing para mantenimiento y evolución futura

## Restricciones consideradas
### 1. Sin licencias de pago
La arquitectura se apoya en herramientas open source y ejecución local.

### 2. Sin subir CSV raw al repositorio
La data raw se descarga manualmente y se mantiene fuera del control de versiones.

### 3. Testing para mantenimiento futuro
El repo ya incluye estructura de pruebas unitarias, integración y fixtures sintéticos.

---

## Política de datos
**Sí se sube:** código, documentación, DAGs, configs, tests, muestras sintéticas pequeñas.  
**No se sube:** raw CSV, outputs pesados, modelos binarios grandes, credenciales.

Ver también:
- `docs/assumptions_and_constraints.md`
- `docs/testing_strategy.md`
- `docs/implementation_plan_6_weeks.md`

---

## Quickstart
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
docker compose up -d
make test
```

---

## Rutas clave
- `data/raw/` → aquí colocas manualmente los CSV
- `data/processed/` → salidas intermedias locales
- `data/features/` → featuresets locales
- `docs/implementation_plan_6_weeks.md` → plan principal de trabajo
- `docs/testing_strategy.md` → estrategia de testeo y mantenibilidad
