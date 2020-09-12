from tkinter import *
from tkinter import ttk

root = Tk()

label_text = 'Python Tkinter 라이브러리를 이용한 GUI 만들기'
label = ttk.Label(root, text = label_text)  
label.img = PhotoImage(file = 'Loading.gif')
label.config(image = label.img, compound = 'bottom') 
label.pack()

# Label을 수정하려면 config를 사용하면 된다.

label.config(justify = CENTER)
label.config(font = ('현대하모니 L', 18, 'bold'))
root.mainloop()
