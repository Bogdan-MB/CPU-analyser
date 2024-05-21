from tkinter import *
from tkinter import ttk
import psutil
import cpuinfo

class myCPU:
    name = cpuinfo.get_cpu_info()['brand_raw']
    logicalCores = psutil.cpu_count(logical = True)
    physicalCores = psutil.cpu_count(logical = False) #these never change
    freq = tuple(psutil.cpu_freq()) #current, min & max freq
    percentUsage = psutil.cpu_percent(interval = None) #list of usage on the CPU as a whole
    percentUsagePerCore = (psutil.cpu_percent(interval = None, percpu=True)) #list of percentage of usage for each core on a CPU
    averageLoad = psutil.getloadavg() #list with average load from 5, 10, and 15m since the program started
    bootTime = psutil.boot_time()
    def refreshValues(self): #for updating values
        self.freq = tuple(psutil.cpu_freq())
        self.percentUsage = psutil.cpu_percent(interval = 0.1)
        self.percentUsagePerCore = psutil.cpu_percent(interval = 0.1, percpu = True)
        self.averageLoad = [x / self.logicalCores * 100 for x in psutil.getloadavg()] #average load given back in % instead of number < 1
        self.bootTime = psutil.boot_time

cpu = myCPU()

#init window
window = Tk()
window.title("Analizator CPU")
window.config(background = 'white')
frame = ttk.Frame(window, padding = 10)
frame.grid()
#CPU title
cpu_title = Label(window, text=cpu.name, font="arial 24").grid(column=2, row=2) #example gives CPU name

if __name__ == "__main__":
    window.mainloop()