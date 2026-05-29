import tkinter as tk
from tkinter import messagebox, scrolledtext
import requests

def get_city_facts():
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("Ошибка", "Введите название города!")
        return

    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, f"Поиск достопримечательностей для: {city}...\n\n")
    root.update()

    url = "https://ru.wikipedia.org/w/api.php"

    params = {
        "action": "query",
        "list": "search",
        "srsearch": f"достопримечательности {city}",
        "format": "json",
        "srlimit": 3,
    }

    headers = {
        "User-Agent": "CityHistoryGuideBot/1.0 (contact@example.com)"
    }

    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()

        search_results = data.get("query", {}).get("search", [])

        if not search_results:
            result_text.insert(
                tk.END, "Информация не найдена. Попробуйте другой город."
            )
            return

        result_text.insert(
            tk.END, f"Вот что удалось найти в исторических источниках:\n\n"
        )

        for i, item in enumerate(search_results, 1):
            title = item["title"]
            snippet = (
                item["snippet"]
                .replace('<span class="searchmatch">', "")
                .replace("</span>", "")
            )

            result_text.insert(tk.END, f"{i}. {title}\n")
            result_text.insert(tk.END, f"Факты: {snippet}...\n")
            result_text.insert(
                tk.END, "-" * 50 + "\n\n"
            )

    except requests.exceptions.RequestException as e:
        messagebox.showerror(
            "Ошибка сети", f"Не удалось подключиться к API:\n{e}"
        )

root = tk.Tk()
root.title("Исторический гид по городам")
root.geometry("600x450")
root.configure(bg="#f0f0f0")

frame_top = tk.Frame(root, bg="#f0f0f0", pady=10)
frame_top.pack(fill=tk.X)

label = tk.Label(
    frame_top, text="Введите город:", font=("Arial", 12), bg="#f0f0f0"
)
label.pack(side=tk.LEFT, padx=10)

city_entry = tk.Entry(frame_top, font=("Arial", 12), width=25)
city_entry.pack(side=tk.LEFT, padx=5)
city_entry.insert(0, "Санкт-Петербург")

btn_search = tk.Button(
    frame_top,
    text="Найти факты",
    font=("Arial", 11, "bold"),
    bg="#4CAF50",
    fg="white",
    command=get_city_facts,
)
btn_search.pack(side=tk.LEFT, padx=10)

result_text = scrolledtext.ScrolledText(
    root, font=("Arial", 11), wrap=tk.WORD, bd=2, relief=tk.GROOVE
)
result_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

root.mainloop()
