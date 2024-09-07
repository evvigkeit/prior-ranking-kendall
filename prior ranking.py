import tkinter as tk
from tkinter import messagebox
import copy
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

pirson = [3.842, 5.992, 7.815, 9.488, 11.071, 12.509, 14.068, 15.509, 16.921, 18.309]


def get_num():
    expert_get = int(expert_ent.get())
    factor_get = int(factor_ent.get())
    if not expert_get:
        tk.messagebox.showinfo(message='Вы не указали количество экспертов!')
    elif not factor_get:
        tk.messagebox.showinfo(message='Вы не указали количество факторов!')
    else:
        expert_num.destroy()
        factor_num.destroy()
        expert_ent.destroy()
        factor_ent.destroy()
        enter_butt_main.destroy()

    ''' ******************* СОЗДАЕМ ПОЛЕ ДЛЯ ВВОДА РЕЗУЛЬТАТОВ *********************'''

    zn, x,  = 0, []
    global y
    y = []
    for i in range(expert_get):
        tk.Label(window, text=f'Ex{i+1}').grid(row=0, column=i+2)
        for j in range(factor_get):
            tk.Label(window, text=f'F{j+1}').grid(row=j+1, column=1)
            zn = tk.Entry(window, width=3)
            zn.grid(row=j+1, column=i+2)
            x.append(zn)
        y.append(x)
        x = []
    butt_count = tk.Button(window, text='Ввод', command=num_count)
    butt_count.grid(row=factor_get + 1, column=expert_get + 2)


"""******************** ПОЛУЧАЕМ ВВЕДЕННЫЕ ЧИСЛА И СОРТИРУЕМ ИХ ***********************"""


def num_count():
    unsorted_a, unsorted_b, sorted_a, sorted_b = [], [], [], []
    for i in range(len(y)):
        for j in range(len(y[i])):
            unsorted_b.append(int(y[i][j].get()))
        unsorted_a.append(unsorted_b)
        unsorted_b = []
    sorted_a = copy.deepcopy(unsorted_a)
    for i in range(len(y)):
        sorted_a[i] = sorted(sorted_a[i])
    print(unsorted_a, '-unsort_a')
    print(sorted_a, '-sort_a')

    '''******************* НОВЫЕ РАНГИ ***************************'''

    count, c, e, repeat_a, repeat_b = 1, 0, [], [], []
    for i in range(len(sorted_a)):
        for j in range(1, len(sorted_a[i])):
            if sorted_a[i][j - 1] == sorted_a[i][j] and j == (len(sorted_a[i]) - 1):
                count += 1
                if c == 0:
                    c = j + 1 + j
                else:
                    c += j + 1
                for g in range(count):
                    if g == 0:
                        repeat_b.append(count)
                    e.append(c / count)
                    if g == count - 1:
                        count = 1
                        c = 0
            elif sorted_a[i][j - 1] != sorted_a[i][j] and count != 1:
                for g in range(count):
                    if g == 0:
                        repeat_b.append(count)
                    e.append(c / count)
                    if g == count - 1:
                        count = 1
                        c = 0
                if j == (len(sorted_a[i]) - 1):
                    e.append(j + 1)
            elif sorted_a[i][j - 1] == sorted_a[i][j]:
                count += 1
                if c == 0:
                    c = j + 1 + j
                else:
                    c += j + 1
            else:
                c = 0
                count = 1
                e.append(j)
        if len(e) < len(sorted_a[i]):
            e.append(len(sorted_a[i]))
        sorted_b.append(e)
        e = []
        if len(repeat_b) == 0:
            repeat_b.append(0)
        repeat_a.append(repeat_b)
        repeat_b = []

    ''' ********************** НОВАЯ ОТСОРТИРОВАННАЯ МАТРИЦА **************************'''

    example_list = []
    ex_list = example_list.copy()
    for _ in range(len(sorted_b[0])):
        example_list.append('x')

    exx_list = []
    for i in range(len(sorted_b)):
        if i > 0:
            del sorted_b[0]
            exx_list.append(ex_list)
            sorted_b.extend(exx_list)
            exx_list = []
        ex_list = example_list.copy()
        for j in range(len(sorted_b[i])):
            min_un = min(unsorted_a[i])
            ind_un = unsorted_a[i].index(min_un)
            min_sort = min(sorted_b[0])
            ind_sort = sorted_b[0].index(min_sort)
            ex_list.insert(ind_un, min_sort)
            ex_list.pop(ind_un + 1)
            unsorted_a[i][ind_un] = 1000
            sorted_b[0][ind_sort] = 1000
        if len(sorted_b) == i + 1:
            del sorted_b[0]
            exx_list.append(ex_list)
            sorted_b.extend(exx_list)
            exx_list = []
    print(sorted_b, '-sort_b')

    """**************** СУММА РАНГОВ ********************************"""

    f_list, f_list_ed = [], [[]]
    for i in range(len(sorted_b[i])):
        for j in range(len(sorted_b)):
            f_list_ed[0].append(sorted_b[j][i])
        f_list.extend(f_list_ed)
        f_list_ed[0] = []

    print(f_list, '-f_list')

    f_list_sum = []
    for i in range(len(f_list)):
        a = 0
        for j in range(len(f_list[i])):
            a += f_list[i][j]
        f_list_sum.append(a)

    print(f_list_sum, '-f_sum')

    range_sum = 0
    for i in range(len(f_list_sum)):
        range_sum += f_list_sum[i]

    print(range_sum, '-range_sum')
    av_range_sum = range_sum / len(f_list_sum)

    """**************** СРЕДНЕЕ КВАДРАТИЧЕСКОЕ ОТКЛОНЕНИЕ *****************************"""

    st_dev = []
    for i in range(len(f_list_sum)):
        a = (f_list_sum[i] - av_range_sum) ** 2
        st_dev.append(a)

    print(st_dev, '-st_dev')
    st_dev_sum = 0
    for i in range(len(st_dev)):
        st_dev_sum += st_dev[i]

    print(st_dev_sum, '-st_dev_sum')

    """*********************** СОГЛАСОВАННОСТЬ МНЕНИЙ ЭКСПЕРТОВ ****************************************"""

    count = 0
    for i in range(len(repeat_a)):
        t = 0
        for j in range(len(repeat_a[i])):
            t += repeat_a[i][j] ** 3 - repeat_a[i][j]
        count += t * 1 / 12

    print(count, '-count')

    w = 12 * st_dev_sum / (len(sorted_b) ** 2 * (len(sorted_b[0]) ** 3 - len(sorted_b[0])) - len(sorted_b) * count)
    print(w, '-w')

    x2 = 0
    if w < 0.5:
        tk.messagebox.showinfo(message='Мнения экспертов не согласованы!')
    else:
        x2 = 12*st_dev_sum / (len(sorted_b)*len(sorted_b[0]) * (len(sorted_b[0])+1) - (1 / (len(sorted_b[0])-1)*count))
        print(x2, '-x^2')

    factor_names = []
    for i in range(len(sorted_b[i])):
        factor_names.append(f'Factor{i + 1}')

    pirson_xi2 = len(sorted_b[0]) - 1
    if pirson_xi2 >= x2:
        tk.messagebox.showinfo(message='Мнения экспертов случайны!')
    else:
        fig1, ax1 = plt.subplots()
        ax1.bar(factor_names, f_list_sum)
        ax1.set_title('Априорная диаграмма рангов')
        ax1.set_xlabel('Факторы')
        ax1.set_ylabel('Суммы рангов')
        canvas1 = FigureCanvasTkAgg(fig1, window)
        canvas1.draw()
        canvas1.get_tk_widget().grid(row=len(sorted_b[0]) + 4, column=len(sorted_b[0]) + 4)


'''************************************** ПАРАМЕТРЫ ОКНА **************************************'''

window = tk.Tk()  # создает окно
window.title("Калькулятор априорного ранжирования")
window.geometry('1100x1000')  # +300 (пикселей) - влево; +10 - вниз

"""*************************************** ГЛАВНОЕ ОКНО ***************************************"""

expert_num = tk.Label(window, text='Укажите количество экспертов: ',
                      font=('Times New Roman', 13), height=5)
factor_num = tk.Label(window, text='Укажите количество факторов: ',
                      font=('Times New Roman', 13), height=5)
expert_ent = tk.Entry(window)
factor_ent = tk.Entry(window)
enter_butt_main = tk.Button(window, text='Ввод', command=get_num)
expert_num.grid(row=0, column=0)
factor_num.grid(row=1, column=0)
expert_ent.grid(row=0, column=1)
factor_ent.grid(row=1, column=1)
enter_butt_main.grid(row=2, column=1, stick='we')


# метод pack размещает элемент на экране
# метод grid размещает табличку на экране
window.mainloop()  # "зацикливает" окно, позволяя ему не проподать
