import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns


a = -3
sigma = 9
n = 30
N = 1000

np.random.seed(362)
samples = np.random.normal(loc=a, scale=sigma, size=(N, n))

#Вычисление выборочной дисперсии
D_v = np.var(samples, axis=1, ddof=0)  # ddof=0 для выборочной дисперсии
