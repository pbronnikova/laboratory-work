import csv
import tkinter as tk
from tkinter import filedialog
from statistics import median

data = []

def open_file():
    global data
    file = filedialog.askopenfilename(filetypes=[("CSV", "*.csv")])
    if not file:
        return

    with open(file, encoding="utf-8-sig") as f:
        data = list(csv.DictReader(f))

    text.delete("1.0", tk.END)
    text.insert(tk.END, "Загружено строк: " + str(len(data)) + "\n\n")

    for row in data:
        text.insert(tk.END, str(row) + "\n")


def calculate():
    ages = [float(r["Age"]) for r in data
            if r["Age"] and float(r["Age"]) >= 18]

    m = median(ages)

    group15 = [
        r for r in data
        if r["Age"] and r["Fare"]
        and m - 15 <= float(r["Age"]) <= m + 15
        and float(r["Age"]) >= 18
    ]

    total = sum(float(r["Fare"]) for r in group15)

    group7 = [
        r for r in data
        if r["Age"] and r["Fare"]
        and m - 7 <= float(r["Age"]) <= m + 7
    ]

    survived = [float(r["Fare"]) for r in group7
                if r["Survived"] == "1"]

    died = [float(r["Fare"]) for r in group7
            if r["Survived"] == "0"]

    avg_survived = sum(survived) / len(survived) if survived else 0
    avg_died = sum(died) / len(died) if died else 0

    text.delete("1.0", tk.END)
    text.insert(tk.END,
        f"Медианный возраст: {m:.2f}\n"
        f"Интервал ±15: {m-15:.2f} - {m+15:.2f}\n"
        f"Суммарная стоимость билетов: {total:.2f}\n\n"
        f"Интервал ±7: {m-7:.2f} - {m+7:.2f}\n"
        f"Средний билет выживших: {avg_survived:.2f}\n"
        f"Средний билет погибших: {avg_died:.2f}"
    )


root = tk.Tk()
root.title("Лабораторная работа №11")
root.geometry("800x600")

tk.Button(root, text="Открыть CSV", command=open_file).pack(pady=5)
tk.Button(root, text="Рассчитать", command=calculate).pack(pady=5)

text = tk.Text(root, font=("Arial", 10))
text.pack(fill="both", expand=True, padx=10, pady=10)

root.mainloop()