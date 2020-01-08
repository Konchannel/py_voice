# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.label import Label

from kivy.clock import Clock


def print_gui(get_message):
    if get_message is "":
        get_message = "not input message"

    ta = TestApp(get_message)
    ta.input_loop("hoge")

    ta.run()


class TestApp(App):
    def __init__(self, get_message):
        super(TestApp, self).__init__()
        self.message = get_message
        self.title = 'py_voice'
        self.la = Label(text="not input message", font_name="C:\WINDOWS\FONTS\MEIRYO.TTC",
                        text_size=(700, 600), halign='left', valign='top')

    def build(self):
        return self.la

    def input_loop(self, hoge):
        Clock.schedule_once(lambda x: self.update_label(self.la, hoge), 5)

    def update_label(self, label_widget, txt):
        label_widget.text = txt
