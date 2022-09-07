class Neuron:

    def __init__(self, w, f=lambda x: x):
        """
        Сохраняет веса и функцию внутри класса.
        :param w: массив весов нейрона --- w = (w_1, ..., w_n).
        :param f: функцию активации f (аргумент по умолчанию f(x) = x).
        """
        self.x = None
        self.w = w
        self.f = f

    def forward(self, x):
        """
        :param x: массив x = (x_1, ..., x_n)--- входы нейрона.
        :return: f(w_1x_1 + ... + w_nx_n).
        """
        summa = 0
        self.x = x
        for i in range(len(x)):
            summa += self.w[i] * x[i]
        return self.f(summa)

    def backlog(self):
        """
        :return: массив x, который подавался на вход функции forward при её последнем вызове. Если ранее функция
        forward не вызывалось, возвращает None.
        """
        if self.x is not None:
            return self.x
        return None



