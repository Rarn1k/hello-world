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


def two_subplots(t_1, u_1, y_1, t_2, u_2, y_2):
    ax1 = plt.subplot(1, 2, 1)
    plt.xlabel('t')
    plt.ylabel('U')
    ax1.plot(t_1, y_1, linestyle='solid', color='orange', label="приближённое решение")
    ax1.plot(t_1, u_1, linestyle='dotted', color='blue', label="точное решение", linewidth='2')
    ax1.legend()

    ax2 = plt.subplot(1, 2, 2)
    plt.xlabel('t')
    plt.ylabel('U')
    ax2.plot(t_2, y_2, linestyle='solid', color='orange', label="приближённое решение")
    ax2.plot(t_2, u_2, linestyle='dotted', color='blue', label="точное решение", linewidth='2')
    ax2.legend()
    plt.show()


def eyler(u_0, t, n, h):
    print("Метод Эйлера")
    y = list()
    y.append(u_0)
    for i in range(n):
        y.append(y[i] + h * func(y[i], t[i]))
    return y


def convergence(n, t_0, u_0, t_n):
    fig, axes = plt.subplots(round(len(n) / 2), 2)
    for j in range(len(n)):
        h = (t_n - t_0) / n[j]
        t, err = [t_0], []
        err_max = 0
        for i in range(n[j]):
            t.append(t[i] + h)
        y = eyler(u_0, t, n[j], h)
        u = exact(u_0, t, n[j])
        for i in range(n[j] + 1):
            err.append(abs(u[i] - y[i]))
            if err[i] > err_max:
                err_max = err[i]

        if n[j] <= 100:
            print(tabulate({"t": t, "U": u, "Y": y, "Error": err}, headers='keys',
                           tablefmt="psql", numalign="center", floatfmt=('.2f', '.12f', '.12f', '.12f')))

        print('\n')
        print("h = ", h)
        print('err_1_max = ', f"{err_max:.15f}")
        print('K = ', f"{err_max / h:.5}", '\n')

        ax = axes.flat[j]
        ax.set_xlabel('t')
        ax.set_ylabel('U')
        ax.plot(t, y, linestyle='solid', color='orange', label="приближённое решение")
        ax.plot(t, u, linestyle='dotted', color='blue', label="точное решение", linewidth='2')
        ax.legend()
    plt.show()


def main():
    t_0 = int(input("Введите t0 = "))
    u_0 = int(input("Введите U0 = "))
    t_n = int(input("Введите T = "))
    n = int(input("Введите N = "))
    h = (t_n - t_0) / n
    t = [t_0]

    for i in range(n):
        t.append(t[i] + h)
    u = exact(u_0, t, n)
    print(tabulate({"t": t, "U": u}, headers='keys',
                   tablefmt="psql", numalign="center", floatfmt=('.2f', '.12f')))
    plt.plot(t, u, 'k:')
    plt.legend(['точное решение'])
    plt.xlabel('t')
    plt.ylabel('U')
    plt.show()


if __name__ == "__main__":
    main()
