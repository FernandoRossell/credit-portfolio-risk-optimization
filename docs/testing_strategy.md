# Estrategia de testing y mantenibilidad

## Objetivo
Asegurar que el proyecto pueda crecer, modificarse y refactorizarse sin romper el comportamiento esperado.

## Tipos de pruebas
### Unit tests
Funciones pequeñas y determinísticas.

### Integration tests
Validan colaboración entre módulos.

### Data quality checks
Complementan el testeo tradicional para proteger el pipeline.

## Qué probar primero
1. configuración
2. paths e I/O
3. métricas
4. thresholding
5. features clave
6. healthcheck de API

## Regla práctica
Cada cambio relevante en utilidades, features, evaluación, inferencia o monitoreo debería acompañarse de al menos una prueba nueva o actualizada.
