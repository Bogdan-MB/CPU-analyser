from tkinter import *
import psutil
import cpuinfo
import clr
import sys
import os
import wmi


dll_path = os.getcwd() + "/OpenHardwareMonitorLib.dll"
sys.path.append(dll_path)
clr.AddReference(r"OpenHardwareMonitorLib")

from OpenHardwareMonitor.Hardware import Computer
c = Computer()
c.CPUEnabled = True # get the Info about CPU
c.Open()
w = wmi.WMI(namespace="root/wmi")

def getLoads(c):
    loads = []
    for a in range(0, len(c.Hardware[0].Sensors)):
        loads.append(c.Hardware[0].Sensors[a].get_Value())
        c.Hardware[0].Update()
    return loads

class myCPU:
    name = cpuinfo.get_cpu_info()['brand_raw']
    logicalCores = psutil.cpu_count(logical = True)
    physicalCores = psutil.cpu_count(logical = False) #these never change
    freq = psutil.cpu_freq() #current, min & max freq on CPU overall
    percentUsage = psutil.cpu_percent(interval = None) #list of usage on the CPU as a whole
    percentUsagePerCore = (psutil.cpu_percent(percpu=True)) #list of percentage of usage for each core on a CPU
    averageLoad = psutil.getloadavg() #list with average load from 5, 10, and 15m since the program started
    loadPerCore = getLoads(c)
    bootTime = psutil.boot_time()
    temperature = w.MSAcpi_ThermalZoneTemperature()[0].CurrentTemperature / 10 - 273.15
    def refreshValues(self): #for updating values
        self.freq = tuple(psutil.cpu_freq())
        self.percentUsage = psutil.cpu_percent(interval = 0.1)
        self.percentUsagePerCore = psutil.cpu_percent(interval = 0.1, percpu = True)
        self.averageLoad = [x / self.logicalCores * 100 for x in psutil.getloadavg()] #average load given back in % instead of number < 1
        self.bootTime = psutil.boot_time()
        self.temperature = w.MSAcpi_ThermalZoneTemperature()[0].CurrentTemperature / 10 - 273.15
def main():
    #for a in range(0, len(c.Hardware[0].Sensors)):
    #    print(c.Hardware[0].Sensors[a].Identifier)
    #    if "/temperature" in str(c.Hardware[0].Sensors[a].Identifier):
    #        print(c.Hardware[0].Sensors[a].get_Value())
    #        c.Hardware[0].Update()
    cpu = myCPU()
    cpu.refreshValues()
    print(cpu.temperature)
    print(cpu.freq[0], cpu.freq[1], cpu.freq[2])
    # #init window
    # window = Tk()
    # window.title("Analizator CPU")
    # window.config(background = 'white')
    # frame = ttk.Frame(window, padding = 10)
    # frame.grid()
    # #CPU title
    # cpu_title = Label(window, text=cpu.name, font="arial 24").grid(column=2, row=2) #example gives CPU name
    # window.mainloop()
if __name__ == "__main__":
     main()
     import interface