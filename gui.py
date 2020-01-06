# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.label import Label


def print_gui(get_message):
    if get_message is "":
        get_message = "not input message"

    ta = TestApp(get_message)

    ta.run()


class TestApp(App):
    def __init__(self, get_message):
        super(TestApp, self).__init__()
        self.message = get_message

    def build(self):
        self.title = 'py_voice'
        la = Label(text=self.message, font_name="C:\WINDOWS\FONTS\MEIRYO.TTC",
                   text_size=(700, 600), halign='left', valign='top')

        return la
