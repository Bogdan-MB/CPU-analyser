import tkinter as tk
from tkinter import *
from tkinter import font

window = tk.Tk()

stylemain=font.Font(size=10)
style1=font.Font(size=10)
style2=font.Font(size=10)
style3=font.Font(size=10)
style4=font.Font(size=10)
style5=font.Font(size=10)
style6=font.Font(size=10)
style7=font.Font(size=10)

main_page=Frame(window)
page1=Frame(window)
page2=Frame(window)
page3=Frame(window)
page4=Frame(window)
page5=Frame(window)
page6=Frame(window)
page7=Frame(window)

main_page.grid(row=0, column=0, sticky="nsew")
page1.grid(row=0, column=0, sticky="nsew")
page2.grid(row=0, column=0, sticky="nsew")
page3.grid(row=0, column=0, sticky="nsew")
page4.grid(row=0, column=0, sticky="nsew")
page5.grid(row=0, column=0, sticky="nsew")
page6.grid(row=0, column=0, sticky="nsew")
page7.grid(row=0, column=0, sticky="nsew")

lbmain=Label(main_page, text="Main este a", font=stylemain)
lbmain.pack(pady=20)

lb1=Label(page1, text="page1 este a", font=style1)
lb1.pack(pady=30)

lb2=Label(page2, text="page2 este a", font=style2)
lb2.pack(pady=40)

lb3=Label(page3, text="page3 este a", font=style3)
lb3.pack(pady=30)

lb4=Label(page4, text="page4 este a", font=style4)
lb4.pack(pady=30)

lb5=Label(page5, text="page5 este a", font=style5)
lb5.pack(pady=30)

lb6=Label(page6, text="page6 este a", font=style6)
lb6.pack(pady=30)

lb7=Label(page7, text="page7 este a", font=style7)
lb7.pack(pady=30)

#button main: main

btn_main1 = Button(main_page, text="Frequency", command=lambda: page1.tkraise(), font=style1)
btn_main2= Button(main_page, text="CPU utilization", command=lambda: page2.tkraise(), font=style2)
btn_main3 = Button(main_page, text="Core utilization", command=lambda: page3.tkraise(), font=style3)
btn_main4 = Button(main_page, text="Load", command=lambda: page4.tkraise(), font=style4)
btn_main5 = Button(main_page, text="Temperature", command=lambda: page5.tkraise(), font=style5)
btn_main6 = Button(main_page, text="Power of consumption", command=lambda: page6.tkraise(), font=style6)
btn_main7 = Button(main_page, text="Speed", command=lambda: page7.tkraise(), font=style7)
btn_main1.pack()
btn_main2.pack()
btn_main3.pack()
btn_main4.pack()
btn_main5.pack()
btn_main6.pack()
btn_main7.pack()

#button frequency: 1

btn_11 = Button(page1, text="Home", command=lambda: main_page.tkraise(), font=stylemain)
btn_12= Button(page1, text="CPU utilization", command=lambda: page2.tkraise(), font=style2)
btn_13 = Button(page1, text="Core utilization", command=lambda: page3.tkraise(), font=style3)
btn_14 = Button(page1, text="Load", command=lambda: page4.tkraise(), font=style4)
btn_15 = Button(page1, text="Temperature", command=lambda: page5.tkraise(), font=style5)
btn_16 = Button(page1, text="Power of consumption", command=lambda: page6.tkraise(), font=style6)
btn_17 = Button(page1, text="Speed", command=lambda: page7.tkraise(), font=style7)
btn_11.pack()
btn_12.pack()
btn_13.pack()
btn_14.pack()
btn_15.pack()
btn_16.pack()
btn_17.pack()

#button CPU utilization: 2

btn_21 = Button(page2, text="Home", command=lambda: main_page.tkraise(), font=stylemain)
btn_22= Button(page2, text="Frequency", command=lambda: page1.tkraise(), font=style1)
btn_23 = Button(page2, text="Core utilization", command=lambda: page3.tkraise(), font=style3)
btn_24 = Button(page2, text="Load", command=lambda: page4.tkraise(), font=style4)
btn_25 = Button(page2, text="Temperature", command=lambda: page5.tkraise(), font=style5)
btn_26 = Button(page2, text="Power of consumption", command=lambda: page6.tkraise(), font=style6)
btn_27 = Button(page2, text="Speed", command=lambda: page7.tkraise(), font=style7)
btn_21.pack()
btn_22.pack()
btn_23.pack()
btn_24.pack()
btn_25.pack()
btn_26.pack()
btn_27.pack()

#button Core utilization: 3

btn_31 = Button(page3, text="Home", command=lambda: main_page.tkraise(), font=stylemain)
btn_32= Button(page3, text="Frequency", command=lambda: page1.tkraise(), font=style1)
btn_33= Button(page3, text="CPU utilization", command=lambda: page2.tkraise(), font=style2)
btn_34 = Button(page3, text="Load", command=lambda: page4.tkraise(), font=style4)
btn_35 = Button(page3, text="Temperature", command=lambda: page5.tkraise(), font=style5)
btn_36 = Button(page3, text="Power of consumption", command=lambda: page6.tkraise(), font=style6)
btn_37 = Button(page3, text="Speed", command=lambda: page7.tkraise(), font=style7)
btn_31.pack()
btn_32.pack()
btn_33.pack()
btn_34.pack()
btn_35.pack()
btn_36.pack()
btn_37.pack()

#button Load: 4

btn_41 = Button(page4, text="Home", command=lambda: main_page.tkraise(), font=stylemain)
btn_42 = Button(page4, text="Frequency", command=lambda: page1.tkraise(), font=style1)
btn_43 = Button(page4, text="CPU utilization", command=lambda: page2.tkraise(), font=style2)
btn_44 = Button(page4, text="Core utilization", command=lambda: page3.tkraise(), font=style3)
btn_45 = Button(page4, text="Temperature", command=lambda: page5.tkraise(), font=style5)
btn_46 = Button(page4, text="Power of consumption", command=lambda: page6.tkraise(), font=style6)
btn_47 = Button(page4, text="Speed", command=lambda: page7.tkraise(), font=style7)
btn_41.pack()
btn_42.pack()
btn_43.pack()
btn_44.pack()
btn_45.pack()
btn_46.pack()
btn_47.pack()

#button temperature: 5

btn_51 = Button(page5, text="Home", command=lambda: main_page.tkraise(), font=stylemain)
btn_52 = Button(page5, text="Frequency", command=lambda: page1.tkraise(), font=style1)
btn_53 = Button(page5, text="CPU utilization", command=lambda: page2.tkraise(), font=style2)
btn_54 = Button(page5, text="Core utilization", command=lambda: page3.tkraise(), font=style3)
btn_55 = Button(page5, text="Load", command=lambda: page4.tkraise(), font=style4)
btn_56 = Button(page5, text="Power of consumption", command=lambda: page6.tkraise(), font=style6)
btn_57 = Button(page5, text="Speed", command=lambda: page7.tkraise(), font=style7)
btn_51.pack()
btn_52.pack()
btn_53.pack()
btn_54.pack()
btn_55.pack()
btn_56.pack()
btn_57.pack()

#button power of consumption: 6

btn_61 = Button(page6, text="Home", command=lambda: main_page.tkraise(), font=stylemain)
btn_62 = Button(page6, text="Frequency", command=lambda: page1.tkraise(), font=style1)
btn_63 = Button(page6, text="CPU utilization", command=lambda: page2.tkraise(), font=style2)
btn_64 = Button(page6, text="Core utilization", command=lambda: page3.tkraise(), font=style3)
btn_65 = Button(page6, text="Load", command=lambda: page4.tkraise(), font=style4)
btn_66 = Button(page6, text="Temperature", command=lambda: page5.tkraise(), font=style5)
btn_67 = Button(page6, text="Speed", command=lambda: page7.tkraise(), font=style7)
btn_61.pack()
btn_62.pack()
btn_63.pack()
btn_64.pack()
btn_65.pack()
btn_66.pack()
btn_67.pack()

#button speed: 7

btn_71 = Button(page7, text="Home", command=lambda: main_page.tkraise(), font=stylemain)
btn_72 = Button(page7, text="Frequency", command=lambda: page1.tkraise(), font=style1)
btn_73 = Button(page7, text="CPU utilization", command=lambda: page2.tkraise(), font=style2)
btn_74 = Button(page7, text="Core utilization", command=lambda: page3.tkraise(), font=style3)
btn_75 = Button(page7, text="Load", command=lambda: page4.tkraise(), font=style4)
btn_76 = Button(page7, text="Temperature", command=lambda: page5.tkraise(), font=style5)
btn_77 = Button(page7, text="Power of consumption", command=lambda: page6.tkraise(), font=style6)
btn_71.pack()
btn_72.pack()
btn_73.pack()
btn_74.pack()
btn_75.pack()
btn_76.pack()
btn_77.pack()


main_page.tkraise()
window.geometry("750x504")
window.title("PyCPU Monitor")
window.resizable(False,False)
window.mainloop()

