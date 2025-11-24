"""Calculadora de distribución normal por consola.

El programa solicita los datos al usuario, calcula los resultados aplicando las
fórmulas estándar y explica brevemente cada paso. Se evita el uso de gráficos
para cumplir con la pauta y mantener el enfoque en los cálculos y su
interpretación textual.
"""
from math import erf, exp, pi, sqrt


def pdf_normal(x: float, mean: float, std_dev: float) -> float:
    """Calcula la densidad f(x) de una N(μ, σ).

    Fórmula: f(x) = (1 / (σ * sqrt(2π))) * exp(-0.5 * ((x - μ)/σ)^2)
    """

    if std_dev <= 0:
        raise ValueError("La desviación estándar debe ser positiva.")
    coefficient = 1 / (std_dev * sqrt(2 * pi))
    exponent = exp(-0.5 * ((x - mean) / std_dev) ** 2)
    return coefficient * exponent


def cdf_normal(x: float, mean: float, std_dev: float) -> float:
    """Calcula la probabilidad acumulada Φ(x).

    Fórmula: Φ(x) = 0.5 * [1 + erf((x-μ)/(σ*sqrt(2)))]
    """

    if std_dev <= 0:
        raise ValueError("La desviación estándar debe ser positiva.")
    z = (x - mean) / (std_dev * sqrt(2))
    return 0.5 * (1 + erf(z))


def probability_between(a: float, b: float, mean: float, std_dev: float) -> float:
    """Calcula P(a <= X <= b) = Φ(b) - Φ(a) para una N(μ, σ)."""

    lower, upper = sorted([a, b])
    return cdf_normal(upper, mean, std_dev) - cdf_normal(lower, mean, std_dev)


def prompt_float(message: str) -> float:
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("⚠️  Ingresa un número válido.")


def normal_menu() -> None:
    print("\n--- Distribución Normal ---")
    mean = prompt_float("Ingresa la media (μ): ")
    std_dev = prompt_float("Ingresa la desviación estándar (σ>0): ")

    print("\n¿Qué deseas calcular?")
    print("1) Densidad en un valor x")
    print("2) Probabilidad acumulada P(X <= x)")
    print("3) Probabilidad entre dos valores P(a <= X <= b)")

    choice = input("Opción: ")
    try:
        if choice == "1":
            x = prompt_float("Valor de x: ")
            result = pdf_normal(x, mean, std_dev)
            print(
                f"f({x}) = {result:.6f}\n"
                "Fórmula: f(x) = 1/(σ*sqrt(2π)) * exp(-0.5*((x-μ)/σ)^2)"
            )
        elif choice == "2":
            x = prompt_float("Valor de x: ")
            result = cdf_normal(x, mean, std_dev)
            print(
                f"P(X <= {x}) = {result:.6f}\n"
                "Fórmula: Φ(x) = 0.5 * [1 + erf((x-μ)/(σ*sqrt(2)))]"
            )
        elif choice == "3":
            a = prompt_float("Valor inferior a: ")
            b = prompt_float("Valor superior b: ")
            result = probability_between(a, b, mean, std_dev)
            print(
                f"P({a} <= X <= {b}) = {result:.6f}\n"
                "Fórmula: Φ(b) - Φ(a), usando la relación con la función error"
            )
        else:
            print("Opción no reconocida.")
    except ValueError as exc:
        print(f"Error: {exc}")


def main() -> None:
    print("Calculadora de Distribución Normal")
    while True:
        print("\nSelecciona una opción:")
        print("1) Distribución normal")
        print("2) Salir")

        choice = input("Opción: ")
        if choice == "1":
            normal_menu()
        elif choice == "2":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no reconocida, intenta nuevamente.")


if __name__ == "__main__":
    main()
