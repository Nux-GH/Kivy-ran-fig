# main.py
from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from kivy.graphics import *

from random import random, randint


DEFAULT_SIZE = 50


def get_int(val):
    return val * random()


class Scatterer(Scatter):
    def __init__(self, window):
        super().__init__()
        self.pos = get_int(window.width), get_int(window.height)
        self.size = DEFAULT_SIZE, DEFAULT_SIZE
        self.rotation = get_int(180)
        figure = randint(0, 2)

        with self.ids.cont.canvas:
            Color(random(),random(),random())
            if figure == 0:
                Rectangle(size=(DEFAULT_SIZE, DEFAULT_SIZE))
            elif figure == 1:
                Ellipse(size=(DEFAULT_SIZE, DEFAULT_SIZE), segments=get_int(180), angle_start=get_int(180),angle_end=get_int(360))
            elif figure == 2:
                Line(points=[get_int(DEFAULT_SIZE) for i in range(20)], width=1)


class MainWindowWidget(FloatLayout):
    is_runnning = True
    scatters = []

    def __init__(self, *args, **kwargs):
        super(MainWindowWidget, self).__init__( *args, **kwargs)
        Clock.schedule_interval(self.addfunction, .4)

    def addfunction(self, *args):
        if not self.is_runnning:
            return
        s = Scatterer(self.get_parent_window())
        self.add_widget(s)

    def add_widget(self, widget, index=0, canvas=None):
        if isinstance(widget, Scatterer):
            self.scatters.append(widget)
        super(MainWindowWidget, self).add_widget(widget, index=0, canvas=None)

    def switch(self):
        self.is_runnning = not self.is_runnning
        if self.is_runnning:
            text = "Stop"
        else:
            text = "Start"
        self.ids.switch.text = text

    def clear(self):
        for s in self.scatters:
            self.remove_widget(s)


class FiguresApp(App):
    def build(self):
        return MainWindowWidget()


if __name__ == '__main__':
    FiguresApp().run()
