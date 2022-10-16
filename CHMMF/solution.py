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


def eyler(u_0, t, n, h):
    y = [u_0]
    for i in range(n):
        y.append(y[i] + h * func(y[i], t[i]))
    return y


def runge_kutta(u_0, t, n, h):
    y = [u_0]
    for i in range(n):
        y_1 = func(y[i], t[i])
        y_2 = func(y[i] + 0.5 * h * y_1, t[i] + 0.5 * h)
        y_3 = func(y[i] + 0.5 * h * y_2, t[i] + 0.5 * h)
        y_4 = func(y[i] + h * y_3, t[i] + h)
        y.append(y[i] + h / 6 * (y_1 + 2 * y_2 + 2 * y_3 + y_4))
    return y


def predictor_corr(u_0, t, n, h):
    y = [u_0]
    for i in range(n):
        y_old = (y[i] + h * func(y[i], t[i]))
        y_new = y[i] + h / 2 * (func(y[i], t[i]) + func(y_old, t[i + 1]))
        y.append(y_new)
    return y


def succ_appr(u_0, t, n, h, e):
    y = [u_0]
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


def newton(u_0, t, n, h, e):
    y = [u_0]
    s_max = 0
    for i in range(n):
        s = 0
        x = y[i]
        ksi = e + 1
        f_i = func(y[i], t[i])
        while ksi > e and s <= 100:
            f_s = func(x, t[i + 1])
            x_1 = x - (x - y[i] - h / 2 * (f_i + f_s)) / (1 - h / 2 * (-2))
            ksi = abs(x_1 - x)
            x = x_1
            s += 1
        if s > 100:
            break
        y.append(x)
        s_max = max(s, s_max)
    return y, s_max


def switcher(k, u_0, t, n, h, i, e):
    if k == 1:
        print(f"Точное решение при N = {n[i]}")
        return exact(u_0, t, n[i]), 1
    elif k == 2:
        print(f"Схема Эйлера при N = {n[i]}")
        return eyler(u_0, t, n[i], h), 1
    elif k == 3:
        print(f"Схема Рунге-Кутта при N = {n[i]}")
        return runge_kutta(u_0, t, n[i], h), 1
    elif k == 4:
        print(f"Схема «предиктор-корректор» при N = {n[i]}")
        return predictor_corr(u_0, t, n[i], h), 1
    elif k == 5:
        print(f"Метод последовательных приближений при N = {n[i]}")
        y, s_max = succ_appr(u_0, t, n[i], h, e)
        print("s_max = ", s_max)
        return y, s_max
    elif k == 6:
        print(f"Метод Ньютона при N = {n[i]}")
        y, s_max = newton(u_0, t, n[i], h, e)
        print("s_max = ", s_max)
        return y, s_max
    else:
        print('Ошибка, введите одно из чисел: 1, 2, 3, 4, 5, 6')
        exit(-1)


def t_list(t_0, t_n, n):
    t = [t_0]
    h = (t_n - t_0) / n
    for i in range(n):
        t.append(t[i] + h)
    return h, t


def out_exact(n, t_0, u_0, t_n):
    n = int(n[0])
    fig, ax = plt.subplots(1, 1, figsize=(7, 5))
    h, t = t_list(t_0, t_n, n)
    u = exact(u_0, t, n)
    ax.set_xlabel('t', fontsize=15)
    ax.set_ylabel('U', fontsize=15, rotation=0)
    ax.scatter(t, u, color='blue', label="точное решение", s=5)
    ax.legend(prop={"size": 16}, loc=2)
    print(tabulate({"t": t, "U": u}, headers='keys',
                   tablefmt="psql", numalign="center", floatfmt=('.2f', '.12f')))
    plt.show()


def test(k, n, t_0, u_0, t_n, e):
    if len(n) == 1:
        fig, axes = plt.subplots(1, 1, figsize=(7, 5))
    else:
        fig, axes = plt.subplots(round(len(n) / 2), 2, figsize=(14, 5))
    h_list, err_max_list, k_list = [], [], []
    for j in range(len(n)):
        h, t = t_list(t_0, t_n, n[j])
        err = []
        err_max = 0
        y, s_max = switcher(k, u_0, t, n, h, j, e)
        u = exact(u_0, t, n[j])

        for i in range(n[j] + 1):
            err.append(abs(u[i] - y[i]))
            if err[i] > err_max:
                err_max = err[i]
        if n[j] <= 100:
            print(tabulate({"t": t, "U": u, "Y": y, "Error": err}, headers='keys',
                           tablefmt="psql", numalign="center", floatfmt=('.2f', '.12f', '.12f', '.12f')))
        print("h = ", h)
        h_list.append(h)
        print('err_1_max = ', f"{err_max:.15f}")
        err_max_list.append(err_max)
        print('K = ', f"{err_max / h:.5}", '\n')
        k_list.append(err_max / h)
        if len(n) == 1:
            ax = axes
        else:
            ax = axes.flat[j]
        ax.set_xlabel('t', fontsize=15)
        ax.set_ylabel('U', fontsize=15, rotation=0)
        ax.plot(t, y, linestyle='solid', color='orange', label="приближённое решение")
        ax.scatter(t, u, color='blue', label="точное решение", s=5)
        ax.legend(prop={"size": 16}, loc=2)
    print(tabulate({"h": h_list, "Psi": err_max_list, "K": k_list}, headers='keys',
                   tablefmt="psql", numalign="center", ))
    plt.show()

    if len(n) > 1:  # Сходимость
        fig2, ax1 = plt.subplots(1, 1, figsize=(7, 5))
        ax1.set_xlabel('h', fontsize=15)
        ax1.set_ylabel(r"$\psi$", fontsize=15, rotation=0)
        ax1.semilogy()
        ax1.semilogx()
        ax1.grid(which='major')
        ax1.grid(which='minor', linestyle=':')
        ax1.invert_xaxis()
        ax1.plot(h_list, err_max_list, linestyle='solid', color='red', )
        plt.show()
    else:
        n_1 = n[0]
        h, t = t_list(t_0, t_n, n_1)
        y = switcher(k, u_0, t, n, h, 0, e)
        if k == 2 or k == 3 or k == 4:  # Устойчивость
            delta = [-0.1, -0.05, 0, 0.05, 0.1]
            x = []
            for d in delta:
                u_0_changed = u_0 + d
                y_changed, s_max = switcher(k, u_0_changed, t, n, h, 0, e), 1
                x.append(abs(y_changed[n_1 - 1] - y[n_1 - 1]))
            print(tabulate({"delta": delta, "Chi": x}, headers='keys',
                           tablefmt="psql", numalign="center", ))
            fig3, ax2 = plt.subplots(1, 1, figsize=(7, 5))
            ax2.set_xlabel(r"$\delta$", fontsize=15)
            ax2.set_ylabel(r"$\chi$", fontsize=15, rotation=0)
            ax2.plot(delta, x, linestyle='solid', color='blue')
            plt.show()
        else:
            e_list = [1, 0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001]  # Сходимость итерационных
            nums = [1, 2, 3, 4, 5, 6, 7]
            psi, s_max_list = [], []
            u_shod = exact(u_0, t, n_1)
            for e_i in e_list:
                err_max_ust = 0
                y_shod, s_max_ust = switcher(k, u_0, t, n, h, 0, e_i)
                for i in range(n_1 + 1):
                    err_shod = abs(u_shod[i] - y_shod[i])
                    if err_shod > err_max_ust:
                        err_max_ust = err_shod
                psi.append(err_max_ust)
                s_max_list.append(s_max_ust)

            print(tabulate({"№": nums, "Epsilon": e_list, "Psi": psi, "L": s_max_list}, headers='keys',
                           tablefmt="psql", numalign="center", ))
            fig3, ax2 = plt.subplots(1, 1, figsize=(7, 5))
            ax2.semilogx()
            ax2.grid(which='major')
            ax2.grid(which='minor', linestyle=':')
            ax2.set_xlabel(r"$\epsilon$", fontsize=15)
            ax2.set_ylabel("L", fontsize=15, rotation=0)
            ax2.plot(e_list, s_max_list, linestyle='solid', color='red')
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
    n = list()
    r = int(input("Режим \"Тест\": r = 1\nРежим \"Сход\": r = 2\nПроизвольные данные: r = 3\nВведите r = "))
    if r not in {1, 2, 3}:
        try:
            raise Exception("Ошибка: ввведено недопустимое значение r")
        except Exception as err:
            print(str(err))
            exit()
    if r == 1:
        t_0 = 0
        u_0 = 0
        t_n = 3
    elif r == 2:
        t_0 = -1
        u_0 = 1
        t_n = 0
    else:
        t_0 = float(input("Введите t0 = "))
        u_0 = float(input("Введите U0 = "))
        t_n = float(input("Введите T = "))
    [n.append(int(j)) for j in input("Введите N = ").split()]
    e = 1
    if k == 5 or k == 6:
        e = float(input("Введите e = "))
    print("t0 = ", t_0)
    print("U0 = ", u_0)
    print("T = ", t_n)
    print("N = ", n)
    if k == 1:
        out_exact(n, t_0, u_0, t_n)
    else:
        test(k, n, t_0, u_0, t_n, e)


if __name__ == "__main__":
    main()
