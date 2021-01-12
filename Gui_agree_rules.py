from tkinter import *
from tkinter import ttk

def main():
    root = Tk()
    button = ttk.Button(root, text = "NEXT")
    button.pack()
    ch_button = ttk.Checkbutton(root, text = "Did you agree?")
    ch_button.pack()
    def callback():
        if ch_button.instate(["selected"]): print("success")
        else: print("choose agree")

    button.config(command=callback)
    root.mainloop()

if __name__ == "__main__": main()
