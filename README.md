# Credit Portfolio Risk & Profit Optimization


**Caso de negocio:** From Credit Risk Modeling to Profit-Driven Decision Making

**Stack:** 

**Autor:** Abel Soto

---

## Visión general

En la banca minorista, las decisiones de aprobación de crédito suelen basarse exclusivamente en métricas de riesgo como la probabilidad de default. Sin embargo, esta aproximación ignora un aspecto crítico: **la rentabilidad esperada del portafolio**.

Este proyecto propone un **framework analítico de extremo a extremo** para optimizar decisiones de crédito, balanceando riesgo y retorno económico. El enfoque combina **machine learning, métricas financieras y simulación de políticas**, con el objetivo de maximizar el beneficio esperado bajo restricciones de riesgo.

El caso está diseñado para replicar desafíos reales enfrentados por equipos senior de analytics en instituciones financieras.

---

## Objetivos del proyecto

- Estimar la **Probability of Default (PD)** a nivel cliente utilizando modelos estadísticos y de machine learning, estableciendo un baseline interpretable y modelos no lineales avanzados.
- Calcular métricas financieras clave como:
  - Expected Loss (EL)
  - Expected Profit
- Diseñar y comparar **políticas de aprobación de crédito**:
  - Basadas exclusivamente en riesgo (PD)
  - Basadas en rentabilidad esperada del cliente y del portafolio
- Evaluar el impacto de dichas políticas sobre indicadores clave de negocio:
  - Approval rate
  - Default rate
  - Profit esperado del portafolio
- Implementar y evaluar **modelos de mayor complejidad** (por ejemplo, Support Vector Machines y Redes Neuronales) como modelos *challenger*, comparándolos contra enfoques tradicionales en términos de:
  - Performance predictiva
  - Calibración de probabilidades
  - Estabilidad temporal
  - Explicabilidad y gobernanza
- Justificar la **selección final del modelo** priorizando soluciones más simples y robustas cuando estas ofrecen un mejor balance entre desempeño, interpretabilidad y viabilidad operativa.
- Simular escenarios adversos y realizar stress testing para analizar la **robustez del sistema de decisión crediticia** bajo cambios macroeconómicos.
- Traducir resultados técnicos en **insights accionables para toma de decisiones ejecutivas**, enfocados en impacto económico y control de riesgo.

---

## Fuente de los datos

### Dataset principal

El proyecto utiliza el **Home Credit Default Risk Dataset**, un dataset público ampliamente usado para problemas de credit scoring.

- **Proveedor:** Home Credit Group  
- **Plataforma:** Kaggle  
- **Tipo de problema:** Clasificación binaria (default / no default)

El dataset incluye información como:
- Datos demográficos
- Ingresos
- Historial crediticio
- Comportamiento financiero

### Variables adicionales (sintéticas)

Para habilitar el análisis económico, se generan variables adicionales bajo supuestos realistas:

- Monto del crédito
- Tasa de interés
- Plazo del préstamo
- Loss Given Default (LGD)

> Estas variables sintéticas están documentadas y se utilizan exclusivamente para simular un entorno de decisión financiera realista.

---

## Enfoque analítico

### Modelado de riesgo crediticio
- Modelo baseline: Regresión logística
- Modelo principal: Gradient Boosting (XGBoost)
- Métricas de evaluación:
  - ROC-AUC
  - KS statistic
  - Calibration curves
- Interpretabilidad:
  - Feature importance
  - SHAP values

---

### Métricas financieras

Para cada solicitud de crédito se estiman:

- **Expected Loss (EL):**

\[
EL = PD \times LGD \times Exposure
\]

- **Expected Profit:**

\[
Expected\ Profit = Interest\ Income - Expected\ Loss
\]

Estas métricas permiten evaluar decisiones desde una perspectiva económica y no únicamente desde el riesgo.

---

### Políticas de aprobación

Se comparan distintas estrategias de decisión:

- Cut-off fijo por PD
- Cut-off basado en profit esperado
- Políticas segmentadas por perfil de cliente

Cada política es evaluada utilizando indicadores de negocio a nivel portafolio.

---

## Testing & Validación
*(Sección a completar)*

-  
-  
-  

---

## Análisis de Hot Spots del programa
*(Sección a completar)*

-  
-  
-  

---

## Supuestos asumidos
*(Sección a completar)*

-  
-  
-  

---

## ¿Dónde se rompen los supuestos?
*(Sección a completar)*

-  
-  
-  

---

## Posible implementación en producción
*(Sección a completar)*

**Arquitectura propuesta**
-  
-  
-  

**Consideraciones operativas**
-  
-  
-  

---

## Resultados esperados

El enfoque orientado a rentabilidad permite:

- Mejorar el profit esperado del portafolio
- Reducir rechazos innecesarios
- Controlar el riesgo bajo límites definidos
- Habilitar decisiones crediticias más informadas y explicables

> Los resultados finales dependen de los escenarios y parámetros simulados.

---

## Extensiones futuras

- Pricing dinámico basado en riesgo
- Modelado dinámico de EAD
- Análisis de fairness y bias
- Integración de aceptación del cliente (take-up rate)

---

## Conclusión

Este proyecto demuestra cómo un sistema tradicional de credit scoring puede evolucionar hacia un **motor de decisión financiera orientado a valor**, integrando análisis predictivo, métricas económicas y criterio de negocio.

El foco no está en maximizar métricas técnicas, sino en **optimizar decisiones reales con impacto económico**, reflejando el trabajo esperado de perfiles senior en analytics para banca.

---