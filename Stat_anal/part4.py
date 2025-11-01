import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import triang
import seaborn as sns
from scipy import stats

MODE = 3
LEFT = 2
RIGHT = 5




def generate(n):
    np.random.seed(42)
    y = np.random.triangular(left = 2, mode = 3, right = 5, size = n)
    return y

def show_y(y):
    print("Случайная величина Y:", y)


def hist_relative_freq_y(y):
    plt.figure(figsize = (8,5))
    count, bins, ignored = plt.hist(y, bins = 10,density = True, alpha = 0.6, color = 'lightblue', edgecolor = 'black', label= 'Эмпирическая гистограмма')
    C = (MODE - LEFT) / (RIGHT - LEFT)
    x_line = np.linspace(LEFT, RIGHT, 200)
    pdf = triang.pdf(x_line,c=C,loc = LEFT,scale = RIGHT- LEFT)
    plt.plot(x_line, pdf,'r-',lw = 2,label='Теоретическая кривая Y')

    plt.title("Гистограмма относительных частот Y с теоретической кривой")
    plt.xlabel("Y")
    plt.ylabel("Относительная частота")
    plt.legend()
    plt.show()


def box_plot_y(y):
    plt.figure(figsize = (6,5))
    sns.boxplot(x = y, color = 'lightblue')
    plt.title("Бокс-плот Y")
    plt.show()

    Q1 = np.percentile(y, 25)
    Q2 = np.percentile(y, 50)  # медиана
    Q3 = np.percentile(y, 75)
    IQR = Q3 - Q1
    whisker_low = Q1 - 1.5 * IQR
    whisker_high = Q3 + 1.5 * IQR

    print(f"Q1 (25%) = {Q1:.3f}")
    print(f"Q2 (50%) = {Q2:.3f}")
    print(f"Q3 (75%) = {Q3:.3f}")
    print(f"Интерквартильный размах IQR = {IQR:.3f}")
    print(f"Границы усов: нижняя = {whisker_low:.3f}, верхняя = {whisker_high:.3f}")


def automatic_y(y):
    mean_y = np.mean(y)
    median_y = np.median(y)
    mode_y = stats.mode(np.round(y, 2))

    variance_y = np.var(y)
    variance_corrected_y = np.var(y, ddof=1)

    std_y = np.std(y)
    std_corrected_y = np.std(y, ddof=1)

    skew_y = stats.skew(y)
    kurt_y = stats.kurtosis(y)


    print("Среднее (NumPy):", mean_y)
    print("Медиана (NumPy):", median_y)
    print("Мода (SciPy):", mode_y)
    print("Дисперсия (NumPy):", variance_y)
    print("Исправленная дисперсия (NumPy):", variance_corrected_y)
    print("Стандартное отклонение (NumPy):", std_y)
    print("Исправленное стандартное отклонение (NumPy):", std_corrected_y)
    print("Асимметрия (SciPy):", skew_y)
    print("Эксцесс (SciPy):", kurt_y)