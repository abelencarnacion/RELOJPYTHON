import tkinter as tk
import time
import locale

try:
    locale.setlocale(locale.LC_ALL, "esp")
except:
    locale.setlocale(locale.LC_ALL, "es_ES")

ROOT = tk.Tk()
ROOT.geometry("500x210")
ROOT.title("Abel Encarnacion Hora Actual"),


ROOT.configure(bg="Black")

fecha = time.strftime("%A, %d de %B de %Y")
lblFecha = tk.Label(ROOT, text=fecha, fg="blue",
                    bg="black", font=("Arial", 20,))
                    
                    
lblFecha.pack()
lblReloj = tk.Label(ROOT, text="00:00", fg="blue",
                    bg="black", font=("Arial Black", 50))
lblReloj.pack()


def reloj():
    global hora
    hora = time.strftime("%I:%M:%S %p").lower()
    lblReloj.config(text=hora)
    lblReloj.after(800, reloj)


reloj()

ROOT.mainloop()
