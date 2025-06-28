import tkinter as tk
from functools import partial

currencies = {
    'USD': {'name': 'US Dollar', 'symbol': '$', 'rate': 1.00},
    'EUR': {'name': 'Euro', 'symbol': '€', 'rate': 0.92},
    'GBP': {'name': 'Pound Sterling', 'symbol': '£', 'rate': 0.78},
    'CNY': {'name': 'Chinese Yuan', 'symbol': '¥', 'rate': 7.26},
    'KWD': {'name': 'Kuwaiti Dinar', 'symbol': 'KD', 'rate': 0.31},
    'SAR': {'name': 'Saudi Riyal', 'symbol': '﷼', 'rate': 3.75},
    'INR': {'name': 'Indian Rupee', 'symbol': '₹', 'rate': 83.3},
    'PKR': {'name': 'Pakistani Rupee', 'symbol': '₨', 'rate': 278.5},
    'KRW': {'name': 'South Korean Won', 'symbol': '₩', 'rate': 1372.7},
    'JPY': {'name': 'Japanese Yen', 'symbol': '¥', 'rate': 157.3},
}

from_currency = "USD"
to_currency = "USD"

def select_currency(code, is_from):
    global from_currency, to_currency
    if is_from:
        from_currency = code
    else:
        to_currency = code
    update_buttons()
    convert()

def update_buttons():
    for btn in from_buttons:
        btn.config(bg='SystemButtonFace')
        if btn['text'].startswith(from_currency):
            btn.config(bg='lightblue')
    for btn in to_buttons:
        btn.config(bg='SystemButtonFace')
        if btn['text'].startswith(to_currency):
            btn.config(bg='lightgreen')

def on_number_click(num):
    entry.insert(tk.END, num)
    convert()

def clear_input():
    entry.delete(0, tk.END)
    result_label.config(text="")

def convert():
    try:
        amount = float(entry.get())
        usd = amount / currencies[from_currency]['rate']
        converted = usd * currencies[to_currency]['rate']
        symbol = currencies[to_currency]['symbol']
        result_label.config(text=f"{symbol} {converted:.2f}")
    except ValueError:
        result_label.config(text="")

root = tk.Tk()
root.title("Currency Converter")
root.geometry("800x500")
root.config(bg="#f0f0f0")

from_frame = tk.Frame(root, padx=10, pady=10)
from_frame.pack(side="left", fill="y")
tk.Label(from_frame, text="From Currency", font=("Segoe UI", 14)).pack()
from_buttons = []
for code, data in currencies.items():
    btn = tk.Button(from_frame, text=f"{code} ({data['symbol']})", width=18,
                    command=partial(select_currency, code, True))
    btn.pack(pady=2)
    from_buttons.append(btn)

to_frame = tk.Frame(root, padx=10, pady=10)
to_frame.pack(side="right", fill="y")
tk.Label(to_frame, text="To Currency", font=("Segoe UI", 14)).pack()
to_buttons = []
for code, data in currencies.items():
    btn = tk.Button(to_frame, text=f"{code} ({data['symbol']})", width=18,
                    command=partial(select_currency, code, False))
    btn.pack(pady=2)
    to_buttons.append(btn)

center_frame = tk.Frame(root, pady=20, padx=20, bg="#f0f0f0")
center_frame.pack(expand=True, fill="both")

entry = tk.Entry(center_frame, font=("Segoe UI", 18), justify='center')
entry.pack(pady=10)

result_label = tk.Label(center_frame, font=("Segoe UI", 20), fg="#333")
result_label.pack(pady=10)

btn_frame = tk.Frame(center_frame)
btn_frame.pack()

buttons = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    ['0', '.', 'C']
]

for row in buttons:
    row_frame = tk.Frame(btn_frame)
    row_frame.pack()
    for char in row:
        if char == 'C':
            btn = tk.Button(row_frame, text=char, width=6, height=2, command=clear_input)
        else:
            btn = tk.Button(row_frame, text=char, width=6, height=2, command=partial(on_number_click, char))
        btn.pack(side="left", padx=5, pady=5)

update_buttons()
root.mainloop()
