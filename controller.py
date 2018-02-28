#  здесь представленны функции обработки событий 

from tkinter import *
from PIL import Image
import functions as fnk
import pylab
from matplotlib import mlab


def error_win(er_code):
        """Рисует окно с ошибкой"""
        if (er_code == 0):
            win = Toplevel()
            win.title("ОШИБКА")
            win.geometry("300x100")
            Button(win, text="Ok", command=win.destroy).pack(side="bottom")
            Label(win, text="Лямбда должна быть меньше чем Мю").pack()
        elif (er_code == 1):
            win = Toplevel()
            win.title("ОШИБКА")
            win.geometry("400x100")
            Button(win, text="Ok", command=win.destroy).pack(side="bottom")

            Label(win,
            text="A должна быть меньше чем 1, а МЮ больше нуля").pack()


def show_diag(model):
        """Выводит на экран картинку с диаграммой"""
        diagrams = {
            "M/M/1": "images/mm1.png",
            "M/M/V/K": "images/mmvk.png",
            "M/M/V": "images/mmv.gif",
            "M/M/Inf": "images/mminf.png",
            "M/M/V/K/N": "images/mmvkn.png"
            }
        img = Image.open(diagrams[model])
        img.show()


def show_scheme(model):
        """Выводит на экран картинку с co схемой"""
        schemes = {
            "M/M/1": "images/schemeMM1.png",
            "M/M/V/K": "images/schemeMMVK.png",
            "M/M/V": "images/schemeMMV.png",
            "M/M/Inf": "images/schemeMMINF.png",
            "M/M/V/K/N": "images/schemeMMVKN.png"
            }
        img = Image.open(schemes[model])
        img.show()


def make_table(model, m, l, vv = 0, aa = 0, nn = 0):
    """Генерит таблицу значений параметров для модели"""
    if model == "M/M/1":
        if m == 0:
            m = 0.1
        ro = l / m
        if ro < 1:
            if ro > 0:
                win = Toplevel()
                win.title("M/M/1")
                win.geometry("400x400")
                text = Text(win)
                text.grid()
                s = "k          P(k)\n"
                for i in range(11):
                        s += str(i) + "     " + str(fnk.funk_mm1(i, ro)) + "\n"
                s += "Характеристики:\n"
                s += "K(ср): " + str(ro / (1 - ro)) + "\n"
                s += "T(ср): " + str((1 / m) / (1 - ro))
                text.insert(0.0, s)
        else:
            error_win(0)

    if model == "M/M/Inf":
        if m == 0:
            m = 0.1
        ro = l / m
        win = Toplevel()
        win.title("M/M/INF")
        win.geometry("400x400")
        text = Text(win)
        text.grid()
        s = "k          P(k)\n"
        for i in range(11):
                s += str(i) + "      " + str(fnk.funk_mminf(i, ro)) + "\n"
        s += "Характеристики:\n"
        s += "K(ср): " + str(ro) + "\n"
        s += "T(ср): " + str(1 / m)
        text.insert(0.0, s)

    if model == "M/M/V":
        if m == 0:
            m = 0.1
        ro = l / m
        z = int(vv + 1)
        gamma = 1 / (m * (vv - ro))
        win = Toplevel()
        win.title("M/M/V")
        win.geometry("400x400")
        text = Text(win)
        text.grid()
        s = "k          P(k)\n"
        for i in range(z):
            s += str(i) + "         " + str(fnk.funk_mmv1(i, ro, vv)) + "\n"
        s += "k          W(k)\n"
        for i in range(z, 100):
                s += str(i) + "      " + str(fnk.funk_mmv2(i, ro, vv)) + "\n"
        s += "Характеристики:\n"
        s += "gamma(ср): " + str(gamma) + "\n"
        s += "j(ср): " + str(l * gamma) + "\n"
        s += "P(t): " + str(fnk.funk_mmv3(ro, vv))
        text.insert(0.0, s)

    if model == "M/M/V/K":
        ro = l / m
        z = int(vv + 1)
        win = Toplevel()
        win.title("M/M/V/K")
        win.geometry("400x400")
        text = Text(win)
        text.grid()
        s = "k          P(k)\n"
        for i in range(z):
            s += str(i) + "          " + str(fnk.funk_mmvk(i, ro, vv)) + "\n"
        s += "Характеристики:\n"
        s += "P(t) = P(b): " + str(fnk.funk_mmvk1(ro, vv))
        text.insert(0.0, s)

    if model == "M/M/V/K/N":
        if m > 0 and 0 < aa < 1:
            z = int(vv + 1)
            win = Toplevel()
            win.title("M/M/V/K/N")
            win.geometry("400x400")
            text = Text(win)
            text.grid()
            s = "k          P(k)\n"
            for i in range(z):
                s += str(i) + " " + str(fnk.funk_mmvkn1(i, vv, aa, nn)) + "\n"
            s += "Характеристики:\n"
            s += "P(t): " + str(fnk.funk_mmvkn2(vv, aa, nn)) + "\n"
            s += "P(b): " + str(fnk.funk_mmvkn3(vv, aa, nn))
            text.insert(0.0, s)
        else:
            error_win(1)


def make_graph(model, m, l, vv = 0, aa = 0, nn = 0):
    """Делает график для мат зависимостей модели"""
    if model == "M/M/1":
        if m == 0:
            m = 0.1
        ro = l / m
        if ro < 1:
            if ro > 0:
                xmin = 0
                xmax = 10.0
                dx = 0.01
                xlist = mlab.frange(xmin, xmax, dx)
                ylist = [fnk.funk_mm1(x, ro) for x in xlist]
                pylab.plot(xlist, ylist, label="MM1")
                pylab.xlabel("K")
                pylab.ylabel("P(K)")
                pylab.legend()
                pylab.show()
        else:
            error_win(0)

    if model == "M/M/Inf":
        if m == 0:
            m = 0.1
        k_shtrih = l / m
        if k_shtrih:
            xmin = 0.0
            xmax = 10.0
            dx = 1
            xlist = mlab.frange(xmin, xmax, dx)
            ylist = [fnk.funk_mminf(x, k_shtrih) for x in xlist]
            pylab.plot(xlist, ylist)
            pylab.xlabel("K")
            pylab.ylabel("P(K)")
            pylab.show()

    if model == "M/M/V":
        ro = l / m
        if m == 0:
            m = 0.1
        if ro:
            xmin = 0.0
            xmax = vv
            dx = 1
            xlist = mlab.frange(xmin, xmax, dx)
            ylist = [fnk.funk_mmv1(x, ro, vv) for x in xlist]

            pylab.plot(xlist, ylist, label="Before V")
            xmin = vv
            xmax = 30
            xlist = mlab.frange(xmin, xmax, dx)
            ylist = [fnk.funk_mmv2(x, ro, vv) for x in xlist]
            pylab.plot(xlist, ylist, label="After V")
            xmin = 0
            xlist = mlab.frange(xmin, xmax, dx)
            ylist = [fnk.funk_mmv3(ro, vv) for x in xlist]
            pylab.plot(xlist, ylist, label="P(t)")
            pylab.legend()
            pylab.show()

    if model == "M/M/V/K":
        if m == 0:
            m = 0.1
        ro = l / m
        if ro:
            xmin = 0.0
            xmax = vv
            dx = 1
            xlist = mlab.frange(xmin, xmax, dx)
            ylist = [fnk.funk_mmvk(x, ro, vv) for x in xlist]
            pylab.plot(xlist, ylist, label="P(k)")
            ylist = [fnk.funk_mmvk1(ro, vv) for x in xlist]
            pylab.plot(xlist, ylist, label="P(t)")
            pylab.legend()
            pylab.show()

    if model == "M/M/V/K/N":
        if m > 0 and 0 < aa < 1:
            xmin = 0.0
            xmax = vv
            dx = 1
            xlist = mlab.frange(xmin, xmax, dx)
            ylist = [fnk.funk_mmvkn1(x, vv, aa, nn) for x in xlist]
            pylab.plot(xlist, ylist, label="P(k)")
            ylist = [fnk.funk_mmvkn2(vv, aa, nn) for x in xlist]
            pylab.plot(xlist, ylist, label="P(t)")
            ylist = [fnk.funk_mmvkn3(vv, aa, nn) for x in xlist]
            pylab.plot(xlist, ylist, label="P(b)")
            pylab.legend(frameon=False)
            pylab.show()
        else:
            error_win(1)
