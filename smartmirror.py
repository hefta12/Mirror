# -*- coding: utf-8 -*-
from Tkinter import *
from goodmorning import Goodmorning
from news import News
from weather import Weather
from clock import Clock


class FullscreenWindow:
    def __init__(self):
        self.tk = Tk()
        self.tk.attributes("-fullscreen", True)
        self.tk.configure(background='black')
        self.topFrame = Frame(self.tk, background='black')
        self.bottomFrame = Frame(self.tk, background='black')
        self.topFrame.pack(side=TOP, fill=BOTH, expand=YES)
        self.bottomFrame.pack(side=BOTTOM, fill=BOTH, expand=YES)
        self.state = False
        self.tk.bind("<Return>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)
        # clock
        self.clock = Clock(self.topFrame)
        self.clock.pack(side=RIGHT, anchor=N, padx=100, pady=60)
        # weather
        self.weather = Weather(self.topFrame)
        self.weather.pack(side=LEFT, anchor=N, pady=60, padx=100)
        # news
        self.news = News(self.bottomFrame)
        self.news.pack(side=LEFT, anchor=S, padx=100, pady=60)
        # goodmorning
        self.Goodmoring = Goodmorning(self.topFrame, background='black')
        self.Goodmoring.pack(side=BOTTOM, anchor=W)

    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", self.state)
        return "break"


if __name__ == '__main__':
    w = FullscreenWindow()
    w.tk.mainloop()
