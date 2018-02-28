# описание структуры программы и GUI

from tkinter import *
import controller as cnt


class Application(Frame):
    """Создает GUI"""
    def __init__(self, master):
        """Создает рамку и элементы"""
        super(Application, self).__init__(master)
        self.lbl = Label(self, text="Модель: ")
        self.m_lbl = Label(self, text=chr(956))  # mu
        self.l_lbl = Label(self, text=chr(955))  # lambda
        self.v_lbl = Label(self, text="V")
        self.a_lbl = Label(self, text="a")
        self.n_lbl = Label(self, text="N")

        self.bttn = StringVar()
        self.mm1_radio = Radiobutton(self, text="M/M/1",
        variable=self.bttn, value="M/M/1", command=self.hide)

        self.mminf_radio = Radiobutton(self, text="M/M/Inf",
        variable=self.bttn, value="M/M/Inf", command=self.hide)

        self.mmv_radio = Radiobutton(self, text="M/M/V",
        variable=self.bttn, value="M/M/V", command=self.hide)

        self.mmvk_radio = Radiobutton(self, text="M/M/V/K",
        variable=self.bttn, value="M/M/V/K", command=self.hide)

        self.mmvkn_radio = Radiobutton(self, text="M/M/V/K/N",
        variable=self.bttn, value="M/M/V/K/N", command=self.hide)

        self.mu = Entry(self, width=10)
        self.lambd = Entry(self, width=10)
        self.v = Entry(self, width=10)
        self.a = Entry(self, width=10)
        self.n = Entry(self, width=10)

        self.diabttn = Button(self, text="Диаграмма", command=self.show_pic)
        self.grafbttn = Button(self, text="График", command=self.show_graph)
        self.schemebttn = Button(self, text="Схема", command=self.show_scheme)
        self.tablebttn = Button(self, text="Таблица", command=self.show_table)

        self.set_vidgets()
        self.grid()

    def set_vidgets(self):
        """Размещает элементы в рамке"""
        self.lbl.grid(row=0, column=0)
        self.mm1_radio.grid(row=1, column=0)
        self.mminf_radio.grid(row=1, column=1)
        self.mmv_radio.grid(row=1, column=2)
        self.mmvk_radio.grid(row=1, column=3)
        self.mmvkn_radio.grid(row=1, column=4)

        self.m_lbl.grid(row=2, column=0)
        self.mu.grid(row=3, column=0, columnspan=1)

        self.l_lbl.grid(row=2, column=1)
        self.lambd.grid(row=3, column=1, columnspan=1)

        self.v_lbl.grid(row=2, column=2)
        self.v.grid(row=3, column=2, columnspan=1, sticky=W)

        self.a_lbl.grid(row=2, column=3)
        self.a.grid(row=3, column=3)

        self.n_lbl.grid(row=2, column=4)
        self.n.grid(row=3, column=4)

        self.diabttn.grid(row=4, column=0)
        self.grafbttn.grid(row=4, column=4)
        self.schemebttn.grid(row=4, column=1)
        self.tablebttn.grid(row=4, column=3)

    def hide(self):
        """блокирует ненужные поля ввода"""
        model = self.bttn.get()
        if model == "M/M/1" or model == "M/M/Inf":
            self.v.configure(state=DISABLED)
            self.a.configure(state=DISABLED)
            self.n.configure(state=DISABLED)
        if model == "M/M/V" or model == "M/M/V/K" or model == "M/M/V/K/N":
            self.v.configure(state=NORMAL)
        if model == "M/M/V/K/N":
            self.a.configure(state=NORMAL)
            self.n.configure(state=NORMAL)
            self.lambd.configure(state=DISABLED)
        if model != "M/M/V/K/N":
            self.a.configure(state=DISABLED)
            self.n.configure(state=DISABLED)
            self.lambd.configure(state=NORMAL)

    def show_pic(self):
        """Обрабатывает нажатие кнопки 'Диаграмма' """
        model = self.bttn.get()
        cnt.show_diag(model)

    def show_scheme(self):
        """Обрабатывает нажатие кнопки 'Схема' """
        model = self.bttn.get()
        cnt.show_scheme(model)

    def show_table(self):
        """Выводит таблицу значений и характеристики"""
        model = self.bttn.get()
        model = self.bttn.get()
        if model == "M/M/1" or model == "M/M/Inf":
            m = float(self.mu.get())
            l = float(self.lambd.get())
            cnt.make_table(model, m, l)
        if model == "M/M/V" or model == "M/M/V/K":
            m = float(self.mu.get())
            l = float(self.lambd.get())
            vv = float(self.v.get())
            cnt.make_table(model, m, l, vv)
        if model == "M/M/V/K/N":
            m = float(self.mu.get())
            l = 1
            vv = float(self.v.get())
            aa = float(self.a.get())
            nn = float(self.n.get())
            cnt.make_table(model, m, l, vv, aa, nn)

    def show_graph(self):
        """Рисует график функции"""
        model = self.bttn.get()
        if model == "M/M/1" or model == "M/M/Inf":
            m = float(self.mu.get())
            l = float(self.lambd.get())
            cnt.make_graph(model, m, l)
        if model == "M/M/V" or model == "M/M/V/K":
            m = float(self.mu.get())
            l = float(self.lambd.get())
            vv = float(self.v.get())
            cnt.make_graph(model, m, l, vv)
        if model == "M/M/V/K/N":
            m = float(self.mu.get())
            l = 1
            vv = float(self.v.get())
            aa = float(self.a.get())
            nn = float(self.n.get())
            cnt.make_graph(model, m, l, vv, aa, nn)


