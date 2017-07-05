import kivy
kivy.require("1.10.0") # replace with your current kivy version !

from kivy.app import App
from kivy.properties import NumericProperty, ObjectProperty
import GoalCreation
from kivy.core.window import Window
Window.size = (400, 400)

from kivy.uix.button import Button

Select_num = 0
class MyButton(Button):
    def on_num_pressed(self):
        Select_num = self.num
        print(Select_num)

Select_op = 0
class MyOp(Button):
    def on_op_pressed(self):
        if Select_num != 0:
            Select_op = self.op
        print(Select_op)


class MainApp(App):
    numbers = GoalCreation.goal_creation(1,5)
    goal = NumericProperty(numbers[0])
    num1 = NumericProperty(numbers[1])
    num2 = NumericProperty(numbers[2])
    num3 = NumericProperty(numbers[3])
    num4 = NumericProperty(numbers[4])
    num5 = NumericProperty(numbers[5])
    num6 = NumericProperty(numbers[6])

    selected_num = 0

    def on_num_pressed(self, id):
        print("number %d pressed" % id)

    def on_op_pressed(self, id):
        print("op %s pressed" % id)

if __name__ == '__main__':
    MainApp().run()