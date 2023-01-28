import requests
import tkinter as tk
import re


class translator:
    def __init__(self, data: tk.StringVar, outer: tk.StringVar):
        self.url = 'https://fanyi.baidu.com/sug'
        try:
            self.data = {
                'kw': data.get()
            }
        except:
            self.data = {
                'kw': data
            }
        self.out = outer
        self.get_information()
        # 下半部分为你需要修改的地方

    def get_information(self):
        resp = requests.post(url=self.url, data=self.data).json()  # 这是爬下来的数据
        try:
            last = dict(resp['data'][0])
        except:
            last = dict(resp['data'])
        l_last = last['v']
        self.out.set(l_last)  # 将处理好的内容映射出来
