# Arquitectura del proyecto

## Resumen
Arquitectura por capas para separar ingestión, calidad, procesamiento, features, entrenamiento, serving y monitoreo.

## Capas
1. Fuente de datos local (`data/raw/`)
2. Raw layer
3. Quality layer
4. Processing layer
5. Feature layer
6. Training & registry
7. Serving batch/API
8. Monitoring

## Principios
- sin licencias empresariales
- sin subir raw data al repo
- lógica pesada fuera de DAGs
- testing y documentación desde el diseño
