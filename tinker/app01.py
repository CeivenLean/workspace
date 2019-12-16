import tkinter.messagebox
#from tkinter.constants import *
from tkinter import *

# 创建一个窗口对象并初始设置
app = Tk()
app.title("测试窗口")
app.geometry("400x200") # 注意，这是小写x
# app.config(bg="red")

# 在窗口内设置一个标签 Label
label = Label(app, text="hellp,windows")
label.pack()



label_str = StringVar()
label2 = Label(app, textvariable=label_str)
label2.pack()

def button_cmd():
    label_str.set("xxxxxxxxx")

# 创建一个按钮 Button
button = Button(app, text="确定", command=lambda : label_str.set("xxxxxxxxx"))
button.pack(side="left")

# 创建一个按钮 Button
button2 = Button(app, text="清除", command=lambda : label_str.set(""))
button2.pack(side="right")


msg = tkinter.messagebox
msg.showinfo('info','yes')


# 程序循环不关闭，直到手动关闭窗口
app.mainloop()