# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.label import Label


class TestApp(App):
    def build(self):
        self.title = 'py_voice'
        return Label(text="GUI Example: Sample :)")  # ,Button(text="OK")


if __name__ == '__main__':
    TestApp().run()
