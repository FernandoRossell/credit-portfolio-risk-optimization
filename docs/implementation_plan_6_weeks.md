# Plan de implementación de 6 semanas

> Objetivo: construir un proyecto **portfolio-ready** de predicción de default y optimización de portafolio usando el dataset **Home Credit Default Risk**, con foco en **calidad de datos, feature engineering, modelado, MLOps, testing y documentación**.

---

## Consideraciones clave antes de empezar

### 1. Sin licencias empresariales
Este plan asume que trabajarás con herramientas open source y ejecución local. Por eso, cada paso evita depender de servicios pagos o componentes enterprise.

### 2. Sin subir los CSV raw al repositorio
La data se tratará como insumo local. Los pasos del plan te indicarán cómo referenciarla y usarla sin versionarla en GitHub.

### 3. Con testing desde el diseño
El plan incorpora pruebas y validaciones como parte del desarrollo, no como algo agregado al final. La idea es que tu repo sea más fácil de mantener, extender y refactorizar.

---

## Cómo leer este plan
Cada semana incluye:
- **Qué**: qué debes construir o completar.
- **Por qué**: la razón técnica o estratégica del paso.
- **Para qué**: cómo aporta al objetivo final del proyecto.
- **Cómo**: una guía breve y práctica para abordarlo.
- **Entregables**: qué deberías tener al final.
- **Checklist**: lista de control.
- **Criterio de salida**: qué debe cumplirse antes de avanzar.

---

# Semana 1 — Fundaciones, setup y entendimiento de datos

## Objetivo general
Dejar el repo operable, entender el dataset, documentar su estructura y preparar las bases de configuración, calidad y manejo correcto de datos.

## Qué vas a trabajar
- configuración del proyecto
- carga de datos raw
- documentación del dataset
- política de manejo de datos
- validaciones de calidad iniciales

## Archivos foco
- `README.md`
- `.env.example`
- `configs/base.yaml`
- `configs/dev.yaml`
- `configs/model_config.yaml`
- `src/config.py`
- `src/logging_config.py`
- `src/utils/paths.py`
- `src/utils/io.py`
- `src/ingestion/load_raw_data.py`
- `src/ingestion/dataset_registry.py`
- `docs/data_dictionary_template.md`
- `notebooks/01_eda.md`
- `notebooks/02_data_quality.md`
- `quality/great_expectations/...`
- `src/monitoring/data_quality.py`
- `docs/assumptions_and_constraints.md`
- `data/README.md`

## Qué hacer
### A. Configurar el proyecto base
**Qué:** centralizar configuración, rutas y logging.  
**Por qué:** evita valores hardcodeados y facilita mantenimiento.  
**Para qué:** cambiar parámetros globales sin tocar múltiples archivos.  
**Cómo:** completa `.env.example`, YAMLs y funciones de carga en `src/config.py` y `src/logging_config.py`.

### B. Definir la política de manejo de datos
**Qué:** documentar que la data raw no se sube a GitHub.  
**Por qué:** los CSV son pesados y no aportan valor dentro del repo.  
**Para qué:** mantener un repo limpio y profesional.  
**Cómo:** actualiza `.gitignore`, `README.md` y `data/README.md`.

### C. Entender el dataset formalmente
**Qué:** construir un diccionario de datos y un EDA inicial.  
**Por qué:** sin entender granularidad y llaves, el feature engineering falla.  
**Para qué:** diseñar joins y agregaciones correctas.  
**Cómo:** completa `docs/data_dictionary_template.md` y resume hallazgos en `notebooks/01_eda.md`.

### D. Implementar ingestión y validación inicial
**Qué:** leer la data local y correr checks básicos.  
**Por qué:** evita descubrir problemas de esquema muy tarde.  
**Para qué:** tener una base reproducible para el resto del pipeline.  
**Cómo:** implementa `src/ingestion/load_raw_data.py`, `src/ingestion/dataset_registry.py` y `src/monitoring/data_quality.py`.

## Entregables
- repo con setup claro
- política explícita de no subir data raw
- diccionario de datos inicial completo
- carga de datos funcional
- validaciones mínimas de calidad sobre raw

## Checklist
- [ ] Actualizar `README.md` con objetivos, restricciones y política de datos.
- [ ] Completar `.env.example` y configs base.
- [ ] Implementar `src/config.py` y `src/logging_config.py`.
- [ ] Implementar utilidades de rutas e I/O.
- [ ] Implementar ingestión y registro de dataset.
- [ ] Completar diccionario de datos.
- [ ] Documentar EDA inicial.
- [ ] Crear expectations mínimas para raw.
- [ ] Implementar runner simple de calidad.

## Criterio de salida
Puedes explicar el dataset de punta a punta, cargarlo localmente sin errores y ejecutar validaciones básicas.

---

# Semana 2 — Limpieza y preparación de datasets intermedios

## Objetivo general
Transformar la capa raw en tablas limpias, consistentes y listas para agregaciones.

## Qué vas a trabajar
- limpieza de tabla principal
- limpieza de tablas auxiliares
- reglas de tratamiento de nulos y anomalías
- diseño documentado del feature engineering

## Archivos foco
- `src/preprocessing/clean_application.py`
- `src/preprocessing/clean_aux_tables.py`
- `notebooks/03_feature_engineering.md`
- `docs/data_dictionary_template.md`
- `src/monitoring/data_quality.py`
- `tests/unit/`

## Qué hacer
### A. Limpiar la tabla principal
**Qué:** estabilizar `application_train` y `application_test`.  
**Por qué:** será el ancla del dataset final.  
**Para qué:** dejar una base limpia para joins y modelado.  
**Cómo:** corrige tipos, homologa categorías, trata nulos/anomalías y guarda outputs en `data/processed/`.

### B. Limpiar tablas auxiliares
**Qué:** preparar `bureau`, `previous_application`, `installments_payments`, etc.  
**Por qué:** mucho del valor vendrá de señales históricas.  
**Para qué:** permitir agregaciones confiables por cliente.  
**Cómo:** corrige llaves, tipos, duplicados y documenta decisiones.

### C. Diseñar el feature engineering antes de programarlo
**Qué:** decidir qué señales extraer de cada fuente.  
**Por qué:** evita columnas redundantes o con leakage.  
**Para qué:** construir features con criterio y poder defenderlas.  
**Cómo:** documenta en `notebooks/03_feature_engineering.md`.

### D. Añadir primeras pruebas unitarias simples
**Qué:** probar funciones pequeñas desde ya.  
**Por qué:** reduce el costo de estabilizar el proyecto después.  
**Para qué:** dejar la base lista para futuras modificaciones.  
**Cómo:** agrega tests a config, paths, I/O o funciones simples de limpieza.

## Entregables
- tabla principal limpia
- tablas auxiliares limpias
- reglas de limpieza documentadas
- plan de features documentado
- primeras pruebas unitarias funcionando

## Checklist
- [ ] Limpiar `application_train/test`.
- [ ] Guardar outputs en `data/processed/`.
- [ ] Limpiar tablas auxiliares.
- [ ] Verificar consistencia de llaves.
- [ ] Actualizar diccionario de datos.
- [ ] Documentar plan de feature engineering.
- [ ] Escribir primeras pruebas unitarias.

## Criterio de salida
Tienes tablas limpias persistidas, una estrategia clara de features y primeros tests ejecutándose.

---

# Semana 3 — Feature engineering y dataset gold

## Objetivo general
Construir el dataset final con una fila por `SK_ID_CURR`, listo para modelado y controlado por validaciones.

## Qué vas a trabajar
- agregaciones históricas por fuente
- join final del featureset
- validación del dataset gold
- pruebas de transformaciones clave

## Archivos foco
- `src/features/aggregate_bureau.py`
- `src/features/aggregate_previous.py`
- `src/features/aggregate_installments.py`
- `src/features/build_featureset.py`
- `quality/great_expectations/expectation_suites/`
- `src/monitoring/data_quality.py`
- `tests/unit/`
- `tests/fixtures/`

## Qué hacer
### A. Construir agregados de `bureau`
**Qué:** resumir historial externo.  
**Por qué:** suele capturar señales fuertes de riesgo.  
**Para qué:** añadir contexto histórico al cliente.  
**Cómo:** crea conteos, ratios, recencia y montos agregados por `SK_ID_CURR`.

### B. Construir agregados de `previous_application`
**Qué:** resumir comportamiento pasado dentro de la institución.  
**Por qué:** aporta señales de rechazo/aprobación y dinámica de montos.  
**Para qué:** enriquecer el perfil histórico del cliente.  
**Cómo:** cuenta solicitudes previas, resume aprobadas/rechazadas y agrega montos.

### C. Construir agregados de `installments_payments`
**Qué:** resumir comportamiento de pago histórico.  
**Por qué:** la puntualidad de pago es muy informativa para default.  
**Para qué:** capturar atraso, severidad y consistencia.  
**Cómo:** calcula atraso promedio, pagos tardíos y recencia de incumplimiento.

### D. Construir el dataset gold
**Qué:** unir application limpia con todos los agregados.  
**Por qué:** necesitas un dataset único para entrenamiento e inferencia.  
**Para qué:** pasar de fuentes relacionales a dataset tabular final.  
**Cómo:** une por `SK_ID_CURR`, valida unicidad y guarda en `data/features/`.

### E. Validar el featureset y probar transformaciones
**Qué:** ejecutar checks y pruebas sobre el activo principal del proyecto.  
**Por qué:** entrenar sobre un featureset defectuoso da resultados engañosos.  
**Para qué:** blindar el paso más importante del pipeline.  
**Cómo:** añade quality checks y usa fixtures sintéticos para agregados clave.

## Entregables
- agregados por fuente
- dataset gold reproducible
- checks del gold dataset
- pruebas unitarias de transformaciones críticas

## Checklist
- [ ] Implementar agregaciones de `bureau`.
- [ ] Implementar agregaciones de `previous_application`.
- [ ] Implementar agregaciones de `installments_payments`.
- [ ] Construir y guardar el featureset final.
- [ ] Validar una fila por `SK_ID_CURR`.
- [ ] Añadir quality checks del gold dataset.
- [ ] Crear fixtures sintéticos.
- [ ] Escribir pruebas unitarias para agregados clave.

## Criterio de salida
Tienes un featureset final reproducible, validado y con primeras pruebas sobre su lógica central.

---

# Semana 4 — Modelado, evaluación y decisión de negocio

## Objetivo general
Entrenar modelos comparables, evaluar su calidad y traducir scores en decisiones de portafolio.

## Qué vas a trabajar
- métricas de clasificación
- baseline y modelo fuerte
- thresholding de negocio
- explicabilidad básica
- análisis por segmento

## Archivos foco
- `src/evaluation/metrics.py`
- `src/evaluation/thresholding.py`
- `src/evaluation/calibration.py`
- `src/evaluation/segment_analysis.py`
- `src/training/train_utils.py`
- `src/training/train_baseline.py`
- `src/training/train_boosting.py`
- `notebooks/04_model_baselines.md`
- `notebooks/05_model_explainability.md`
- `notebooks/06_threshold_portfolio_strategy.md`
- `tests/unit/`

## Qué hacer
### A. Estandarizar métricas
**Qué:** definir una capa única de evaluación.  
**Por qué:** comparar experimentos sin estándar lleva a inconsistencias.  
**Para qué:** benchmark reproducible entre baseline y modelos complejos.  
**Cómo:** implementa ROC-AUC, PR-AUC, KS, Brier y métricas por threshold.

### B. Entrenar un baseline serio
**Qué:** construir una referencia simple e interpretable.  
**Por qué:** sirve como punto de comparación honesto.  
**Para qué:** saber si el problema ya tiene señal útil.  
**Cómo:** usa Logistic Regression como benchmark mínimo.

### C. Entrenar el modelo principal
**Qué:** implementar un modelo de boosting.  
**Por qué:** suele capturar mejor relaciones complejas.  
**Para qué:** tener un candidato fuerte para el portfolio.  
**Cómo:** usa LightGBM o XGBoost con manejo básico de imbalance.

### D. Traducir score a decisiones
**Qué:** pasar de score a acción.  
**Por qué:** en crédito importa la decisión operativa, no solo AUC.  
**Para qué:** demostrar pensamiento de negocio.  
**Cómo:** define thresholds o buckets y simula approval rate vs bad rate.

### E. Añadir pruebas a métricas y utilidades
**Qué:** proteger la lógica que más se reutilizará.  
**Por qué:** estas piezas cambian mucho durante iteraciones.  
**Para qué:** reducir errores silenciosos cuando refactorices.  
**Cómo:** prueba métricas y thresholding con escenarios sintéticos pequeños.

## Entregables
- baseline funcional
- modelo boosting funcional
- comparación clara entre ambos
- threshold inicial de negocio
- explainability básica documentada
- más pruebas unitarias

## Checklist
- [ ] Implementar paquete de métricas.
- [ ] Implementar utilidades de entrenamiento.
- [ ] Entrenar baseline y documentarlo.
- [ ] Entrenar modelo boosting y compararlo.
- [ ] Implementar thresholding de negocio.
- [ ] Documentar explainability y segmentos.
- [ ] Escribir tests para métricas y thresholding.

## Criterio de salida
Tienes un modelo defendible, sabes compararlo con baseline y puedes convertir el score en una acción de portafolio razonable.

---

# Semana 5 — Pipelines, MLflow y batch scoring

## Objetivo general
Pasar de notebooks/experimentos sueltos a flujos reproducibles con tracking y salida utilizable.

## Qué vas a trabajar
- pipeline de entrenamiento
- integración con MLflow
- registro de modelo
- scoring batch reproducible
- model card
- pruebas de integración iniciales

## Archivos foco
- `src/pipelines/training_pipeline.py`
- `scripts/run_train.py`
- `src/training/train_utils.py`
- `scripts/register_model.py`
- `docs/model_card_template.md`
- `src/inference/batch_scoring.py`
- `src/pipelines/scoring_pipeline.py`
- `scripts/run_score.py`
- `tests/integration/`
- `tests/fixtures/`

## Qué hacer
### A. Construir el training pipeline
**Qué:** encapsular el flujo de entrenamiento en una sola orquestación local.  
**Por qué:** reduce dependencia de notebooks y mejora reproducibilidad.  
**Para qué:** ejecutar entrenamiento end-to-end con un comando claro.  
**Cómo:** carga features, genera splits, entrena, evalúa y selecciona mejor candidato.

### B. Integrar MLflow
**Qué:** registrar parámetros, métricas y artefactos.  
**Por qué:** convierte experimentación dispersa en proceso trazable.  
**Para qué:** demostrar MLOps serio dentro del portfolio.  
**Cómo:** agrega logging de params, metrics y artifacts en el pipeline.

### C. Registrar modelo y documentarlo
**Qué:** dejar evidencia formal del mejor candidato.  
**Por qué:** un modelo sin registro es difícil de mantener.  
**Para qué:** mostrar lifecycle básico del modelo.  
**Cómo:** implementa `scripts/register_model.py` y llena una model card real.

### D. Implementar batch scoring
**Qué:** usar el modelo activo para predecir sobre nueva población.  
**Por qué:** demuestra paso a uso operativo.  
**Para qué:** mostrar que el proyecto no se queda solo en evaluación offline.  
**Cómo:** carga modelo, prepara input, calcula score y guarda resultados.

### E. Añadir integration tests básicos
**Qué:** validar flujos completos pequeños.  
**Por qué:** detectan roturas entre módulos.  
**Para qué:** mejorar mantenibilidad.  
**Cómo:** usa fixtures sintéticos y prueba training/scoring o al menos imports y healthchecks.

## Entregables
- training pipeline funcional
- MLflow registrando corridas
- primer modelo registrado
- batch scoring funcional
- model card inicial
- primeras pruebas de integración

## Checklist
- [ ] Implementar `training_pipeline.py`.
- [ ] Hacer funcional `scripts/run_train.py`.
- [ ] Integrar MLflow en entrenamiento.
- [ ] Registrar parámetros, métricas y artefactos.
- [ ] Implementar `scripts/register_model.py`.
- [ ] Implementar batch scoring.
- [ ] Implementar `scoring_pipeline.py`.
- [ ] Hacer funcional `scripts/run_score.py`.
- [ ] Llenar model card con un modelo real.
- [ ] Añadir pruebas de integración iniciales.

## Criterio de salida
Puedes correr entrenamiento y scoring con scripts claros, con trazabilidad en MLflow y al menos algunos tests de integración validando comportamiento esperado.

---

# Semana 6 — Airflow, monitoreo, drift, API y polish final

## Objetivo general
Conectar la plataforma en workflows automatizados, añadir monitoreo básico y dejar el repo listo para mostrarse.

## Qué vas a trabajar
- conexión real de DAGs
- drift y alertas
- monitoring pipeline
- API mínima
- pruebas finales
- documentación de cierre

## Archivos foco
- `airflow/dags/data_ingestion_dag.py`
- `airflow/dags/data_preparation_dag.py`
- `airflow/dags/training_dag.py`
- `airflow/dags/scoring_dag.py`
- `airflow/dags/monitoring_dag.py`
- `src/monitoring/drift.py`
- `quality/evidently/drift_config_placeholder.yaml`
- `src/monitoring/alerts.py`
- `src/pipelines/monitoring_pipeline.py`
- `scripts/generate_reports.py`
- `api/schemas.py`
- `api/model_loader.py`
- `src/inference/predict_service.py`
- `api/app.py`
- `tests/unit/`
- `tests/integration/`
- `docs/governance.md`
- `docs/architecture.md`
- `docs/testing_strategy.md`
- `README.md`

## Qué hacer
### A. Conectar DAGs a lógica real
**Qué:** reemplazar placeholders por llamadas a funciones reales.  
**Por qué:** el valor de Airflow está en orquestar flujos reales.  
**Para qué:** cerrar el ciclo ingestión → preparación → entrenamiento → scoring → monitoreo.  
**Cómo:** importa funciones desde `src/` o `scripts/` y mantén la lógica pesada fuera del archivo DAG.

### B. Implementar drift y alertas
**Qué:** medir si cambian datos o scores respecto a una referencia.  
**Por qué:** muestra madurez técnica sobre el lifecycle del modelo.  
**Para qué:** demostrar que piensas en estabilidad, no solo en entrenamiento.  
**Cómo:** compara datasets, calcula drift por feature y define umbrales simples.

### C. Crear el monitoring pipeline
**Qué:** consolidar calidad + drift + alertas.  
**Por qué:** el monitoreo disperso comunica menos valor.  
**Para qué:** mostrar una estrategia coherente de observabilidad.  
**Cómo:** ejecuta checks, reportes y reglas en un solo pipeline.

### D. Exponer una API mínima
**Qué:** definir un contrato básico de inferencia.  
**Por qué:** suma valor curricular incluso si el caso principal es batch.  
**Para qué:** demostrar skills de serving y separación de responsabilidades.  
**Cómo:** implementa schemas, model loader, predict service y endpoints simples.

### E. Completar tests y documentación final
**Qué:** cerrar el proyecto de forma mantenible y fácil de revisar.  
**Por qué:** un repo fuerte no solo funciona; también explica cómo mantenerlo.  
**Para qué:** maximizar su valor como pieza de portafolio.  
**Cómo:** añade tests finales, actualiza docs y pule el README con resultados.

## Entregables
- DAGs conectados
- drift report básico
- reglas iniciales de alerta
- API mínima funcional
- tests unitarios e integración básicos
- documentación final robusta

## Checklist
- [ ] Conectar `data_ingestion_dag.py`.
- [ ] Conectar `data_preparation_dag.py`.
- [ ] Conectar `training_dag.py`.
- [ ] Conectar `scoring_dag.py`.
- [ ] Conectar `monitoring_dag.py`.
- [ ] Implementar `src/monitoring/drift.py`.
- [ ] Configurar `quality/evidently/drift_config_placeholder.yaml`.
- [ ] Implementar `src/monitoring/alerts.py`.
- [ ] Implementar `src/pipelines/monitoring_pipeline.py`.
- [ ] Implementar `scripts/generate_reports.py`.
- [ ] Implementar API mínima funcional.
- [ ] Escribir tests unitarios y de integración básicos.
- [ ] Actualizar `docs/governance.md` y `docs/architecture.md`.
- [ ] Hacer polish final del `README.md`.

## Criterio de salida
El proyecto ya comunica una solución end-to-end coherente, mantenible y demostrable: datos → features → entrenamiento → tracking → scoring → monitoreo → documentación → tests.
