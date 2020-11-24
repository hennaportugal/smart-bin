import time
import tkinter as tk
from tkinter import font as tkfont
from mock_sensor import ProximitySensor

class SmartBinGUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self)

        self.attributes('-fullscreen', True)
        self.title_font = tkfont.Font(family='Roboto', size=60)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        base_container= tk.Frame(self)
        base_container.pack(fill = "both", expand = True)
        # base_container.grid_rowconfigure(0, weight=1)
        # base_container.grid_columnconfigure(0, weight=1)

        title_container = tk.Frame(base_container, width = 100, height = 100)
        title_container.pack(side = "top", fill = "x")

        instructions_container = tk.Frame(base_container, width = 700)
        instructions_container.pack(side = "left", fill = "both")
        # instructions_container.grid_rowconfigure(0, weight=1)
        # instructions_container.grid_columnconfigure(0, weight=1)

        status_container = tk.Frame(base_container)
        status_container.pack(side = "right", fill = "both", expand = True)
        # bin_container.grid_rowconfigure(0, weight=1)
        # bin_container.grid_columnconfigure(0, weight=1)

        left_status_container = tk.Frame(status_container, width = 425)
        left_status_container.pack(side = "left", fill = "both")

        center_status_container = tk.Frame(status_container, width = 425)
        center_status_container.pack(side = "left", fill = "both")

        right_status_container = tk.Frame(status_container, width = 425)
        right_status_container.pack(side = "left", fill = "both")

        TitleText = tk.Label(title_container, text = "SmartBin v2", fg = 'green', font = self.title_font)
        TitleText.pack(side = "top", fill = "x", pady = 15)

        TitleText = tk.Label(title_container, text = "Automatic Sorting Machine\n", fg = 'black')
        TitleText.config(font=("Roboto", 20))
        TitleText.pack(side = "top", fill = "x")

        Instructions = tk.Label(instructions_container, text = "\n1. Pour remaining liquid in the item\n\n2. Place the item inside of the bin\n\n3. Wait for the system to classify and sort your trash\n\n4. Get your reward!",
                                fg = 'black')
        Instructions.config(font=("Roboto", 20))
        Instructions.pack(side = "bottom", fill = "both")

        InstructionsTitle = tk.Label(instructions_container, text = "Instructions:", fg = 'black')
        InstructionsTitle.config(font=("Roboto", 25))
        InstructionsTitle.pack(side = "bottom", fill = "both")

        status_indicator = tk.Canvas(center_status_container, width = 400, height = 100)
        status_indicator.create_rectangle(0, 0, 400, 100, outline = "black", fill = "green")
        status_indicator.pack(side = "top", fill = "x")
        # status_indicator.grid(column = 1, row = 0, sticky = "new")

        status_indicator = tk.Canvas(center_status_container, width = 400, height = 100)
        status_indicator.create_rectangle(0, 0, 400, 100, outline = "black", fill = "green")
        status_indicator.pack(side = "bottom", fill = "x", pady = (0, 300))
        # status_indicator.grid(column = 1, row = 0, sticky = "new")

        aluminum_can_bin = tk.Canvas(left_status_container, width = 400, height = 100)
        aluminum_can_bin.create_rectangle(0, 0, 400, 100, outline = "black", fill = "green")
        aluminum_can_bin.pack(side = "top", pady = (150, 0))
# #         status_indicator.grid(column =  3, row = 1, sticky = "w")

        plastic_bottle_bin = tk.Canvas(left_status_container, width = 400, height = 100)
        plastic_bottle_bin.create_rectangle(0, 0, 400, 100, outline = "black", fill = "green")
        plastic_bottle_bin.pack(side = "top", pady = (100, 0))
# #         status_indicator.grid(column =  3, row = 1, sticky = "w")

        paper_cup_bin = tk.Canvas(right_status_container, width = 400, height = 100)
        paper_cup_bin.create_rectangle(0, 0, 400, 100, outline = "black", fill = "green")
        paper_cup_bin.pack(side = "top", pady = (150, 0))
# #         status_indicator.grid(column =  3, row = 1, sticky = "w")

        unclassified_bin = tk.Canvas(right_status_container, width = 400, height = 100)
        unclassified_bin.create_rectangle(0, 0, 400, 100, outline = "black", fill = "green")
        unclassified_bin.pack(side = "top", pady = (100, 0))

        bin_views = [aluminum_can_bin, plastic_bottle_bin, paper_cup_bin, unclassified_bin]
        # print(bin_views.__name__)

       # self.update_sensor_values()

   # def update_sensor_values(self):
   #     self.after(1000, self.update_sensor_values())

#     def displaySensor(assigned_bin, is_bin_full):
#         if is_bin_full:
#             label = tk.Label(display, textVariable = assigned_bin, width=40, fg="yellow", bg = "red")
#         else:
#             label = tk.Label(display, textVariable = assigned_bin, width=40, fg="yellow", bg = "green")

if __name__ == '__main__':
    app = SmartBinGUI()
    app.mainloop()
