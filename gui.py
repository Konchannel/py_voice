# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.label import Label


def print_gui(get_message):
    ta = TestApp()

    if get_message is not "":
            ta.set_message(get_message)

    ta.run()


class TestApp(App):
    def __init__(self):
        self.message = "not input message"
        super(TestApp, self).__init__()

    def build(self):
        self.title = 'py_voice'
        return Label(text=self.message, font_name="C:\WINDOWS\FONTS\MEIRYO.TTC",
                     text_size=(700, 600), halign='left', valign='top')

    def set_message(self, message):
        self.message = message

