from tkinter import *
from tkinter import ttk
class GUI_Python:
       def __init__(self):
                     self.root = Tk()
                     try:
                            self.list_ = ["", self.ent1, self.ent2]
                     except:
                            pass
                     self.names = ["", "url:", "word:"]
                     self.root.geometry("500x500")
                     self.root.resizable(0, 0)
                     self.root.title("")
                     photo = PhotoImage(file="image.png")
                     self.root.iconphoto(False, photo)
                     for i in range(1, 3):
                            try:
                                   self.nt = self.list_[i]
                                   self.lb = self.names[i]
                            except:
                                    pass
                            Label(self.root, text=self.lb, font="Arial bold 14").grid(row=i, column=1)
                            nt = ttk.Entry(self.root, font="Cascandia 14")
                            nt.grid(row=i, column=2)
                     self.root.mainloop()
                     
       def get_entry(self):

                     self.get_ent1 = self.ent1.get()
                     self.get_ent2 = self.ent2.get()

GUI_Python()

