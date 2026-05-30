from tkinter import *
import requests
root = Tk()
def get_facts():
    city = cityField.get()
    url = "https://ru.wikipedia.org/api/rest_v1/page/summary/" + city
    headers = {
        "User-Agent": "Python Tkinter student project"
    }
    result = requests.get(url, headers=headers)
    data = result.json()
    text = data["extract"]
    sentences = text.split(". ")
    if len(sentences) >= 2:
        result_text = city + "\n\n1. " + sentences[0] + ".\n\n2. " + sentences[1] + "."
    else:
        result_text = text
    info.delete("1.0", END)
    info.insert("1.0", result_text)
root["bg"] = "#fafafa"
root.title("Факты о городе")
root.geometry("600x500")
root.resizable(width=False, height=False)
frame_top = Frame(root, bg="#ffb700", bd=5)
frame_top.place(relx=0.15, rely=0.08, relwidth=0.7, relheight=0.20)
frame_bottom = Frame(root, bg="#ffb700", bd=5)
frame_bottom.place(relx=0.08, rely=0.34, relwidth=0.84, relheight=0.58)
cityField = Entry(frame_top, bg="white", font=18)
cityField.pack()
btn = Button(frame_top, text="Показать факты", command=get_facts)
btn.pack()
info = Text(frame_bottom, bg="#ffb700", font=12, wrap=WORD)
info.pack(fill=BOTH, expand=True)
info.insert("1.0", "Введите город")
root.mainloop()