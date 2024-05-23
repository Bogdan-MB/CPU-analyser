import tkinter as tk


root = tk.Tk()
root.geometry('700x400')
root.title('PyCPU Monitor')
root.resizable(False, False)

def home_page():
    home_frame= tk.Frame(main_frame)
    lb = tk.Label(home_frame, text='Home page\n\nPage: 1', font=('Bold', 30))
    lb.pack()
    home_frame.pack(pady=20)

def page1_page():
    page1_frame= tk.Frame(main_frame)
    lb = tk.Label(page1_frame, text='Page1 page\n\nPage: 1', font=('Bold', 30))
    lb.pack()
    page1_frame.pack(pady=20)

def page2_page():
    page2_frame= tk.Frame(main_frame)
    lb = tk.Label(page2_frame, text='Page2 page\n\nPage: 1', font=('Bold', 30))
    lb.pack()
    page2_frame.pack(pady=20)

def page3_page():
    page3_frame= tk.Frame(main_frame)
    lb = tk.Label(page3_frame, text='Page3 page\n\nPage: 1', font=('Bold', 30))
    lb.pack()
    page3_frame.pack(pady=20)

def page4_page():
    page4_frame= tk.Frame(main_frame)
    lb = tk.Label(page4_frame, text='Page4 page\n\nPage: 1', font=('Bold', 30))
    lb.pack()
    page4_frame.pack(pady=20)

def page5_page():
    page5_frame= tk.Frame(main_frame)
    lb = tk.Label(page5_frame, text='Page5 page\n\nPage: 1', font=('Bold', 30))
    lb.pack()
    page5_frame.pack(pady=20)

def page6_page():
    page6_frame= tk.Frame(main_frame)
    lb = tk.Label(page6_frame, text='Page6 page\n\nPage: 1', font=('Bold', 30))
    lb.pack()
    page6_frame.pack(pady=20)

def page7_page():
    page7_frame= tk.Frame(main_frame)
    lb = tk.Label(page7_frame, text='Page7 page\n\nPage: 1', font=('Bold', 30))
    lb.pack()
    page7_frame.pack(pady=20)

def hide_indicators():
    home_indicate.config(bg='#c3c3c3')
    page1_indicate.config(bg='#c3c3c3')
    page2_indicate.config(bg='#c3c3c3')
    page3_indicate.config(bg='#c3c3c3')
    page4_indicate.config(bg='#c3c3c3')
    page5_indicate.config(bg='#c3c3c3')
    page6_indicate.config(bg='#c3c3c3')
    page7_indicate.config(bg='#c3c3c3')

def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()

def indicate(lb, page):
    hide_indicators()
    lb.config(bg='#158aff')
    delete_pages()
    page()



options_frame = tk.Frame(root, bg='#c3c3c3')

home_btn=tk.Button(options_frame, text='Home', font=('Bolt',12), fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: indicate(home_indicate, home_page))
home_btn.place(x=10, y=0)

home_indicate=tk.Label(options_frame, text='', bg='#c3c3c3')
home_indicate.place(x=3, y=1, width=5, height=40)

page1_btn=tk.Button(options_frame, text='Frequency', font=('Bolt',12), fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: indicate(page1_indicate, page1_page))
page1_btn.place(x=10, y=50)

page1_indicate=tk.Label(options_frame, text='', bg='#c3c3c3')
page1_indicate.place(x=3, y=50, width=5, height=40)

page2_btn=tk.Button(options_frame, text='CPU utilization', font=('Bolt',12), fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: indicate(page2_indicate, page2_page))
page2_btn.place(x=10, y=100)

page2_indicate=tk.Label(options_frame, text='', bg='#c3c3c3')
page2_indicate.place(x=3, y=100, width=5, height=40)

page3_btn=tk.Button(options_frame, text='Core utilization', font=('Bolt',12), fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: indicate(page3_indicate, page3_page))
page3_btn.place(x=10, y=150)

page3_indicate=tk.Label(options_frame, text='', bg='#c3c3c3')
page3_indicate.place(x=3, y=150, width=5, height=40)

page4_btn=tk.Button(options_frame, text='Load', font=('Bolt',12), fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: indicate(page4_indicate, page4_page))
page4_btn.place(x=10, y=200)

page4_indicate=tk.Label(options_frame, text='', bg='#c3c3c3')
page4_indicate.place(x=3, y=200, width=5, height=40)

page5_btn=tk.Button(options_frame, text='Temperature', font=('Bolt',12), fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: indicate(page5_indicate, page5_page))
page5_btn.place(x=10, y=250)

page5_indicate=tk.Label(options_frame, text='', bg='#c3c3c3')
page5_indicate.place(x=3, y=250, width=5, height=40)

page6_btn=tk.Button(options_frame, text='Power of consumption', font=('Bolt',12), fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: indicate(page6_indicate, page6_page))
page6_btn.place(x=10, y=300)

page6_indicate=tk.Label(options_frame, text='', bg='#c3c3c3')
page6_indicate.place(x=3, y=300, width=5, height=40)

page7_btn=tk.Button(options_frame, text='Speed', font=('Bolt',12), fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: indicate(page7_indicate, page7_page))
page7_btn.place(x=10, y=350)

page7_indicate=tk.Label(options_frame, text='', bg='#c3c3c3')
page7_indicate.place(x=3, y=350, width=5, height=40)


options_frame.pack(side='left')
options_frame.pack_propagate(False)
options_frame.configure(width=200, height=400)

main_frame = tk.Frame(root, highlightbackground='black', highlightthickness=2)
main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=400, width=700)

root.mainloop()