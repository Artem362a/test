import numpy as np
from scipy import stats
import pandas as pd
from collections import Counter

def mean_manual(x, n):
    result = sum(x)/n
    return result


def median(x, n):
    x_sorted = sorted(x)
    if n%2 == 0:
        median_manual = (x_sorted[n//2 - 1]+x_sorted[n//2])/2

    else:
        median_manual = x_sorted[n//2]

    return median_manual


def mode(x):
    counts = Counter(np.round(x,2))
    mode_manual = counts.most_common(1)[0][0]
    return mode_manual


def variance(x, n):
    mean_m = mean_manual(x, n)
    variance_manual = sum((x - mean_m)**2)/n
    variance_corrected = sum((x - mean_m)**2)/ (n-1)
    return variance_manual, variance_corrected

def std_manual(x, n,):
    variance_manual, variance_corrected = variance(x,n)
    std_manual = np.sqrt(variance_manual)
    std_corrected = np.sqrt(variance_corrected)
    return std_manual, std_corrected

def skewness(x, n):
    mean_m  = mean_manual(x, n)
    variance_m = variance_manual = sum((x - mean_m)**2)/n
    skew = sum((x - mean_m)**3)/n /(variance_m**1.5)
    return skew

def kurtosis(x, n):
    mean_m = mean_manual(x, n)
    variance_m = variance_manual = sum((x - mean_m) ** 2) / n
    kurt = sum((x - mean_m)**4)/n /(variance_m**2) - 3
    return kurt



def automatic_x(x, n):
    mean_np = np.mean(x)
    median_np = np.median(x)
    mode_np = stats.mode(np.round(x, 2)) # округляем, чтобы мода совпадала
    variance_np = np.var(x)  # несмещённая по умолчанию
    variance_corrected_np = np.var(x, ddof=1)  # исправленная
    std_np = np.std(x)
    std_corrected_np = np.std(x, ddof=1)
    skew_np = stats.skew(x)
    kurt_np = stats.kurtosis(x)  # эксцесс

    df = pd.DataFrame(x, columns=["X"])
    describe_df = df.describe()

    print("Среднее (NumPy):", mean_np)
    print("Медиана (NumPy):", median_np)
    print("Мода (SciPy):", mode_np)
    print("Дисперсия (NumPy):", variance_np)
    print("Исправленная дисперсия (NumPy):", variance_corrected_np)
    print("Стандартное отклонение (NumPy):", std_np)
    print("Исправленное стандартное отклонение (NumPy):", std_corrected_np)
    print("Асимметрия (SciPy):", skew_np)
    print("Эксцесс (SciPy):", kurt_np)