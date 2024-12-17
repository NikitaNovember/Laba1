'''Требуется для своего варианта второй части л.р. №6 (усложненной программы) разработать 
реализацию с использованием графического интерфейса. Допускается использовать любую графическую 
библиотеку питона. Рекомендуется использовать внутреннюю библиотеку питона  tkinter.
В программе должны быть реализованы минимум одно окно ввода, одно окно вывода (со скролингом), 
одно текстовое поле, одна кнопка.
Вариант 9. Вывести все натуральные числа до n, в записи которых встречается не более 2 четных 
цифр. Вывести наибольшую сумму цифр в числах и максимальное возможное число из чисел, которые 
имеют наибольшую сумму цифр.
'''
from textwrap import wrap
import tkinter as tk
import timeit
d={
    '0':0,
    '2':0,
    '4':0,
    '6':0,
    '8':0
}
def alg(n):
    a=[]
    for number in range(1,n):
        count_ch=0
        for el in str(number):
            if count_ch>2: break
            if int(el)%2==0: count_ch+=1
        if count_ch<3: a.append(number)
    return a
def target(n):
    msumm=0
    chislo=0
    matches=[]
    for number in [str(ch) for ch in range(1, n)]:
        tsumm=0
        for el in number:
            tsumm+=int(el)
            if el in d.keys(): d[el]+=1
        if sum(d.values())<3: 
            if msumm<tsumm:
                msumm=tsumm
                chislo=number
            matches.append(int(number))
        for keys in d.keys(): d[keys]=0
    return matches,chislo,msumm
def is_n():
    btn1['state']='disabled'
    global n
    n=entry1.get()
    t.focus()
    t.delete(1.0,tk.END)
    if n.isnumeric():
        n=int(n)
        if n>0:
            alg_time =timeit.timeit('alg(n)', globals = globals(), number =1)
            func_time = timeit.timeit('target(n)', globals = globals(), number =1)
            te = f'n: {n} \n\nАлгоритмический метод\nПодходящие числа: \n{alg(n)} \nНаибольшая сумма цифр в выведенных числах, которая находится в наибольшем числе {target(n)[1]}: {target(n)[2]}\nВремя выполнение алгоритмическим способом формирования: {alg_time}\n\nФункциональный метод\nПодходящие числа: \n{target(n)[0]}\nВремя выполнение функциональным способом формирования: {func_time}'
            t.insert(1.0,te)
            scrollbar = tk.Scrollbar(orient="vertical", command = t.yview)
            t["yscrollcommand"]=scrollbar.set
            scrollbar.grid(row=3,column=0,columnspan=2,sticky='nse',pady=10)
            t.yview_scroll(number=1, what="units")
            scrollbar.config(command=t.yview)
        else: t.insert(1.0,'Вы ввели некорректное число n. Введите натуральное число n.')
    else: t.insert(1.0,'Вы ввели некорректное число n. Введите натуральное число n.')
def quit(): win.quit()
win = tk.Tk()
win.geometry('700x450')
win.title('Программа нахождения всех натуральных чисел до заданного n с условием.')
lblif = tk.Label(font='9',text='Программа нахождения всех натуральных чисел до заданного, в которых встречается не более 2 четных цифр.')
lblif.grid(row=0,column=0,columnspan=2,pady=10)
win.update() 
width = lblif.winfo_width()
char_width = width / len(lblif['text'])
wrapped_text = '\n'.join(wrap(lblif['text'], int(700 / char_width)))
lblif['text'] = wrapped_text
lbl1 = tk.Label(text='Введите натуральное число n: ',font='9')
lbl1.grid(row=1, column=0, pady=10)
win.columnconfigure(index=0, weight=350)
win.columnconfigure(index=1, weight=350)
btn1 = tk.Button(text='Выполнить вычисления',font='9', command=is_n, state='disabled')
btn1.grid(row=2, column=0, columnspan=2, pady=10)
var = tk.StringVar()
def btnvis(*args):
    if entry1.get()!='': btn1['state']='normal'
var.trace_add("write", btnvis)
entry1 = tk.Entry(font='9', textvariable=var)
entry1.grid(row=1,column=1, pady=10)
entry1.focus()
t = tk.Text(win,height=7,font='9', width = 700)
t.grid(row=3,column=0, columnspan=2, sticky='ew', pady=10)
btn2 = tk.Button(text='Закрыть программу',font='9', command=quit)
btn2.grid(row=4,column=0,columnspan=2,pady=10)
win.mainloop()

