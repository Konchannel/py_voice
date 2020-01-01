# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.label import Label


def print_gui(get_message):
    ta = TestApp()
    ta.set_message(get_message)
    ta.run()


class TestApp(App):
    message = "not message"

    def build(self):
        self.title = 'py_voice'
        return Label(text=self.message, font_name="C:\WINDOWS\FONTS\MEIRYO.TTC")

    def set_message(self, message):
        self.message = message

