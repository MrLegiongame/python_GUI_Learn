from tkinter import *
from tkinter import ttk


def main():
    root = Tk()
    notebook = ttk.Notebook(root)
    notebook.pack()
    frame1 = ttk.Frame(notebook)
    frame2 = ttk.Frame(notebook)
    notebook.add(frame1, text="F1")
    notebook.add(frame2, text="F2")
    button = ttk.Button(frame1, text = "click me")
    button.pack()
    lable = ttk.Label(frame2,text = "HELLO WORLD")
    lable.pack()

    def callback():
        def callback2():
            window.iconify()
        window = Toplevel(root)
        window.title("new window")
        button2 = ttk.Button(window, text = "KILL ME")
        button2.pack()
        button2.config(command=callback2)

    button.config(command=callback)
    root.mainloop()


if __name__ == "__main__": main()
