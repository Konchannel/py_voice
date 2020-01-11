# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.label import Label

from kivy.clock import Clock


def print_gui(get_message):
    if get_message is "":
        get_message = "not input message"

    ta = MyApp(get_message)
    # ta.input_loop("hoge")
    ta.update_label(ta.la, ta.message)

    ta.run()


class MyApp(App):
    def __init__(self, get_message):
        super(MyApp, self).__init__()
        self.message = get_message
        self.title = 'py_voice'
        self.la = Label(font_name="C:\WINDOWS\FONTS\MEIRYO.TTC")

    def build(self):
        return self.la

    def input_loop(self, hoge):
        Clock.schedule_once(lambda x: self.update_label(self.la, hoge), 5)

    def update_label(self, label_widget, txt):
        label_widget.text = txt
