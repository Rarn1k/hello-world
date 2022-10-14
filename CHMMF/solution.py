from math import exp
from matplotlib import pyplot as plt
from tabulate import tabulate


def func(u, t):
    return -2 * u + 4 * t


def diff(t, c):
    return 2 * t - 1 + c / exp(2 * t)


def find_c(t0, u0):
    return exp(2 * t0) * (u0 - 2 * t0 + 1)


def exact(u_0, t, n):
    u = list()
    c = find_c(t[0], u_0)
    for i in range(n + 1):
        u.append(diff(t[i], c))
    return u


def out_exact():
    e = 1


def eyler(u_0, t, n, h):
    y = list()
    y.append(u_0)
    for i in range(n):
        y.append(y[i] + h * func(y[i], t[i]))
    return y


def predictor_corr(u_0, t, n, h):
    y = list()
    y.append(u_0)
    for i in range(n):
        y_old = (y[i] + h * func(y[i], t[i]))
        y.append(y[i] + h / 2 * (func(y[i], t[i]) + func(y_old, t[i + 1])))
    return y


def succ_appr(u0, t, n, h, e):
    y = list()
    y.append(u0)
    s_max = 0
    for i in range(n):
        s = 0
        y_old = y[i]
        ksi = e + 1
        while ksi > e:
            y_new = y[i] + h / 2 * (func(y[i], t[i]) + func(y_old, t[i + 1]))
            ksi = abs(y_new - y_old)
            y_old = y_new
            s += 1
        y.append(y_old)
        s_max = max(s, s_max)
    return y, s_max


def newton(u0, t, n, h, e):
    x = list()
    x.append(u0)
    s_max = 0
    for i in range(n):
        s = 0
        x_old = x[i]
        ksi = e + 1
        while ksi > e:
            x_new = x_old - func(x_old, t[i]) / (1 - h / 2 * (-2))
            ksi = abs(x_new - x_old)
            x_old = x_new
            s += 1
        x.append(x_old)
        s_max = max(s, s_max)
    return x, s_max


def switcher(k, u_0, t, n, h, i, e):
    if k == 1:
        return exact(u_0, t, n[i])
    elif k == 2:
        return eyler(u_0, t, n[i], h)
    elif k == 4:
        return predictor_corr(u_0, t, n[i], h)
    elif k == 5:
        y, s_max = succ_appr(u_0, t, n[i], h, e)
        print("s_max = ", s_max)
        return y
    elif k == 6:
        return newton(u_0, t, n[i], h, e)
    else:
        print('Ошибка, введите одно из чисел: 1, 2, 3, 4, 5, 6')


def convergence(k, n, t_0, u_0, t_n, e):
    if len(n) == 1:
        fig, axes = plt.subplots(1, 1)
    else:
        fig, axes = plt.subplots(round(len(n) / 2), 2)
    for j in range(len(n)):
        h = (t_n - t_0) / n[j]
        t, err = [t_0], []
        err_max = 0
        for i in range(n[j]):
            t.append(t[i] + h)
        y = switcher(k, u_0, t, n, h, j, e)
        u = exact(u_0, t, n[j])
        if len(n) == 1:
            ax = axes
        else:
            ax = axes.flat[j]
        ax.set_xlabel('t')
        ax.set_ylabel('U')
        if k == 1:
            print(tabulate({"t": t, "U": u}, headers='keys',
                           tablefmt="psql", numalign="center", floatfmt=('.2f', '.12f')))
        else:
            for i in range(n[j] + 1):
                err.append(abs(u[i] - y[i]))
                if err[i] > err_max:
                    err_max = err[i]

            if n[j] <= 100:
                print(tabulate({"t": t, "U": u, "Y": y, "Error": err}, headers='keys',
                               tablefmt="psql", numalign="center", floatfmt=('.2f', '.12f', '.12f', '.12f')))
            print("h = ", h)
            print('err_1_max = ', f"{err_max:.15f}")
            print('K = ', f"{err_max / h:.5}", '\n')

            ax.plot(t, y, linestyle='solid', color='orange', label="приближённое решение")
        ax.scatter(t, u, color='blue', label="точное решение", s=2)
        ax.set_title(f"N = {n[j]}")
        ax.legend()
    plt.show()


def main():
    k = int(input("Точное решение: k = 1\nСхема Эйлера: k = 2\nСхема Рунге-Кутта: k = 3\n"
                  "Схема «предиктор-корректор»: k = 4\nМетод последовательных приближений: k = 5\n"
                  "Метод Ньютона: k = 6\nВведите k = "))
    if k not in {1, 2, 3, 4, 5, 6}:
        try:
            raise Exception("Ошибка: ввведено недопустимое значение k")
        except Exception as err:
            print(str(err))
            exit()
    t_0 = float(input("Введите t0 = "))
    u_0 = float(input("Введите U0 = "))
    t_n = float(input("Введите T = "))
    n = list()
    [n.append(int(j)) for j in input("Введите N = ").split()]
    e = 1
    if k == 5:
        e = float(input("Введите e = "))
    convergence(k, n, t_0, u_0, t_n, e)


if __name__ == "__main__":
    main()
