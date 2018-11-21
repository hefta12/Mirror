# -*- coding: utf-8 -
import datetime
from Tkinter import *
import feedparser
import traceback
from mail import Mail

now = datetime.datetime.now()
midnight = datetime.datetime.combine(now.date(), datetime.time())
minutes = (now - midnight).seconds / 60

xlarge_text_size = 40
large_text_size = 38
medium_text_size = 18
small_text_size = 12


class Goodmorning(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.titles1 = ''
        self.GoodmorningLbl = Label(self, text=self.titles1, font=('Helvetica', xlarge_text_size, 'roman', 'italic'),
                                    fg="white", bg="black", anchor=W)
        self.GoodmorningLbl.pack()
        self.mails = Label(self, font=('Helvetica', xlarge_text_size, 'roman', 'italic'), fg="white",
                           background="black")
        self.mails.pack(side=TOP)
        self.get_title_gm()

    # intervals when do you want to display which text
    def get_title_gm(self):
        now = datetime.datetime.now()
        midnight = datetime.datetime.combine(now.date(), datetime.time())
        minutes = (now - midnight).seconds / 60
        if 0 <= minutes <= 300:
            titles2 = 'Your text'
        elif 300 < minutes <= 720:
            titles2 = 'Your text'
        elif 720 < minutes <= 900:
            titles2 = 'Your text'
        elif 900 < minutes <= 1140:
            titles2 = 'Your text'
        elif 1140 < minutes <= 1320:
            titles2 = 'Your text'
        elif 1321 < minutes <= 1440:
            titles2 = 'Your text'
        else:
            titles2 = 'Your text'

        if titles2 != self.titles1:
            self.titles1 = titles2
            self.GoodmorningLbl.config(text=titles2)

        self.mails.config(text=Mail.email)

        self.GoodmorningLbl.after(500, self.get_title_gm)
