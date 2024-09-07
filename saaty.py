import tkinter as tk
from tkinter import Frame


def get_num():
    alter_get = int(alter_ent.get())
    factor_get = int(factor_ent.get())
    for widget in frame1.winfo_children():
        widget.destroy()
    t1 = tk.Label(frame1, text='''Делее необходимо оценить значимость выбранных Вами критериев. Для этого можно воспользоваться таблицей, приведенной ниже.
    ''').grid(row=0, column=0, stick='w')
    t2 = tk.Label(frame1, text='''ВАЖНО! Значимость критериев оценивается ОТНОСИТЕЛЬНО НАИБОЛЕЕ ВАЖНОГО КРИТЕРИЯ:
    
1 – ниболее важный критерий (к1) и фактор "Х" одинаково важны.
3 – умеренное превосходство к1 над "Х".
5 – существенное превосходство к1 над "Х".
7 – значительное превосходство к1 над "Х".
9 – очень сильное превосходство к1 над "Х".
2, 4, 6, 8 – промежуточные решения между двумя соседними суждениями.
''').grid(row=1, column=0, stick='w')
    tk.Label(frame2, text='Значимость').grid(row=0, column=1)
    for j in range(factor_get):
        tk.Label(frame2, text=f'Критерий №{j + 1}').grid(row=j +1, column=0)
        zn1 = tk.Entry(frame2, width=10)
        zn1.grid(row=j + 1, column=1)
    butt_factors = tk.Button(frame2, text='Ввод', command=factor_prior)
    butt_factors.grid(row=100, column=100)


def factor_prior():
    for widget in frame2.winfo_children():
        widget.destroy()








"""************************************ ГЛАВНОЕ ОКНО ******************************************"""
root = tk.Tk()
root.title('Метод анализа иерархий Саати')
root.state('zoomed')
frame1 = Frame(root)
frame2 = Frame(root)
frame1.grid(padx=0, pady=0)
frame2.grid(padx=0, pady=30)

alter_num = tk.Label(frame1, text='Укажите количество альтернатив: ', font=('Times New Roman', 13), height=5)
factor_num = tk.Label(frame1, text='Укажите количество критериев: ', font=('Times New Roman', 13), height=5)
alter_ent = tk.Entry(frame1)
factor_ent = tk.Entry(frame1)
enter_butt_main = tk.Button(frame1, text='Ввод', command=get_num)
alter_num.grid(row=0, column=0)
factor_num.grid(row=1, column=0)
alter_ent.grid(row=0, column=1)
factor_ent.grid(row=1, column=1)
enter_butt_main.grid(row=2, column=1, stick='we')
root.mainloop()
