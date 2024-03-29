import tkinter as tk
# from translators import translator as tr


class history_page:
    def __init__(self, main: tk.Tk, main_page: tk.Frame):
        self.main = main
        self.main_page = main_page
        self.history_page = tk.Frame(main)
        self.show_information = tk.StringVar()
        self.listbox = tk.Listbox(self.history_page)
        self.back_on = tk.StringVar()
        self.get = tk.IntVar()
        try:
            self.information = open(file='./user/user', mode='r')
        except:
            tk.Label(self.history_page, textvariable=self.show_information).grid(row=1,column=1)
        self.history_page.pack()
        self.setting()
        while True:
            self.getting()
            self.history_page.update()

    def setting(self):
        self.main_page.forget()
        tk.Label(self.history_page, text='History',font=('微软雅黑',15)).grid(row=1, column=1)
        tk.Button(self.history_page, text='back', command=self.back).grid(row=1, column=4)
        for i in self.information:
            self.listbox.insert('end', i)
        self.listbox.grid(row=2, column=2)
        tk.Label(self.history_page, textvariable=self.back_on).grid(row=2, column=1)

    def back(self):
        self.history_page.forget()
        self.main_page.pack()

    def getting(self):
        consequnce = self.listbox.get()[0]
        # tr(consequnce, outer=self.back_on)
