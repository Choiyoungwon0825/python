import tkinter as tk
import tkinter.font
import random as rd

window = tk.Tk()
lotto_range = range(1,46)

def buttonClick():
    font = tk.font.Font(size=20)
    label = tk.Label(master=window, text=str(rd.sample(lotto_range,6)), font=font)
    label.pack()

window.title("로또 번호 뽑기 프로그램")
window.geometry("400x400")
window.resizable(True,True)

button = tkinter.Button(window, overrelief="solid", text="번호확인",
                        width=16, command=buttonClick, repeatdelay=1000, 
                        repeatinterval=10)
button.pack(side="top")

window.mainloop()
