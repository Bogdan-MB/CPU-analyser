import tkinter as tk
from tkinter.ttk import Progressbar, Style
from PIL import Image, ImageTk
from tkinter import font
import psutil
import cpuinfo
import clr
import sys
import os
import pyuac
import time
import datetime

clear = 'cls'

dll_path = os.getcwd() + "/OpenHardwareMonitorLib.dll"
sys.path.append(dll_path)
clr.AddReference(r"OpenHardwareMonitorLib")

from OpenHardwareMonitor.Hardware import Computer #for load per core
c = Computer()
c.CPUEnabled = True
c.Open()

def getLoads(c):
    loads = []
    for a in range(0, len(c.Hardware[0].Sensors)):
        loads.append(c.Hardware[0].Sensors[a].get_Value())
        c.Hardware[0].Update()
    return loads

class myCPU:
    name = cpuinfo.get_cpu_info()['brand_raw']
    users = psutil.users()
    logicalCores = psutil.cpu_count(logical=True)
    physicalCores = psutil.cpu_count(logical=False)
    freq = psutil.cpu_freq()
    percentUsage = psutil.cpu_percent(interval=None)
    percentUsagePerCore = psutil.cpu_percent(percpu=True)
    averageLoad = psutil.getloadavg()
    loadPerCore = getLoads(c)
    bootTime = [psutil.boot_time(), datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")]
    
    def get_freq(self):
        self.freq = psutil.cpu_freq()
        return self.freq
    
    def get_percentage_usage(self):
        self.percentUsage = psutil.cpu_percent(interval=0.1)
        return self.percentUsage
    
    def get_percent_per_core(self):
        self.percentUsagePerCore = psutil.cpu_percent(percpu=True)
        return self.percentUsagePerCore
    
    def get_avg_load(self):
        self.averageLoad = psutil.getloadavg()
        return self.averageLoad
    
    def get_load_per_core(self):
        self.loadPerCore = getLoads(c)
        return self.loadPerCore
    
    def get_boot_time(self):
        self.bootTime = [psutil.boot_time(), datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")]
        return self.bootTime
    
    def refreshValues(self):
        self.freq = psutil.cpu_freq()
        self.percentUsage = psutil.cpu_percent(interval=0.1)
        self.percentUsagePerCore = psutil.cpu_percent(interval=0.1, percpu=True)
        self.averageLoad = [x / self.logicalCores * 100 for x in psutil.getloadavg()]
        self.loadPerCore = getLoads(c)
        self.bootTime = [psutil.boot_time(), datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")]
        
    def print_info(self):
        info = (
        f"CPU: {self.name}\n"
        f"Users: {self.users}\n"
        f"Logical Cores: {self.logicalCores}\n"
        f"Physical Cores: {self.physicalCores}\n"
        f"Frequency: {self.freq.current:.2f} MHz\n"
        f"CPU Usage: {self.percentUsage:.2f}%\n"
        f"Boot Time: {self.bootTime[1]}\n"
        )
        return info


cpu = myCPU()

root = tk.Tk()
root.geometry('700x400')
root.title('PyCPU Monitor')
root.resizable(False, False)
title_font = ('Segoe UI Semibold', 30)

def set_background(frame, image_path):
    image = Image.open(image_path)
    image = image.resize((700, 400))
    bg_image = ImageTk.PhotoImage(image)

    bg_label = tk.Label(frame, image=bg_image)
    bg_label.image = bg_image
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

def update_progress_bar(progress, max_value=100):
    def update():
        if not progress.winfo_exists():
            return  

        current_value = progress['value']
        if current_value < max_value:
            progress['value'] = current_value + 10
        else:
            progress['value'] = 0  

        if progress.active:
            progress.after(500, update)

    update()


def start_progress_bar(frame, style_name="blue.Horizontal.TProgressbar"):
    style = Style()
    style.theme_use('default')
    style.configure(style_name, troughcolor='#050A30', background='#20E5F6', thickness=30)

    progress = Progressbar(frame, orient=tk.HORIZONTAL, length=300, mode='determinate', style=style_name)
    progress.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    progress.active = True

    update_progress_bar(progress)
    return progress


def update_labels(labels, values):
    for label, value in zip(labels, values):
        label.config(text=str(value))

current_frame = None

def home_page():
    global current_frame
    if current_frame:
        current_frame.destroy()

    home_frame = tk.Frame(main_frame)
    set_background(home_frame, 'homedesign.png')
    lb = tk.Label(home_frame, text='PyCPU Monitor', font=title_font, fg='#20E5F6', bg='#050A30')
    lb.pack()
    home_frame.pack(fill='both', expand=True)
    current_frame = home_frame


def page1_page():
    global current_frame
    if current_frame:
        current_frame.destroy()

    page1_frame = tk.Frame(main_frame)
    set_background(page1_frame, 'pagedesign.png')
    lb = tk.Label(page1_frame, text='Frequency', font=title_font, fg='#20E5F6', bg='#050A30')
    lb.pack()

    freq_label = tk.Label(page1_frame, font=('Arial', 12), bg='#050A30', fg='#20E5F6')
    freq_label.pack(pady=20)

    freq_progress = start_progress_bar(page1_frame, "blue.Horizontal.TProgressbar")

    def update_freq():
        if not page1_frame.active:
            return
        cpu.refreshValues()
        freq = cpu.get_freq()[0]
        freq_label.config(text=f"Frequency: {freq:.2f} MHz")
        freq_progress['value'] = (freq / cpu.freq.max) * 100  
        root.after(500, update_freq)

    page1_frame.active = True
    update_freq()
    page1_frame.pack(fill='both', expand=True)
    current_frame = page1_frame

def page2_page():
    global current_frame
    if current_frame:
        current_frame.destroy()

    page2_frame = tk.Frame(main_frame)
    set_background(page2_frame, 'pagedesign.png')
    lb = tk.Label(page2_frame, text='CPU utilization', font=title_font, fg='#20E5F6', bg='#050A30')
    lb.pack()

    utilization_label = tk.Label(page2_frame, font=('Arial', 12), bg='#050A30', fg='#20E5F6')
    utilization_label.pack(pady=20)

    utilization_progress = start_progress_bar(page2_frame, "blue.Horizontal.TProgressbar")

    def update_utilization():
        if not page2_frame.active:
            return
        cpu.refreshValues()
        utilization = cpu.get_percentage_usage()
        utilization_label.config(text=f"CPU Utilization: {utilization:.2f}%")
        utilization_progress['value'] = utilization
        root.after(500, update_utilization)

    page2_frame.active = True
    update_utilization()
    page2_frame.pack(fill='both', expand=True)
    current_frame = page2_frame

def page3_page():
    global current_frame
    if current_frame:
        current_frame.destroy()

    page3_frame = tk.Frame(main_frame)
    set_background(page3_frame, 'pagedesign.png')
    lb = tk.Label(page3_frame, text='Core utilization', font=title_font, fg='#20E5F6', bg='#050A30')
    lb.pack()

    core_utilization_labels = []
    for i in range(cpu.logicalCores):
        core_utilization_labels.append(tk.Label(page3_frame, font=('Arial', 12), bg='#050A30', fg='#20E5F6'))
        core_utilization_labels[-1].pack(pady=2)

    def update_core_utilization():
        cpu.refreshValues()
        percent_per_core = cpu.get_percent_per_core()
        for i, label in enumerate(core_utilization_labels):
            label.config(text=f"Core {i + 1} Utilization: {percent_per_core[i]:.2f}%")
        root.after(500, update_core_utilization)
    
    update_core_utilization()
    page3_frame.pack(fill='both', expand=True)
    current_frame = page3_frame

def page4_page():
    global current_frame
    if current_frame:
        current_frame.destroy()

    page4_frame = tk.Frame(main_frame)
    set_background(page4_frame, 'pagedesign.png')
    lb = tk.Label(page4_frame, text='Load', font=title_font, fg='#20E5F6', bg='#050A30')
    lb.pack()

    core_loads_labels = []
    for i in range(cpu.logicalCores):
        core_loads_labels.append(tk.Label(page4_frame, font=('Arial', 12), bg='#050A30', fg='#20E5F6'))
        core_loads_labels[-1].pack(pady=2)

    def update_core_load():
        cpu.refreshValues()
        load_per_core = cpu.get_load_per_core()
        for i, label in enumerate(core_loads_labels):
            if i < len(load_per_core):
                label.config(text=f"Core {i + 1} Load: {load_per_core[i]:.2f}%")
        root.after(500, update_core_load)

    load_label = tk.Label(page4_frame, font=('Arial', 12), bg='#050A30', fg='#20E5F6')
    load_label.pack(pady=20)

    def update_load():
        cpu.refreshValues()
        load_label.config(text=f"Load Average: {cpu.get_avg_load()}")
        root.after(500, update_load)
    
    update_load()
    update_core_load()
    page4_frame.pack(fill='both', expand=True)
    current_frame = page4_frame

def page5_page():
    global current_frame
    if current_frame:
        current_frame.destroy()

    page5_frame = tk.Frame(main_frame)
    set_background(page5_frame, 'pagedesign.png')
    lb = tk.Label(page5_frame, text='General', font=title_font, fg='#20E5F6', bg='#050A30')
    lb.pack()

    all_label = tk.Label(page5_frame, font=('Arial', 12), bg='#050A30', fg='#20E5F6')
    all_label.pack(pady=20,padx=20)

    def update_general():
        cpu.refreshValues()
        all_label.config(text=f"{cpu.print_info()}")
        root.after(500, update_general)

    
    update_general()
    page5_frame.pack(fill='both', expand=True)
    current_frame = page5_frame


def hide_indicators():
    home_indicate.config(bg='#050929')
    page1_indicate.config(bg='#050929')
    page2_indicate.config(bg='#050929')
    page3_indicate.config(bg='#050929')
    page4_indicate.config(bg='#050929')
    page5_indicate.config(bg='#050929')

def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()

def indicate(lb, page):
    hide_indicators()
    lb.config(bg='#158aff')
    delete_pages()

    if current_frame and hasattr(current_frame, 'active'):
        current_frame.active = False

    page()

options_frame = tk.Frame(root, bg='#050929')

btnFont = font.Font(family="Arial", size=12, weight="bold")

home_btn = tk.Button(options_frame, text='Home', font=btnFont, fg='#073246', bd=0, bg='#c3c3c3', command=lambda: indicate(home_indicate, home_page))
home_btn.place(x=10, y=10)

home_indicate = tk.Label(options_frame, text='', bg='#335f73')
home_indicate.place(x=3, y=10, width=5, height=40)

page1_btn = tk.Button(options_frame, text='Frequency', font=btnFont, fg='#073246', bd=0, bg='#c3c3c3', command=lambda: indicate(page1_indicate, page1_page))
page1_btn.place(x=10, y=60)

page1_indicate = tk.Label(options_frame, text='', bg='#335f73')
page1_indicate.place(x=3, y=60, width=5, height=40)

page2_btn = tk.Button(options_frame, text='CPU utilization', font=btnFont, fg='#073246', bd=0, bg='#c3c3c3', command=lambda: indicate(page2_indicate, page2_page))
page2_btn.place(x=10, y=110)

page2_indicate = tk.Label(options_frame, text='', bg='#335f73')
page2_indicate.place(x=3, y=110, width=5, height=40)

page3_btn = tk.Button(options_frame, text='Core utilization', font=btnFont, fg='#073246', bd=0, bg='#c3c3c3', command=lambda: indicate(page3_indicate, page3_page))
page3_btn.place(x=10, y=160)

page3_indicate = tk.Label(options_frame, text='', bg='#335f73')
page3_indicate.place(x=3, y=160, width=5, height=40)

page4_btn = tk.Button(options_frame, text='Load & Core loads', font=btnFont, fg='#073246', bd=0, bg='#c3c3c3', command=lambda: indicate(page4_indicate, page4_page))
page4_btn.place(x=10, y=210)

page4_indicate = tk.Label(options_frame, text='', bg='#335f73')
page4_indicate.place(x=3, y=210, width=5, height=40)

page5_btn = tk.Button(options_frame, text='Generals', font=btnFont, fg='#073246', bd=0, bg='#c3c3c3', command=lambda: indicate(page5_indicate, page5_page))
page5_btn.place(x=10, y=260)

page5_indicate = tk.Label(options_frame, text='', bg='#335f73')
page5_indicate.place(x=3, y=260, width=5, height=40)


options_frame.pack(side='left')
options_frame.pack_propagate(False)
options_frame.configure(width=200, height=400)

main_frame = tk.Frame(root, highlightbackground='black', highlightthickness=2)
set_background(main_frame, 'homedesign.png')
main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=400, width=700)
home_page()
root.mainloop()
