# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.label import Label


class TestApp(App):
    message = "NOT MESSAGE"

    def build(self):
        self.title = 'py_voice'
        return Label(text=TestApp.message, font_name="C:\WINDOWS\FONTS\MEIRYO.TTC")

    def get_message(self, mes):
        TestApp.message = mes


if __name__ == '__main__':
    TestApp().run()
