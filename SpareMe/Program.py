from tkinter import *
from FlashDevice import FlashDevicePopup
import subprocess as sub


class App:

    def __init__(self, master):

        group = LabelFrame(master, text="CHANGE CARRIER", padx=5, pady=5)
        group.pack(padx=10, pady=10)

        frame0 = Frame(master)
        frame0.pack()

        frame1 = Frame(master)
        frame1.pack()

        frame2 = Frame(master)
        frame2.pack()

        group_evidence = LabelFrame(master, text="EVIDENCES", padx=5, pady=5)
        group_evidence.pack(padx=10, pady=10)

        frame3 = Frame(master)
        frame3.pack()

        self.e = Entry(group)
        self.e.pack()

        bt_restart = Button(frame1, text="RESTART", command=self.restart)
        bt_restart.pack(side=LEFT)

        bt_bootloader = Button(frame1, text="BOOTLOADER", command=self.bootloader)
        bt_bootloader.pack(side=LEFT)

        bt_fdr = Button(frame1, text="FDR", command=self.fdr)
        bt_fdr.pack(side=LEFT)

        bt_flash = Button(frame1, text="FLASH", command=self.flash_device)
        bt_flash.pack(side=LEFT)

        bt_single_sim = Button(frame2, text="SINGLE SIM", command=self.single_sim)
        bt_single_sim.pack(side=LEFT)

        bt_dual_sim = Button(frame2, text="DUAL SIM", command=self.dual_sim)
        bt_dual_sim.pack(side=LEFT)

        bt_get_info = Button(frame2, text="GET INFO", command=self.get_info)
        bt_get_info.pack(side=LEFT)

        bt_take_screenshot = Button(group_evidence, text="SCREENSHOT", command=self.get_info)
        bt_take_screenshot.pack(side=LEFT)

        bt_make_video = Button(group_evidence, text="VIDEO", command=self.get_info)
        bt_make_video.pack(side=LEFT)

        bt_generate_logs = Button(group_evidence, text="LOGS", command=self.get_info)
        bt_generate_logs.pack(side=LEFT)

        bt_quit = Button(frame3, text="QUIT", fg="red", command=frame3.quit)
        bt_quit.pack(side=LEFT)

    def get_carrier(self):
        return self.e.get()

    def delete_carrier(self):
        self.e.delete(0, END)

    def restart(self):
        sub.check_output('adb reboot', shell=True)

    def bootloader(self):
        sub.check_output('adb reboot bootloader', shell=True)

    def fdr(self):
        self.get_carrier();
        result = sub.check_output(['./scripts/script_fdr.sh %s' % self.get_carrier()], shell=True)
        print(result)
        self.delete_carrier()

    def single_sim(self):
        self.get_carrier();
        result = sub.check_output(['./scripts/script_single_sim.sh %s' % self.get_carrier()], shell=True)
        print(result)
        self.delete_carrier()

    def dual_sim(self):
        self.get_carrier();
        result = sub.check_output(['./scripts/script_dual_sim.sh %s' % self.get_carrier()], shell=True)
        print(result)
        self.delete_carrier()

    def get_info(self):
        result = sub.check_output([str('./scripts/script_get_info.sh')], shell=True)

        top = Toplevel()
        top.title("GET INFO")

        txt = Text(top, height=10, width=80)
        txt.pack()

        button = Button(top, text="Dismiss", command=top.destroy)
        button.pack()

        txt.insert(END, result)

    def flash_device(self):
        flash_popup = FlashDevicePopup()


root = Tk()
root.title("ADX CBS")

app = App(root)

root.mainloop()
