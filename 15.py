import tkinter as tk
from tkinter import messagebox
import requests

def get_weather():
    city = city_entry.get().strip()

    if not city:
        messagebox.showwarning("Внимание", "Пожалуйста, введите название города!")
        return

    url = f"https://wttr.in/{city}?format=%C+%t+\nВетер:+%w"
    response = requests.get(url)

    if response.status_code == 200 and "NOT FOUND" not in response.text:
        result_label.config(text=f"Погода в городе {city.capitalize()}:\n\n{response.text}")
    else:
        messagebox.showerror("Ошибка", "Город не найден. Проверьте раскладку.")

root = tk.Tk()
root.title("Погода на 1 курсе")
root.geometry("400x300")
root.resizable(False, False)

title_label = tk.Label(root, text="Мониторинг Погоды", font=("Arial", 14, "bold"))
title_label.pack(pady=15)

input_frame = tk.Frame(root)
input_frame.pack(pady=10)

tk.Label(input_frame, text="Введите город:", font=("Arial", 11)).pack(side=tk.LEFT, padx=5)
city_entry = tk.Entry(input_frame, font=("Arial", 11), width=15)
city_entry.pack(side=tk.LEFT, padx=5)

search_btn = tk.Button(root, text="Получить погоду", command=get_weather, font=("Arial", 11), bg="lightblue")
search_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue", justify=tk.CENTER)
result_label.pack(pady=20)

root.mainloop()