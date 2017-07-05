import kivy
kivy.require("1.10.0")

from kivy.app import App
from kivy.properties import NumericProperty

class MainApp(App):
    goal = NumericProperty(635)

MainApp().run()