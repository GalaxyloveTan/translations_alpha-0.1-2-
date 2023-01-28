import datetime
import tkinter as tk
from function.translators import translator
from tkinter import messagebox as mes
from function.history import history_page
import datetime as dt

class main_thing:
    def __init__(self, main: tk.Tk):
        self.main = main
        self.url = 'https://fanyi.baidu.com/sug'
        self.inn = tk.StringVar()
        self.out = tk.StringVar()
        main.title('translator made by Galaxy')
        main.geometry('600x500+474+150')
        self.main_page = tk.Frame(main)
        self.menu_bar = tk.Menu(self.main)
        self.son_menu = tk.Menu(self.menu_bar)
        self.main.iconbitmap('icon/favicon.ico')

        self.main_page.pack()
        self.setting()
        self.menu_bar_setting()
        self.about = '本软件由银河系与一仔联合制作,严禁用于商业\n违者必将以法律责任追究'
        self.main['menu'] = self.menu_bar
        main.mainloop()

    def setting(self):
        tk.Entry(self.main_page, textvariable=self.inn).grid(row=2, column=2)
        tk.Label(self.main_page, text='Translator',font=('微软雅黑',13),foreground='blue').grid(row=1, column=2)
        tk.Label(self.main_page, textvariable=self.out, state='normal',font=(None,10)).grid(row=5, column=2)
        tk.Button(self.main_page, text='translate', command=self.translate).grid(row=3, column=2)

    def translate(self):
        try:
            translator(data=self.inn, outer=self.out)
        except:
            self.out.set('please check the text')
        try:
            with open(file=r'user/data', mode='a') as f:
                if str(self.inn.get()) != '':
                    f.write(str(self.inn.get()) + '\n')
        except:
            with open(file=r'user/data', mode='w') as f:
                if str(self.inn.get()) != '':
                    f.write(str(self.inn.get()) + '\n')

    def menu_bar_setting(self):

        self.menu_bar.add_cascade(menu=self.son_menu,label='about')
        self.son_menu.add_command(label='author',command=lambda : mes.showinfo(title='author',message='Galaxy\n特别感谢:一仔'))
        self.menu_bar.add_command(label='语言',command=lambda : mes.showinfo(title='luaghge',message='开发中,敬请期待'))
        self.son_menu.add_command(label='注意事项',

                                  command=lambda: mes.showinfo(title='注意事项', message='{}'.format(self.about)))
        self.menu_bar.add_command(label='history',command=self.history_pages)

    def history_pages(self):
        history_page(main=self.main,main_page=self.main_page,menu=self.menu_bar)

root = main_thing

if __name__ == '__main__':
    try:
        with open('user/log', mode='a') as f:
            f.write(str(dt.datetime.now())+'\n')
    except:
        with open('user/log', mode='w') as f:
            f.write(str(dt.datetime.now())+'\n')
    finally:
        root(tk.Tk())
    with open('user/log', mode='a') as f:
        f.write(str(dt.datetime.now())+'\n')
































