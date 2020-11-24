import time
import tkinter as tk
from tkinter import font as tkfont
from mock_sensor import ProximitySensor

class BinIndicator():
    def __init__(self, assigned_bin, trig_pin, echo_pin, canvas_position, canvas_container):
        # bin name
        self.assigned_bin = assigned_bin

        # sensor object
        self.trig_pin = trig_pin
        self.echo_pin = echo_pin
        self.sensor = ProximitySensor(trig_pin, echo_pin)

        # gui canvas
        self.canvas = tk.Canvas(canvas_container, width = 320, height = 100)
        self.rectangle = self.canvas.create_rectangle(0, 0, 320, 100, outline = "black", fill = "green")
        self.canvas.pack(side = "top", pady = canvas_position)

    def get_assigned_bin(self):
        return self.assigned_bin

    def update(self):
        if self.sensor.is_bin_full():
            self.canvas.itemconfig(self.rectangle, fill = "red")

class SmartBinGUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self)

        self.attributes('-fullscreen', True)
        self.title_font = tkfont.Font(family='Roboto', size=50)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        base_container= tk.Frame(self)
        base_container.pack(fill = "both", expand = True)

        title_container = tk.Frame(base_container, width = 100, height = 100)
        title_container.pack(side = "top", fill = "x", pady = (20, 0))

        # instructions_container = tk.Frame(base_container, width = 700)
        # instructions_container.pack(side = "left", fill = "both")

        status_container = tk.Frame(base_container)
        status_container.pack(side = "top", fill = "both", expand = True)

        left_status_container = tk.Frame(status_container, width = 325)
        left_status_container.pack(side = "left", fill = "both", padx = 10)

        center_status_container = tk.Frame(status_container, width = 325)
        center_status_container.pack(side = "left", fill = "both", padx = 10)

        right_status_container = tk.Frame(status_container, width = 325)
        right_status_container.pack(side = "left", fill = "both", padx = 10)

        TitleText = tk.Label(title_container, text = "SmartBin v2", fg = 'green', font = self.title_font)
        TitleText.pack(side = "top", fill = "x")

        TitleText = tk.Label(title_container, text = "Automatic Sorting Machine", fg = 'black')
        TitleText.config(font=("Roboto", 15))
        TitleText.pack(side = "top", fill = "x")

#         InstructionsTitle = tk.Label(instructions_container, text = "Instructions:", fg = 'black')
#         InstructionsTitle.config(font=("Roboto", 25))
#         InstructionsTitle.pack(side = "top", fill = "both", pady = (300, 0))

#         Instructions = tk.Label(instructions_container, text = "\n1. Pour remaining liquid in the item\n\n2. Place the item inside of the bin\n\n3. Wait for the system to classify and sort your trash\n\n4. Get your reward!",
#                                 fg = 'black')
#         Instructions.config(font=("Roboto", 20))
#         Instructions.pack(side = "top", fill = "both")

        self.status_indicator = tk.Canvas(center_status_container, width = 320, height = 100)
        self.status_indicator.create_rectangle(0, 0, 320, 100, outline = "black", fill = "green")
        self.status_indicator.pack(side = "top", fill = "x", pady = (30, 0))

        self.coin_indicator = tk.Canvas(center_status_container, width = 320, height = 100)
        self.coin_indicator.create_rectangle(0, 0, 320, 100, outline = "black", fill = "green")
        self.coin_indicator.pack(side = "bottom", fill = "x", pady = (0, 100))

        # bin                   = BinIndicator("name",               trigger_pin, echo_pin, position, container)
        self.aluminum_can_bin   = BinIndicator("Aluminum Cans",      14, 15, (143, 0), left_status_container)
        self.plastic_bottle_bin = BinIndicator("Plastic Bottles",    25, 8,  (100, 0), left_status_container)
        self.paper_cup_bin      = BinIndicator("Paper Cups",         23, 24, (143, 0), right_status_container)
        self.unclassified_bin   = BinIndicator("Unclassified Items", 7,  1,  (100, 0), right_status_container)

    def update_sensor_values(self):
        for bin in (self.aluminum_can_bin, self.plastic_bottle_bin, self.paper_cup_bin, self.unclassified_bin):
            bin.update()

        self.after(1000, self.update_sensor_values)

if __name__ == '__main__':
    app = SmartBinGUI()
    app.update_sensor_values()
    app.mainloop()
