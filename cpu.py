from tkinter import *
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

#for a in range(0, len(c.Hardware[0].Sensors)):
    #    print(c.Hardware[0].Sensors[a].Identifier)
    #    if "/temperature" in str(c.Hardware[0].Sensors[a].Identifier):
    #        print(c.Hardware[0].Sensors[a].get_Value())
    #        c.Hardware[0].Update()

def getLoads(c):
    loads = []
    for a in range(0, len(c.Hardware[0].Sensors)):
        loads.append(c.Hardware[0].Sensors[a].get_Value())
        c.Hardware[0].Update()
    return loads

class myCPU:
    name = cpuinfo.get_cpu_info()['brand_raw']
    users = psutil.users()
    logicalCores = psutil.cpu_count(logical = True)
    physicalCores = psutil.cpu_count(logical = False) #these never change
    freq = psutil.cpu_freq() #current, min & max freq on CPU overall
    percentUsage = psutil.cpu_percent(interval = None) #list of usage on the CPU as a whole
    percentUsagePerCore = (psutil.cpu_percent(percpu=True)) #list of percentage of usage for each core on a CPU
    averageLoad = psutil.getloadavg() #list with average load from 5, 10, and 15m since the program started
    loadPerCore = getLoads(c) #load per core
    bootTime = [psutil.boot_time(), datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")]
    def print(self):
        print("Name: ", self.name)
        print("CPU users: ", end = "")
        for user in self.users:
            print(user[0], end = " ")
        print()
        print("Logical Cores: ", self.logicalCores)
        print("Physical Cores: ", self.physicalCores)
        print("Nominal frequency: ", self.freq[0],"GHz", "\nMin frequency: ", self.freq[1],"GHz", "\nMax frequency: ", self.freq[2],"GHz")
        print("CPU utilization: ", self.percentUsage)
        print("Core usage: ", end = "")
        for x in range(len(self.percentUsagePerCore)):
            print("Core#", x + 1, " ", self.percentUsagePerCore[x],"%", end=" ")
        print()
        print("Average load in the last: 5m - %.2f" % self.averageLoad[0], " 10m - %.2f" % self.averageLoad[1], " 15m - %.2f" % self.averageLoad[2])
        print("Load per Core: ", end = "")
        for x in range(len(self.loadPerCore)):
            print("Core#", x + 1, " %.2f" % self.loadPerCore[x], end = " ")
        print()
        print("Time since epoch: ", self.bootTime[0], " approximately ", self.bootTime[1])
    def refreshValues(self): #for updating values
        self.freq = tuple(psutil.cpu_freq())
        self.percentUsage = psutil.cpu_percent(interval = 0.1)
        self.percentUsagePerCore = psutil.cpu_percent(interval = 0.1, percpu = True)
        self.averageLoad = [x / self.logicalCores * 100 for x in psutil.getloadavg()] #average load given back in % instead of number < 1
        self.bootTime = psutil.boot_time()
        self.loadPerCore = getLoads(c)
        self.bootTime = [psutil.boot_time(), datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")]
    def printWindow(self):
        while True:
            self.print()
            self.refreshValues()
            time.sleep(2)
            os.system(clear)
def main():
    if not pyuac.isUserAdmin():
        pyuac.runAsAdmin()
    cpu = myCPU()
    cpu.refreshValues()
if __name__ == "__main__":
     main()
     import interface