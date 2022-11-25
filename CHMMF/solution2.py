import numpy as np
import matplotlib.pyplot as plt
import math
import copy


def func(x, X):
    return math.sqrt(1 - x / X) * abs(np.sin(3 * x))


def mu(t):
    return (1 + t / 100) ** (-1) * (np.sin(t / 8)) ** 2


def speed(x, t):
    return np.sin(t / 4.5 - x / 2)


def positive_speed(a, b, T_L, X_L, Nx):
    hx = X_L / Nx
    x = np.linspace(0, X_L, Nx + 1)
    ht = b * hx / abs(a)
    Nt = int(T_L / ht)
    t = np.linspace(0, T_L, Nt + 1)
    lyambda = a * ht / hx
    U_exact = np.zeros(len(x))
    Uj = np.zeros(len(x))
    Uj1 = np.zeros(len(x))
    for i in range(len(x)):
        Uj[i] = func(x[i], X_L)
    for j in range(len(t) - 1):
        Uj1[0] = mu(t[j + 1])
        for i in range(1, len(x)):
            Uj1[i] = Uj[i] * (1 - lyambda) + lyambda * Uj[i - 1]
        Uj = copy.copy(Uj1)
    for i in range(0, len(x)):
        if x[i] >= a * T_L:
            U_exact[i] = func(x[i] - a * T_L, X_L)
        else:
            U_exact[i] = mu(T_L - x[i] / a)
    return U_exact, Uj1, x


def negative_speed(a, b, T_L, X_L, Nx):
    hx = X_L / Nx
    x = np.linspace(0, X_L, Nx + 1)
    ht = b * hx / abs(a)
    Nt = int(T_L / ht)
    t = np.linspace(0, T_L, Nt + 1)
    lyambda = a * ht / hx
    Uj = np.zeros(len(x))
    Uj1 = np.zeros(len(x))
    U_exact = np.zeros(len(x))
    for i in range(len(x)):
        Uj[i] = func(x[len(x) - 1 - i], X_L)
    for j in range(0, len(t) - 1):
        Uj1[Nx] = mu(t[j + 1])
        for i in range(Nx - 1, -1, -1):
            Uj1[i] = Uj[i] * (1 + lyambda) - lyambda * Uj[i + 1]
        Uj = copy.copy(Uj1)
    for i in range(0, len(x)):
        if X_L - x[i] >= abs(a) * T_L:
            U_exact[i] = func(X_L - x[i] - abs(a) * T_L, X_L)
        else:
            U_exact[i] = mu(T_L - (X_L - x[i]) / abs(a))
    return U_exact, Uj1, x


def main():
    a = 1
    b = 1
    T_L = 15
    X_L = 10
    Nx = 400

    U_exact, Uj1, x = positive_speed(a, b, T_L, X_L, Nx)
    fig, ax = plt.subplots()
    ax.set_title('Решение уравнения переноса U=U(x,t)')
    ax.grid(which='major')
    ax.grid(which='minor', linestyle=':')
    ax.set_xlabel('x', fontsize=15)
    ax.set_ylabel('U(x,t)', fontsize=15, rotation=90)
    ax.scatter(x, U_exact, color="blue", s=1, label="Точное решение")
    ax.plot(x, Uj1, linestyle='solid', color='orange', label="Приближенное решение")
    ax.legend()
    plt.show()

    a = -1
    b = 1
    T_L = 15
    X_L = 10
    Nx = 400
    U_exact, Uj1, x = negative_speed(a, b, T_L, X_L, Nx)
    fig1, ax = plt.subplots()
    ax.set_title('Решение уравнения переноса U=U(x,t)')
    ax.grid(which='major')
    ax.grid(which='minor', linestyle=':')
    ax.set_xlabel('x', fontsize=15)
    ax.set_ylabel('U(x,t)', fontsize=15, rotation=90)
    ax.scatter(x, U_exact, color="blue", s=1, label="Точное решение")
    ax.plot(x, Uj1, linestyle='solid', color='orange', label="Приближенное решение")
    ax.legend()
    plt.show()

    T_L = 15
    b = 1
    X_L = 10
    Nx = 400
    Hx = X_L / Nx
    x = np.linspace(0, X_L, Nx + 1)

    Ujj = np.zeros(len(x))
    for i in range(len(x)):
        Ujj[i] = func(x[i], X_L)
    Uj11 = np.zeros(len(x))
    a1 = np.zeros(len(x))

    Uj = np.zeros(len(x))
    for i in range(len(x)):
        Uj[i] = func(x[i], X_L)
    Uj1 = np.zeros(len(x))
    a = np.zeros(len(x))

    t1 = 0
    while t1 <= T_L:
        a_max = max(abs(speed(x, t1)))
        if a_max != 0:
            Ht = Hx / abs(a_max)
        else:
            Ht = Hx
        a1[0] = speed(x[0], t1)
        a1[Nx] = speed(x[Nx], t1)

        if a1[0] < 0:
            lyambda = a1[0] * Ht / Hx
            Uj11[0] = (1 + lyambda) * Ujj[0] - lyambda * Ujj[1]
        else:
            Uj11[0] = mu(t1)

        if a1[Nx] < 0:
            Uj11[Nx] = Ujj[Nx]
        else:
            lyambda = a1[Nx] * Ht / Hx
            Uj11[Nx] = Ujj[Nx] * (1 - lyambda) + lyambda * Ujj[Nx - 1]

        for i in range(1, Nx):
            a1[i] = speed(x[i], t1)
            lyambda = a1[i] * Ht / Hx
            if a1[i] >= 0:
                Uj11[i] = Ujj[i] * (1 - lyambda) + lyambda * Ujj[i - 1]
            else:
                Uj11[i] = Ujj[i] * (1 + lyambda) - lyambda * Ujj[i + 1]

        Ujj = copy.copy(Uj11)
        t1 += Ht

    t = 0
    while t <= T_L:
        a_max = max(abs(speed(x, t)))
        if a_max != 0:
            Ht = b * Hx / abs(a_max)
        else:
            Ht = b * Hx
        a[0] = speed(x[0], t)
        a[Nx] = speed(x[Nx], t)

        if a[0] < 0:
            lyambda = a[0] * Ht / Hx
            Uj1[0] = (1 + lyambda) * Uj[0] - lyambda * Uj[1]
        else:
            Uj1[0] = mu(t)

        if a[Nx] < 0:
            Uj1[Nx] = Uj[Nx]
        else:
            lyambda = a[Nx] * Ht / Hx
            Uj1[Nx] = Uj[Nx] * (1 - lyambda) + lyambda * Uj[Nx - 1]

        for i in range(1, Nx):
            a[i] = speed(x[i], t)
            lyambda = a[i] * Ht / Hx
            if a[i] >= 0:
                Uj1[i] = Uj[i] * (1 - lyambda) + lyambda * Uj[i - 1]
            else:
                Uj1[i] = Uj[i] * (1 + lyambda) - lyambda * Uj[i + 1]

        Uj = copy.copy(Uj1)
        t += Ht

    fig = plt.figure(figsize=(12, 5))
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2)
    ax1.set_title('Скорость а = a(x,t)')
    ax1.set_xlabel('x', fontsize=15)
    ax1.set_ylabel('a(x,t)', fontsize=15, rotation=90)
    ax1.plot(x, a1, color="red")
    ax1.grid(which='major')
    ax1.grid(which='minor', linestyle=':')
    ax2.axis([0, 10, 0, 1.1])
    ax2.grid(which='major')
    ax2.grid(which='minor', linestyle=':')
    ax2.set_title('Решение уравнения переноса U = U(x,t)')
    ax2.set_xlabel('x', fontsize=15)
    ax2.set_ylabel('U(x,t)', fontsize=15, rotation=90)
    # ax2.plot(x, Uj11, color="blue", label="Приближенное решение при B = 1")
    ax2.plot(x, Uj11, color="blue")
    # ax2.plot(x, Uj1, linestyle="dashed", color='orange', label="Приближенное решение при B = 0.9")
    ax2.plot(x, Uj1, linestyle="dashed", color='orange')
    ax2.legend()
    plt.show()


if __name__ == "__main__":
    main()
