import tkinter as tk
import tkinter.font

window = tk.Tk()

font = tk.font.Font(size=32)

# 텍스트를 담을 때는 Label 클래스를 이용한다.
label = tk.Label(master=window, text="I am here!", font=font)
label.pack()

# 창의 속성 정하기
window.title("tkinter Example") # 창 제목 정하기 
window.geometry("400x400") # 창 크기 정하기
window.resizable(True,True) # 창 확대/축소 여부정하기
window.mainloop() # 창의 실행을 유지한다.
