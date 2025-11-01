import numpy as np

def generate_sample(a: float, sigma_sq: float, n: int):
    """Генерирует выборку X ~ N(a, sigma^2) и возвращает массив x и sigma."""
    sigma = np.sqrt(sigma_sq)
    np.random.seed(42)
    x = np.random.normal(loc=a, scale=sigma, size=n)
    return x, sigma

def sturges_bins(n: int) -> int:
    """Возвращает число интервалов по правилу Стерджеса."""
    return int(np.ceil(1 + np.log2(n)))

def absolute_frequencies(x: np.ndarray, k: int):
    """Возвращает массив абсолютных частот и границы интервалов."""
    abs_freq, borders = np.histogram(x, bins=k)
    return abs_freq, borders

def relative_frequencies(abs_freq: np.ndarray, n: int):
    """Возвращает массив относительных частот и их сумму."""
    rel_freq = abs_freq / n
    return rel_freq, rel_freq.sum()


def show_x(a: float, sigma_sq: float, n: int):
    """
    Генерирует выборку, вычисляет все показатели
    и выводит подробный отчёт.
    """
    x, sigma = generate_sample(a, sigma_sq, n)
    print("=== ОТЧЁТ ПО ВЫБОРКЕ ===")
    print(f"Параметры распределения: a = {a}, sigma^2 = {sigma_sq}, n = {n}")
    print(f"Фактическое sigma: {sigma:.4f}\n")
    print("Первые 10 элементов выборки:", x[:10], "\n")

    k = sturges_bins(n)
    print(f"Число интервалов (Стерджес): {k}\n")

    abs_freq, borders = absolute_frequencies(x, k)
    print("Абсолютные частоты:", abs_freq)
    print("Границы интервалов:", borders, "\n")
    print("Сумма абсолютных частот:", abs_freq.sum(), "\n")

    rel_freq, rel_sum = relative_frequencies(abs_freq, n)
    print("Относительные частоты:", rel_freq)
    print("Сумма относительных частот:", rel_sum, "\n")
