import time
import tkinter as tk
from tkinter import font as tkfont
from proximity_sensor import ProximitySensor
from mock_hopper import CoinHopper

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
        self.text = self.canvas.create_text((160, 55), text = assigned_bin, fill = "white", font = tkfont.Font(family='Roboto', size=22))

    def update(self):
        if self.sensor.is_bin_full():
            self.canvas.itemconfig(self.rectangle, fill = "red")
            return True
        else:
            self.canvas.itemconfig(self.rectangle, fill = "green")
            return False

# TODO: make this a strategy pattern(?) with bin indicator
class StatusIndicator():
    def __init__(self, assigned_bin, canvas_position, canvas_container):
        # bin name
        self.assigned_bin = assigned_bin

        # gui canvas
        self.canvas = tk.Canvas(canvas_container, width = 320, height = 100)
        self.rectangle = self.canvas.create_rectangle(0, 0, 320, 100, outline = "black", fill = "green")
        self.canvas.pack(side = "top", pady = canvas_position)
        self.text = self.canvas.create_text((160, 55), text = self.assigned_bin, fill = "white", font = tkfont.Font(family='Roboto', size=18))

    def update(self, is_bin_full):
        if True in is_bin_full:
            self.canvas.itemconfig(self.rectangle, fill = "red")
            self.canvas.itemconfig(self.text, text="Maintenance Mode")
        else:
            self.canvas.itemconfig(self.rectangle, fill = "green")
            self.canvas.itemconfig(self.text, fill = "white", text=self.assigned_bin)

class CoinIndicator():
    def __init__(self, assigned_bin, sensor_pin, relay_pin, canvas_position, canvas_container, side = "top"):
        # bin name
        self.assigned_bin = assigned_bin
        self.side = side

        # sensor object
        self.sensor_pin = sensor_pin
        self.relay_pin = relay_pin
        self.hopper = CoinHopper(sensor_pin, relay_pin)

        # gui canvas
        self.canvas = tk.Canvas(canvas_container, width = 320, height = 100)
        self.rectangle = self.canvas.create_rectangle(0, 0, 320, 100, outline = "black", fill = "green")
        self.canvas.pack(side = self.side, pady = canvas_position)
        self.text = self.canvas.create_text((160, 55), text = self.assigned_bin, fill = "white", font = tkfont.Font(family='Roboto', size=18))

    def update(self):
        if self.hopper.drop_coin():
            self.canvas.itemconfig(self.rectangle, fill = "green")
            self.canvas.itemconfig(self.text, fill = "white", text=self.assigned_bin)
            return False
        else:
            self.canvas.itemconfig(self.rectangle, fill = "red")
            self.canvas.itemconfig(self.text, text="REFILL COINS")
            return True

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
        base_container.grid_rowconfigure(0, weight=1)
        base_container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for i, F in enumerate((StatusFrame, InstructionsFrame)):
            frame = F(parent=base_container, controller = self)
            self.frames[i] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row = 0, column = 0, sticky = 'nsew')

        self.time_shown = 0
        self.page_index = 1
        self.show_frame(self.page_index)

    def show_frame(self, page_index):
        self.time_shown = time.time()
        '''Show a frame for the given page name'''
        self.page_index = page_index ^ 1
        frame = self.frames[self.page_index]
        frame.tkraise()

    def update(self):
#        if (time.time() - self.time_shown) >= 15:
#            self.show_frame(self.page_index)
        self.frames[0].update()
        self.after(3000, self.update)

class StatusFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        title_container = tk.Frame(self, width = 100, height = 100)
        title_container.pack(side = "top", fill = "x", pady = (20, 0))

        status_container = tk.Frame(self)
        status_container.pack(side = "top", fill = "both", expand = True)

        left_status_container = tk.Frame(status_container, width = 500)
        left_status_container.pack(side = "left", fill = "both", padx = (110, 60))

        center_status_container = tk.Frame(status_container, width = 500)
        center_status_container.pack(side = "left", fill = "both", padx = 60)

        right_status_container = tk.Frame(status_container, width = 500)
        right_status_container.pack(side = "left", fill = "both", padx = (60, 110))

        TitleText = tk.Label(title_container, text = "SmartBin v2", fg = 'green', font = controller.title_font)
        TitleText.pack(side = "top", fill = "x")

        TitleText = tk.Label(title_container, text = "Automatic Sorting Machine", fg = 'black')
        TitleText.config(font=("Roboto", 15))
        TitleText.pack(side = "top", fill = "x")

        self.status_indicator    = StatusIndicator("Ready for Trash", (30, 0), center_status_container)

        self.coin_indicator = CoinIndicator("I got money", 16, 12, (0, 130), center_status_container, side = "bottom")

        # bin                   = BinIndicator("name",               trigger_pin, echo_pin, position, container)
        self.aluminum_can_bin   = BinIndicator("ALUMINUM CANS",      14, 15, (143, 0), left_status_container)
        self.plastic_bottle_bin = BinIndicator("PLASTIC BOTTLES",    25, 8,  (100, 0), left_status_container)
        self.paper_cup_bin      = BinIndicator("PAPER CUPS",         23, 24, (143, 0), right_status_container)
        self.unclassified_bin   = BinIndicator("UNCLASSIFIED ITEMS", 7,  1,  (100, 0), right_status_container)

    def update(self):
        bin_is_full = []
        for bin in (self.aluminum_can_bin,
                    self.plastic_bottle_bin,
                    self.paper_cup_bin,
                    self.unclassified_bin):
            bin_is_full.append(bin.update())

        bin_is_full.append(self.coin_indicator.update())
        self.status_indicator.update(bin_is_full)

class InstructionsFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        title_container = tk.Frame(self, width = 100, height = 100)
        title_container.pack(side = "top", fill = "x", pady = (20, 0))

        instructions_container = tk.Frame(self)
        instructions_container.pack(side = "top", fill = "both", expand = True)

        TitleText = tk.Label(title_container, text = "SmartBin v2", fg = 'green', font = controller.title_font)
        TitleText.pack(side = "top", fill = "x")

        TitleText = tk.Label(title_container, text = "Automatic Sorting Machine", fg = 'black')
        TitleText.config(font=("Roboto", 15))
        TitleText.pack(side = "top", fill = "x")

        InstructionsTitle = tk.Label(instructions_container, text = "INSTRUCTIONS:", fg = 'black')
        InstructionsTitle.config(font=("Roboto", 30))
        InstructionsTitle.pack(side = "top", fill = "both", pady = (100, 0))

        Instructions = tk.Label(instructions_container, text = "\n1. Pour remaining liquid in the item\n\n2. Place the item inside of the bin\n\n3. Wait for the system to classify\n\nand sort your trash\n\n4. Get your reward!",
                                fg = 'black')
        Instructions.config(font=("Roboto", 25))
        Instructions.pack(side = "top", fill = "both")

if __name__ == '__main__':
    app = SmartBinGUI()
    app.update()
    app.mainloop()
