import tkinter as tk
from tkinter import *
from tkinter import font

window = tk.Tk()

stylemain = font.Font(size=10)
style1 = font.Font(size=10)
style2 = font.Font(size=10)
style3 = font.Font(size=10)
style4 = font.Font(size=10)
style5 = font.Font(size=10)
style6 = font.Font(size=10)
style7 = font.Font(size=10)

main_page = Frame(window)
page1 = Frame(window)
page2 = Frame(window)
page3 = Frame(window)
page4 = Frame(window)
page5 = Frame(window)
page6 = Frame(window)
page7 = Frame(window)

for page in (main_page, page1, page2, page3, page4, page5, page6, page7):
    page.grid(row=0, column=0, sticky="nsew")

labels = {
    main_page: ("Main este a", stylemain),
    page1: ("page1 este a", style1),
    page2: ("page2 este a", style2),
    page3: ("page3 este a", style3),
    page4: ("page4 este a", style4),
    page5: ("page5 este a", style5),
    page6: ("page6 este a", style6),
    page7: ("page7 este a", style7),
}

for page, (text, style) in labels.items():
    label = Label(page, text=text, font=style)
    label.pack(pady=30)

def create_buttons(frame, buttons):
    for text, command, style in buttons:
        button = Button(frame, text=text, command=command, font=style)
        button.pack(pady=5)

main_buttons = [
    ("Frequency", lambda: page1.tkraise(), style1),
    ("CPU utilization", lambda: page2.tkraise(), style2),
    ("Core utilization", lambda: page3.tkraise(), style3),
    ("Load", lambda: page4.tkraise(), style4),
    ("Temperature", lambda: page5.tkraise(), style5),
    ("Power of consumption", lambda: page6.tkraise(), style6),
    ("Speed", lambda: page7.tkraise(), style7),
]

page_buttons = {
    page1: [
        ("Home", lambda: main_page.tkraise(), stylemain),
        ("CPU utilization", lambda: page2.tkraise(), style2),
        ("Core utilization", lambda: page3.tkraise(), style3),
        ("Load", lambda: page4.tkraise(), style4),
        ("Temperature", lambda: page5.tkraise(), style5),
        ("Power of consumption", lambda: page6.tkraise(), style6),
        ("Speed", lambda: page7.tkraise(), style7),
    ],
    page2: [
        ("Home", lambda: main_page.tkraise(), stylemain),
        ("Frequency", lambda: page1.tkraise(), style1),
        ("Core utilization", lambda: page3.tkraise(), style3),
        ("Load", lambda: page4.tkraise(), style4),
        ("Temperature", lambda: page5.tkraise(), style5),
        ("Power of consumption", lambda: page6.tkraise(), style6),
        ("Speed", lambda: page7.tkraise(), style7),
    ],
    page3: [
        ("Home", lambda: main_page.tkraise(), stylemain),
        ("Frequency", lambda: page1.tkraise(), style1),
        ("CPU utilization", lambda: page2.tkraise(), style2),
        ("Load", lambda: page4.tkraise(), style4),
        ("Temperature", lambda: page5.tkraise(), style5),
        ("Power of consumption", lambda: page6.tkraise(), style6),
        ("Speed", lambda: page7.tkraise(), style7),
    ],
    page4: [
        ("Home", lambda: main_page.tkraise(), stylemain),
        ("Frequency", lambda: page1.tkraise(), style1),
        ("CPU utilization", lambda: page2.tkraise(), style2),
        ("Core utilization", lambda: page3.tkraise(), style3),
        ("Temperature", lambda: page5.tkraise(), style5),
        ("Power of consumption", lambda: page6.tkraise(), style6),
        ("Speed", lambda: page7.tkraise(), style7),
    ],
    page5: [
        ("Home", lambda: main_page.tkraise(), stylemain),
        ("Frequency", lambda: page1.tkraise(), style1),
        ("CPU utilization", lambda: page2.tkraise(), style2),
        ("Core utilization", lambda: page3.tkraise(), style3),
        ("Load", lambda: page4.tkraise(), style4),
        ("Power of consumption", lambda: page6.tkraise(), style6),
        ("Speed", lambda: page7.tkraise(), style7),
    ],
    page6: [
        ("Home", lambda: main_page.tkraise(), stylemain),
        ("Frequency", lambda: page1.tkraise(), style1),
        ("CPU utilization", lambda: page2.tkraise(), style2),
        ("Core utilization", lambda: page3.tkraise(), style3),
        ("Load", lambda: page4.tkraise(), style4),
        ("Temperature", lambda: page5.tkraise(), style5),
        ("Speed", lambda: page7.tkraise(), style7),
    ],
    page7: [
        ("Home", lambda: main_page.tkraise(), stylemain),
        ("Frequency", lambda: page1.tkraise(), style1),
        ("CPU utilization", lambda: page2.tkraise(), style2),
        ("Core utilization", lambda: page3.tkraise(), style3),
        ("Load", lambda: page4.tkraise(), style4),
        ("Temperature", lambda: page5.tkraise(), style5),
        ("Power of consumption", lambda: page6.tkraise(), style6),
    ],
}

create_buttons(main_page, main_buttons)

for page, buttons in page_buttons.items():
    create_buttons(page, buttons)

main_page.tkraise()
window.geometry("730x500")
window.title("PyCPU Monitor")
window.resizable(False, False)
window.mainloop()
