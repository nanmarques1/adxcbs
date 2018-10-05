from tkinter import *
from tkinter import filedialog
import subprocess as sub


class FlashDevicePopup:

    def __init__(self):

        top = Toplevel()
        top.title("FLASH DEVICE")

        group = LabelFrame(top, text="CARRIER", padx=5, pady=5)
        group.pack(padx=10, pady=10)

        self.e = Entry(group)
        self.e.pack()

        self.txt_directory = None

        frame1 = Frame(top)
        frame1.pack()

        self.e_directory = Entry(frame1, width=40)
        self.e_directory.pack(side=LEFT)

        bt_directory = Button(frame1, text="Open Directory", command=self.open_directory)
        bt_directory.pack(side=RIGHT)

        frame2 = Frame(top)
        frame2.pack()

        bt_dismiss = Button(frame2, text="Dismiss", command=top.destroy)
        bt_dismiss.pack(side=LEFT)

        bt_flash = Button(frame2, text="Flash", command=self.flash)
        bt_flash.pack(side=RIGHT)

    def get_carrier(self):
        return self.e.get()

    def open_directory(self):
        self.txt_directory = filedialog.askdirectory()
        self.e_directory.insert(0, self.txt_directory)

    def flash(self):
        self.get_carrier()
        result = sub.check_output(['./scripts/script_flash_device.sh ' + self.txt_directory +
                                   ' ' + self.get_carrier()], shell=True)
        print(result)