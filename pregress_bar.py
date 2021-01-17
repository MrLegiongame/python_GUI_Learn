from tkinter import *
from tkinter import ttk


def main():
    root = Tk()
    progressnbar = ttk.Progressbar(root, orient=HORIZONTAL, length=200)
    progressnbar.pack()
    progressnbar.config(mode="determinate", maximum=4.0, value=0.0)
    month = StringVar()
    combo_box = ttk.Combobox(root, textvariable = month)
    combo_box.config(value = ("m" , "a" , "b"))
    combo_box.pack()
    ch1 = ttk.Checkbutton(root, text="test 1")
    ch1.pack()
    ch2 = ttk.Checkbutton(root, text="test 2")
    ch2.pack()
    ch3 = ttk.Checkbutton(root, text="test 3")
    ch3.pack()

    def callback():
        v = 0.0
        if ch1.instate(["selected"]):v = 2.0
        if ch2.instate(["selected"]):v = 3.0
        if ch3.instate(["selected"]):v = 4.0
        progressnbar.config(mode="determinate", maximum=4.0, value=v)
    def callback_bind(self):
        v = 0.0
        if month.get() == "a" or month.get() == "b" or month.get() == "m": v = 1.0
        progressnbar.config(mode="determinate", maximum=4.0, value=v)



    ch1.config(command=callback)
    ch2.config(command=callback)
    ch3.config(command=callback)
    combo_box.bind("<<ComboboxSelected>>", callback_bind)
    root.mainloop()


if __name__ == "__main__": main()
