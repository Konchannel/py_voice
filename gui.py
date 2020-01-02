# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.label import Label


def print_gui(get_message):
    ta = TestApp()
    ta.set_message(get_message)
    ta.run()


class TestApp(App):
    message = "no message"

    def build(self):
        TestApp.title = 'py_voice'
        return Label(text=TestApp.message, font_name="C:\WINDOWS\FONTS\MEIRYO.TTC")

    @staticmethod
    def set_message(message):
        TestApp.message = message

