import kivy
kivy.require("1.10.0") # replace with your current kivy version !

from kivy.app import App
from kivy.properties import NumericProperty
import GoalCreation
from kivy.core.window import Window
Window.size = (400, 400)

class MainApp(App):
    numbers = GoalCreation.goal_creation(1,5)
    goal = NumericProperty(numbers[0])
    num1 = NumericProperty(numbers[1])
    num2 = NumericProperty(numbers[2])
    num3 = NumericProperty(numbers[3])
    num4 = NumericProperty(numbers[4])
    num5 = NumericProperty(numbers[5])
    num6 = NumericProperty(numbers[6])

if __name__ == '__main__':
    MainApp().run()