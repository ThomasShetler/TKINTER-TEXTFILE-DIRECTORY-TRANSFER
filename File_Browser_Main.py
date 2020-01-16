from tkinter import *
import File_Browser_GUI
import File_Browser_Function

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.master.minsize(600, 200)
        self.master.maxsize(600, 200)
        self.master.title('Check Files')
        self.master.config(bg='#f0f0f0')

        arg = self.master
        File_Browser_GUI.load_gui(self)


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
    File_Browser_Function.list_directory()