# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.label import Label


class TestApp(App):
    def build(self, response_str):
        self.title = 'py_voice'
        return Label(text=response_str)


if __name__ == '__main__':
    TestApp().run()
