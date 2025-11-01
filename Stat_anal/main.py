from part1 import *
from part2 import *
from part3 import *
from part4 import *

def main():
    a = -3
    sigma_sqrt = 9
    n = 125

    x, sigma = generate_sample(a, sigma_sqrt, n)  # генерируем один раз

    while True:
        n_task = input("Введите номер задания (1–4) или 0 для выхода: ").strip()

        if n_task == "0":
            print("Программа завершена.")
            break

        if n_task not in {"1", "2", "3", "4"}:
            print("Попробуйте снова.\n")
            continue

        n_task = int(n_task)

        if n_task == 1:
            show_x(x, sigma, n)

        elif n_task == 2:
            k = sturges_bins(n)
            hist_relative_freq_x(x)
            hist_abs_freq(x, k, a, sigma)
            hist_with_theoretical_line(x, k, a, sigma)
            empirical_function(x, a, k, sigma, n)
            box_plot_x(x, a, k, sigma)

        elif n_task == 3:
            mean_m = mean_manual(x, n)
            print("Выборочное среднее (ручной расчет):", mean_m)

            median_ = median(x, n)
            print("Медиана (ручной расчет):", median_)

            mode_ = mode(x)
            print("Мода (ручной расчет):", mode_)

            variance_, variance_corr = variance(x, n)
            print("Дисперсия:", variance_)
            print("Исправленная дисперсия:", variance_corr)

            std_, std_corr = std_manual(x, n)
            print("Стандартное отклонение:", std_)
            print("Исправленное стандартное отклонение:", std_corr)

            skew_ = skewness(x, n)
            print("Коэффициент асимметрии:", skew_)

            kurtosis_ = kurtosis(x, n)
            print("Эксцесс:", kurtosis_, "\n")

            automatic_x(x, n)

        elif n_task == 4:
            y = generate(n)
            show_y(y)
            hist_relative_freq_y(y)
            box_plot_y(y)
            automatic_y(y)

if __name__ == "__main__":
    main()
