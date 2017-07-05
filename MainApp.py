import kivy
kivy.require("1.10.0") # replace with your current kivy version !

from kivy.app import App
from kivy.properties import NumericProperty, ObjectProperty
import GoalCreation
import GoalCheck
from kivy.core.window import Window
Window.size = (400, 400)

from kivy.uix.button import Button


class MyButton(Button):
    Select_num = 0
    def on_num_pressed(self):
        if MyButton.Select_num == self.num:
            MyButton.Select_num = 0
            MyOp.Select_op = 0
        else:
            if MyOp.Select_op != 0 or MyOp.Select_op != 5:
                MyButton.Select_num = self.num
            else:
                


class MyOp(Button):
    Select_op = 0
    def on_op_pressed(self):
        if MyButton.Select_num != 0:
            MyOp.Select_op = self.op
        print(MyOp.Select_op)


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