import tkinter
import requests
import bs4
import random


c1 = "#f4ecd8"
c2 = "#4b2e2e"
def robaee(num=random.randint(1, 178)):
    try:
        url = f"https://ganjoor.net/khayyam/robaee/sh{num}"
        res = requests.get(url, timeout=5)
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, "html.parser")
        m1 = soup.find_all("div", class_="m1")
        m2 = soup.find_all("div", class_="m2")


        if not m1 or not m2 or len(m1) < 2 or len(m2) < 2:
            return "!ساختار سایت تغییر کرده یا شعر پیدا نشد"

        text = f"\n{m1[0].text}  /  {m2[0].text}\n\n{m1[1].text}  /  {m2[1].text}\n\nرباعی شماره: {num}"
        return text

    except requests.exceptions.Timeout:
        return "!اتصال به سایت بیش از حد طول کشید"
    except requests.exceptions.RequestException:
        return f"!خطا در اتصال"
    except Exception:
        return f"!خطای غیرمنتظره"

 
def repet():
    lb.config(text=robaee(random.randint(1, 178)))


root = tkinter.Tk()
root.configure(bg=c1)
root.title("Khayyam")
root.minsize(850, 280)
root.maxsize(850, 280)


lb = tkinter.Label(root, text=robaee(random.randint(1, 178)), anchor="center", justify="center",font=("Arial", 24))
lb.configure(bg=c1, fg=c2)
lb.pack()

btn = tkinter.Button(root, text="شعر تصادفی", width=15, height=2, command=repet)
btn.place(x=850-120-10, y=280-50-10)
btn.configure(bg=c1, fg=c2)


root.mainloop()