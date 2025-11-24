# Calculadora de Distribución Normal

Aplicación de consola en Python que ayuda a resolver problemas de probabilidad
para la distribución normal. No usa gráficos, solo texto explicativo y los
resultados de cada cálculo.

## Requisitos
- Python 3.9 o superior.

## Cómo ejecutar
```bash
python main.py
```
Sigue el menú interactivo para escoger el cálculo dentro de la distribución normal.

## Funcionalidades
- **Normal**: densidad en un punto, probabilidad acumulada y probabilidad entre
dos valores usando Φ(b) - Φ(a).

## Manejo de errores
- Validaciones para que σ sea positiva.
- Mensajes claros que piden reingresar los datos cuando el formato no es numérico.

## Referencia rápida de fórmulas
Las funciones en `main.py` documentan las fórmulas empleadas para la densidad,
la acumulada y la probabilidad entre dos valores, facilitando la revisión
teórica durante la presentación.
