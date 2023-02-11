import os
import tkinter as tk
import webbrowser
from tkinter import messagebox as mes
import sys

class login:
    def __init__(self,main,menu):
        self.main = main
        self.menu = menu
        self.login_page = tk.Toplevel(main)
        self.login_page.title('login')
        self.login_page.geometry('300x400')
        self.login_page_thing = tk.Frame(self.login_page)
        self.user_name = tk.StringVar()
        self.user_code = tk.StringVar()
        self.setting()

    def setting(self):
        tk.Label(self.login_page_thing,text='登陆').grid(row=1,column=3)
        tk.Label(self.login_page_thing,text = '管理员账号:').grid(row=2,column=1)
        tk.Label(self.login_page_thing,text='密码:').grid(row=3,column=1)
        tk.Entry(self.login_page_thing,textvariable=self.user_name).grid(row=2,column=2)
        tk.Entry(self.login_page_thing,textvariable=self.user_code).grid(row=3,column=2)
        tk.Button(self.login_page_thing,text='done',command=self.admin_in).grid(row=4,column=3)
        self.login_page_thing.pack()

    def wonder(self):
        if self.user_name.get() == 'admin' and self.user_code.get() == '114514':
            mes.showinfo(title='welcome',message='welcome admin')
            self.login_page.destroy()
            return True
        else:
            mes.showerror(title='error',message='please check your enter')
            self.login_page.destroy()
            return False

    def admin_in(self):
        if self.wonder() is True:
            admin_menu(self.main,self.menu)


class admin_menu:
        def __init__(self,main:tk.Tk,menu:tk.Menu):
            self.url = 'https://github.com/GalaxyloveTan/translations_alpha-0.1-2-'
            self.main = main
            self.menu = menu
            self.admin_menu = tk.Menu(self.menu)
            self.setting()

        def setting(self):
            self.menu.add_cascade(label='管理员菜单',menu=self.admin_menu)
            self.admin_menu.add_command(label='delete data(慎用)',command=lambda :os.remove('user/data'))
            self.admin_menu.add_command(label='cmd指令',command=lambda :cmd_command(self.main))
            self.admin_menu.add_command(label='打开git仓库',command=lambda :webbrowser.open(self.url))
            self.admin_menu.add_command(label='添加子窗口',command=lambda :tk.Toplevel(self.main))

class cmd_command:
        def __init__(self,main:tk.Tk):
            self.main = main
            self.cmd_page = tk.Toplevel(main)
            self.cmd_page.title('cmd')
            self.cmd_page.geometry('400x300')
            self.get = tk.StringVar()
            self.enter = tk.Frame(self.cmd_page)
            self.setting()

        def setting(self):
            tk.Entry(self.enter,textvariable=self.get).grid(row=1,column=2)
            tk.Button(self.enter,text='execute',command=lambda :os.system(self.get.get())).grid(row=2,column=2)
            self.enter.pack()


