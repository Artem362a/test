import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


def hist_relative_freq_x(x):
    plt.figure(figsize=(12,5))
    for bins in range(2,11):
        plt.hist(x, bins, density = True, alpha = 0.5, label = f'bins={bins}')
        plt.title("Гистограмма относительных частот(интервалы 2-10)")
        plt.xlabel("X")
        plt.ylabel("Relative Frequency")
        plt.legend()
        plt.show()

    plt.figure(figsize=(12, 5))
    for bins in range(15, 26):
        plt.hist(x, bins, density=True, alpha=0.5, label=f'bins={bins}')
        plt.title("Гистограммы относительных частот(интервалы 15-25)")
        plt.xlabel("X")
        plt.ylabel("Relative Frequency")
        plt.legend()
        plt.show()


def hist_abs_freq(x,k,a,sigma):

    plt.figure(figsize=(8,5))
    plt.hist(x, bins = k, edgecolor = 'black')
    plt.title("Гистограмма абсолютных частот:")
    plt.xlabel("X")
    plt.ylabel("Absolutely Frequency")
    plt.show()

def hist_with_theoretical_line(x,k,a,sigma):

    plt.figure(figsize=(8,5))
    count, bins, ignored = plt.hist(x, bins = k, density = True, alpha = 0.6,color = 'skyblue', edgecolor = 'black', label = 'Эмпирическая гистограмма' )

    x_line = np.linspace(min(x), max(x), 100)
    pdf = stats.norm.pdf(x_line, loc=a, scale=sigma)
    plt.plot(x_line, pdf, 'r-', lw = 2, label = 'Теоретическая кривая N(-1;16)')
    plt.title("Гистограмма относительных частот с теоретической кривой")
    plt.xlabel("X")
    plt.ylabel("Relative Frequency")
    plt.legend()
    plt.show()

def empirical_function(x,a,k,sigma,n):
    count,bins, = np.histogram(x, bins = k, density = True)
    relative_freq = count/ n
    cum_freq = np.cumsum(relative_freq)

    plt.figure(figsize=(8,5))
    plt.step(bins[1:], cum_freq, where='mid', label='Эмпирическая ФР')
    plt.xlabel('X')
    plt.ylabel('Вероятность')
    plt.legend('Эмпирическая функция распределения')
    plt.grid(True)

    x_line = np.linspace(min(x), max(x), 200)
    cdf = stats.norm.pdf(x_line, loc=a, scale=sigma)
    plt.plot(x_line,cdf, 'r-', lw=2,label='Теоретическая ФР N(-1;16)')
    plt.legend()
    plt.show()

def box_plot_x(x,a,k,sigma):
    plt.figure(figsize=(6,5))
    sns.boxplot(x = x, color = 'lightgreen')
    plt.title("Бокс-плот")
    plt.show()

    q1 = np.percentile(x, 25)
    q2 = np.percentile(x, 50)
    q3 = np.percentile(x, 75)
    i_q_r = q3 - q1
    whisker_low = q1 - 1.5 * i_q_r
    whisker_high = q3 + 1.5 * i_q_r

    print(f"Q1(25%) = {q1:.3f}\n")
    print(f"Q3(50%) = {q2:.3f}\n")
    print(f"Q3(75%) = {q3:.3f}\n")
    print(f"Интерквартильный размах = {i_q_r:.3f}\n")
    print(f"Границы усов: нижняя = {whisker_low:.3f}, верхняя = {whisker_high:.3f}\n")
