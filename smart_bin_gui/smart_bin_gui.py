import time
import tkinter as tk
from tkinter import font as tkfont

class SmartBinGUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self)

        self.attributes('-fullscreen', True)
        self.title_font = tkfont.Font(family='Roboto', size=60)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.current_frame = 1
        for i, F in enumerate((InstructionsPage, InfoPage)):
            print (i, F.__name__)
            frame = F(parent=container, controller=self)
            self.frames[i] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

#        self.update_frames()
        self.show_frame(1)

    def show_frame(self, page_index):
        '''Show a frame for the given page name'''
        frame = self.frames[page_index]
        frame.tkraise()

#    def update_frames(self):
#        self.current_frame = self.current_frame ^ 1
#        self.show_frame(self.current_frame)
#        self.after(1000, self.update_frames())

class InstructionsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        TitleText = tk.Label(self, text = "SmartBin v2", fg = 'green', font = controller.title_font)
        TitleText.pack(side = "top", fill = "x", pady = 15)

        TitleText = tk.Label(self, text = "Automatic Sorting Machine\n\n\n", fg = 'black')
        TitleText.config(font=("Roboto", 20))
        TitleText.pack(side = "top", fill = "x")

        InstructionsTitle = tk.Label(self, text = "Instructions:", fg = 'black')
        InstructionsTitle.config(font=("Roboto", 25))
        InstructionsTitle.pack(side = "top", fill = "both")

        Instructions = tk.Label(self, text = "\n1. Pour remaining liquid in the item\n\n2. Place the item inside of the bin\n\n3. Wait for the system to classify and sort your trash\n\n4. Get your reward!",
                                fg = 'black')
        Instructions.config(font=("Roboto", 20))
        Instructions.pack(side = "top", fill = "both")

class InfoPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg = 'black')
        self.controller = controller

        TitleText = tk.Label(self, text = "SmartBin v2", fg = 'green', bg = 'black', font = controller.title_font)
        TitleText.pack(side = "top", fill = "x", pady = 15)

        TitleText = tk.Label(self, text = "Automatic Sorting Machine\n\n\n", fg = 'white', bg = 'black')
        TitleText.config(font=("Roboto", 20))
        TitleText.pack(side = "top", fill = "x")

        c = tk.Canvas(self, width=500, height=500, bg = 'black', bd = 0)
        c.create_arc((500,500, 50, 50), fill="#FAF402", outline="#FAF402", start=self.prop(0), extent = self.prop(200))
        c.create_arc((500,500, 50, 50), fill="#2BFFF4", outline="#2BFFF4", start=self.prop(200), extent = self.prop(400))
        c.create_arc((500,500, 50, 50), fill="#E00022", outline="#E00022", start=self.prop(600), extent = self.prop(50))
        c.create_arc((500,500, 50, 50), fill="#7A0871", outline="#7A0871", start=self.prop(650), extent = self.prop(200))
        c.create_arc((500,500, 50, 50), fill="#294994", outline="#294994", start=self.prop(850), extent = self.prop(150))
        c.pack(side = "top", fill = "x")

    def prop(self, n):
        return 360.0*n / 100

def displaySensor(assigned_bin, is_bin_full):
    if is_bin_full:
        label = tk.Label(display, textVariable = assigned_bin, width=40, fg="yellow", bg = "red")
    else:
        label = tk.Label(display, textVariable = assigned_bin, width=40, fg="yellow", bg = "green")

if __name__ == '__main__':
    app = SmartBinGUI()
    app.mainloop()
