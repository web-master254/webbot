import requests 
import os
import time
from bs4 import BeautifulSoup
from random import random
import math
from time import sleep

class Web_bot:
    def __init__(self):
        self.links = []
        self.visited_link = ()
        self.folder = "Text_files"
        self.folder_list = os.listdir('.')
        if self.folder not in self.folder_list:
            os.mkdir(self.folder)
        else:
            pass

    def get_links(self,url):
        for i in BeautifulSoup(requests.get(url).text,'html.parser').find_all('a'):
            if i.get('href').startswith('http'):
                sleep(1)
                self.links.append(i.get('href'))
                sleep(2)

        return self.links
    def visit_links(self,lk,url):
        lk(url)
        for l in self.links:
            for w in BeautifulSoup(requests.get(l).text,'html.parser').find_all('div'):
                sleep(3)
                if len(w.get_text()) > 99:
                    with open(os.path.join(self.folder,f"file{math.floor(random()**2*56)}.txt"),'w+') as f:
                        f.write(w.get_text())
                        sleep(2)
                else:
                    pass
                              



y = Web_bot()
y.visit_links(y.get_links,"https://www.pythonanywhere.com/forums/topic/26990/")
