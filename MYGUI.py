from tkinter import *
import tkinter.font as tkFont

class GUI: 
    def __init__(self, root):
        #ใส่ข้อความbinary
        ft = tkFont.Font(family='Times',size=68)
        mylabel1 = Label(text = "BINARY SEARCH",font = ft).place(x=110,y=20,width=761,height=85)
        mylabel2 = Label(text = "",font = ft, bg = "#00babd").place(x=30,y=150,width=900,height=45)
        mylabel3 = Label(text = "",font = ft, bg = "#00babd").place(x=30,y=250,width=900,height=45)

        #ปุ่ม
        ft = tkFont.Font(family='Times',size = 36)
        start = Button(root,text="START",font = ft,bg = "#90ee90").place(x=50,y=370,width=200,height=100)
        result = Button(root,text="RESULT",font= ft, bg = "#d35f5f").place(x=500,y=370,width=200,height=100)

        #รับtext
        input1 = StringVar()
        result1 = StringVar()
        ft = tkFont.Font(family='Times',size=24)
        Text3 = Entry(root,textvariable=input1, font= ft).place(x=270,y=400,width=200,height=50)    
        Text4 = Entry(root,textvariable=result1, font= ft).place(x=720,y=400,width=200,height=50)

        root.geometry("980x500+300+150")
        root.mainloop()
        if __name__ == "__main__":
            root = Tk.Tk()
            GUI = GUI(root)
            root.mainloop()
       