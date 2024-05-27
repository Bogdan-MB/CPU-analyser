import tkinter as tk
from tkinter.ttk import Progressbar, Style
from PIL import Image, ImageTk

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

def update_progress_bar(progress, value=0):
    if progress.active: 
        if value > 100:
            return
        progress['value'] = value
        progress.after(500, update_progress_bar, progress, value + 20)

def start_progress_bar(frame):
    style = Style()
    style.theme_use('default')
    style.configure("blue.Horizontal.TProgressbar", troughcolor='#050A30', background='#20E5F6', thickness=30)

    progress = Progressbar(frame, orient=tk.HORIZONTAL, length=300, mode='determinate', style='blue.Horizontal.TProgressbar')
    progress.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    progress.active = True 

    update_progress_bar(progress)
    return progress 

def home_page():
    home_frame = tk.Frame(main_frame)
    set_background(home_frame, 'homedesign.png')
    lb = tk.Label(home_frame, text='PyCPU Monitor', font=title_font, fg='#20E5F6', bg='#050A30')
    lb.pack()
    home_frame.pack(fill='both', expand=True)
    return home_frame

def page1_page():
    page1_frame = tk.Frame(main_frame)
    set_background(page1_frame, 'pagedesign.png')
    lb = tk.Label(page1_frame, text='Frequency', font=title_font, fg='#20E5F6', bg='#050A30')
    lb.pack()
    page1_frame.pack(fill='both', expand=True)
    progress = start_progress_bar(page1_frame)  
    page1_frame.progress = progress 
    frames.append(page1_frame)  
    return page1_frame  

def page2_page():
    page2_frame = tk.Frame(main_frame)
    set_background(page2_frame, 'pagedesign.png')
    lb = tk.Label(page2_frame, text='CPU utilization', font=title_font, fg='#20E5F6', bg='#050A30')
    lb.pack()
    page2_frame.pack(fill='both', expand=True)
    progress = start_progress_bar(page2_frame) 
    page2_frame.progress = progress  
    frames.append(page2_frame)  
    return page2_frame 

def page3_page():
    page3_frame = tk.Frame(main_frame)
    set_background(page3_frame, 'pagedesign.png')
    lb = tk.Label(page3_frame, text='Core utilization', font=title_font, fg='#20E5F6', bg='#050A30')
    lb.pack()
    page3_frame.pack(fill='both', expand=True)
    progress = start_progress_bar(page3_frame) 
    page3_frame.progress = progress  
    frames.append(page3_frame) 
    return page3_frame 

def page4_page():
    page4_frame = tk.Frame(main_frame)
    set_background(page4_frame, 'pagedesign.png')
    lb = tk.Label(page4_frame, text='Load', font=title_font, fg='#20E5F6', bg='#050A30')
    lb.pack()
    page4_frame.pack(fill='both', expand=True)
    progress = start_progress_bar(page4_frame) 
    page4_frame.progress = progress 
    frames.append(page4_frame)  
    return page4_frame  

def page5_page():
    page5_frame = tk.Frame(main_frame)
    set_background(page5_frame, 'pagedesign.png')
    lb = tk.Label(page5_frame, text='Temperature', font=title_font, fg='#20E5F6', bg='#050A30')
    lb.pack()
    page5_frame.pack(fill='both', expand=True)
    progress = start_progress_bar(page5_frame) 
    page5_frame.progress = progress  
    frames.append(page5_frame)  
    return page5_frame

def page6_page():
    page6_frame = tk.Frame(main_frame)
    set_background(page6_frame, 'pagedesign.png')
    lb = tk.Label(page6_frame, text='Power of consumption', font=title_font, fg='#20E5F6', bg='#050A30')
    lb.pack()
    page6_frame.pack(fill='both', expand=True)
    progress = start_progress_bar(page6_frame) 
    page6_frame.progress = progress 
    frames.append(page6_frame)  
    return page6_frame 

def page7_page():
    page7_frame = tk.Frame(main_frame)
    set_background(page7_frame, 'pagedesign.png')
    lb = tk.Label(page7_frame, text='Speed', font=title_font, fg='#20E5F6', bg='#050A30')
    lb.pack()
    page7_frame.pack(fill='both', expand=True)
    progress = start_progress_bar(page7_frame)  
    page7_frame.progress = progress 
    frames.append(page7_frame) 
    return page7_frame 

def delete_page(frame):
    frame.active = False 
    frame.destroy()

def indicate(lb, page):
    hide_indicators()
    lb.config(bg='#158aff')
    delete_pages()
    frame = page()
    frames.append(frame)

def delete_pages():
    for frame in frames:
        delete_page(frame)
    frames.clear()

def hide_indicators():
    home_indicate.config(bg='#c3c3c3')
    page1_indicate.config(bg='#c3c3c3')
    page2_indicate.config(bg='#c3c3c3')
    page3_indicate.config(bg='#c3c3c3')
    page4_indicate.config(bg='#c3c3c3')
    page5_indicate.config(bg='#c3c3c3')
    page6_indicate.config(bg='#c3c3c3')
    page7_indicate.config(bg='#c3c3c3')

options_frame = tk.Frame(root, bg='#050929')

home_btn = tk.Button(options_frame, text='Home', font=('Bolt', 12), fg='#335f73', bd=0, bg='#c3c3c3', command=lambda: indicate(home_indicate, home_page))
home_btn.place(x=10, y=0)

home_indicate = tk.Label(options_frame, text='', bg='#335f73')
home_indicate.place(x=3, y=1, width=5, height=40)

page1_btn = tk.Button(options_frame, text='Frequency', font=('Bolt', 12), fg='#335f73', bd=0, bg='#c3c3c3', command=lambda: indicate(page1_indicate, page1_page))
page1_btn.place(x=10, y=50)

page1_indicate = tk.Label(options_frame, text='', bg='#335f73')
page1_indicate.place(x=3, y=50, width=5, height=40)

page2_btn = tk.Button(options_frame, text='CPU utilization', font=('Bolt', 12), fg='#335f73', bd=0, bg='#c3c3c3', command=lambda: indicate(page2_indicate, page2_page))
page2_btn.place(x=10, y=100)

page2_indicate = tk.Label(options_frame, text='', bg='#335f73')
page2_indicate.place(x=3, y=100, width=5, height=40)

page3_btn = tk.Button(options_frame, text='Core utilization', font=('Bolt', 12), fg='#335f73', bd=0, bg='#c3c3c3', command=lambda: indicate(page3_indicate, page3_page))
page3_btn.place(x=10, y=150)

page3_indicate = tk.Label(options_frame, text='', bg='#335f73')
page3_indicate.place(x=3, y=150, width=5, height=40)

page4_btn = tk.Button(options_frame, text='Load', font=('Bolt', 12), fg='#335f73', bd=0, bg='#c3c3c3', command=lambda: indicate(page4_indicate, page4_page))
page4_btn.place(x=10, y=200)

page4_indicate = tk.Label(options_frame, text='', bg='#335f73')
page4_indicate.place(x=3, y=200, width=5, height=40)

page5_btn = tk.Button(options_frame, text='Temperature', font=('Bolt', 12), fg='#335f73', bd=0, bg='#c3c3c3', command=lambda: indicate(page5_indicate, page5_page))
page5_btn.place(x=10, y=250)

page5_indicate = tk.Label(options_frame, text='', bg='#335f73')
page5_indicate.place(x=3, y=250, width=5, height=40)

page6_btn = tk.Button(options_frame, text='Power of consumption', font=('Bolt', 12), fg='#335f73', bd=0, bg='#c3c3c3', command=lambda: indicate(page6_indicate, page6_page))
page6_btn.place(x=10, y=300)

page6_indicate = tk.Label(options_frame, text='', bg='#335f73')
page6_indicate.place(x=3, y=300, width=5, height=40)

page7_btn = tk.Button(options_frame, text='Speed', font=('Bolt', 12), fg='#335f73', bd=0, bg='#c3c3c3', command=lambda: indicate(page7_indicate, page7_page))
page7_btn.place(x=10, y=350)

page7_indicate = tk.Label(options_frame, text='', bg='#335f73')
page7_indicate.place(x=3, y=350, width=5, height=40)

options_frame.pack(side='left')
options_frame.pack_propagate(False)
options_frame.configure(width=200, height=400)

main_frame = tk.Frame(root, highlightbackground='black', highlightthickness=2)
set_background(main_frame, 'homedesign.png')
main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=400, width=700)

frames = []

root.mainloop()
