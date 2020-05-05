import tkinter

from app.BankInterest import BankInterest

LEFT_MOUSE_CLICK = "<Button-1>"


def calculate(_):
    try:
        _total = float(total.get())
        _duration = int(duration.get())
        _percentage = float(percentage.get())
    except ValueError:
        raise Exception("Невалидные данные")

    credit = BankInterest(_total, _duration, _percentage)
    payouts_list.grid_forget()
    total_amount.grid_forget()
    each_month_payout.grid_forget()

    if payout_type.get() == 0:
        info = credit.ann_int()
        total_amount['text'] = f'Общая сумма: {info[1]}'
        total_amount.grid(column=0, columnspan=2, row=6)

        each_month_payout['text'] = f'Ежемесячная выплата: {info[0]}'
        each_month_payout.grid(column=0, columnspan=2, row=7)
    else:
        info = credit.diff_int()
        total_amount['text'] = f'Общая сумма: {info[1]}'
        total_amount.grid(column=0, columnspan=2, row=6)
        elements = []
        for i, value in enumerate(info[0]):
            elements.append(f'Месяц {i + 1}: {value} рублей')
        for element in reversed(elements):
            payouts_list.insert(0, element)
        payouts_list.grid(column=0, columnspan=2, row=7)


root = tkinter.Tk()
root.title('Расчет кредита')

total_label = tkinter.Label(root, text="Сумма кредита (рубли)")
total = tkinter.Entry(root, width=10)
total_label.grid(column=0, row=0)
total.grid(column=1, row=0)

duration_label = tkinter.Label(root, text="Срок кредита (лет)")
duration = tkinter.Entry(root, width=10)
duration_label.grid(column=0, row=1)
duration.grid(column=1, row=1)

percentage_label = tkinter.Label(root, text="Годовые проценты")
percentage = tkinter.Entry(root, width=10)
percentage_label.grid(column=0, row=2)
percentage.grid(column=1, row=2)

payout_type = tkinter.IntVar()
payout_type.set(0)
annual = tkinter.Radiobutton(text="Аннуальные выплаты", variable=payout_type, value=0)
differentiated = tkinter.Radiobutton(text="Дифференцированные выплаты", variable=payout_type, value=1)

annual.grid(column=0, columnspan=2, row=3)
differentiated.grid(column=0, columnspan=2, row=4)

btn = tkinter.Button(root,
                     text="Рассчитать", width=30,
                     height=3,
                     bg="white", fg="black")
btn.grid(column=0, columnspan=2, row=5)

payouts_list = tkinter.Listbox(selectmode=tkinter.EXTENDED)
total_amount = tkinter.Label(root)
each_month_payout = tkinter.Label(root)

btn.bind(LEFT_MOUSE_CLICK, calculate)
