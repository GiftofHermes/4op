import kivy
kivy.require("1.10.0") # replace with your current kivy version !

from kivy.app import App
from kivy.properties import NumericProperty
from kivy.graphics import Color
import GoalCreation
import GoalCheck

from kivy.core.window import Window
Window.size = (360, 400)

from kivy.uix.button import Button

def get_child(children, id):
    for child in children:
        if child.num == id:
            return child

class MyButtonStateLog:
    logs = []
    def add(self, children):
        states = []
        for child in children:
            state = MyButtonState(
                child.num,
                child.text,
                child.disabled
            )
            states.append(state)
        print("state logged")
        print(states)
        self.logs.append(states)

    def pop(self):
        return self.logs.pop()

class MyButtonState:
    num = 0
    text = ""
    disabled = None
    def __init__(self, num, text, disabled):
        self.num = num
        self.text = text
        self.disabled = disabled

class MyButton(Button):
    Select_num = None
    stateLog = None

    def on_num_pressed(self):
        # deselect number
        if MyButton.Select_num != None and MyButton.Select_num.num == self.num:
            MyButton.Select_num = None
            MyOp.Select_op.background_color = 1,1,1,1
            MyOp.Select_op = None
            self.background_color = 1,1,1,1
        else:
            # do the math
            if MyOp.Select_op != None:
                # save the num state
                if MyButton.stateLog == None:
                    MyButton.stateLog = MyButtonStateLog()
                MyButton.stateLog.add(self.parent.children)
                MyButton.Select_num.background_color = 1,1,1,1
                MyOp.Select_op.background_color = 1, 1, 1, 1
                MyButton.Select_num.disabled = True

                newValue = int(get_child(self.parent.children, MyButton.Select_num.num).text)
                if(MyOp.Select_op.op == 1):
                    self.text = str(int(self.text) + newValue)
                    MyButton.Select_num = None
                    MyOp.Select_op = None
                elif(MyOp.Select_op.op == 2):
                    #if does not substract properly abort or take abs
                    self.text = str(newValue - int(self.text))
                    MyButton.Select_num = None
                    MyOp.Select_op = None
                elif(MyOp.Select_op.op == 3):
                    self.text = str(int(self.text) * newValue)
                    MyButton.Select_num = None
                    MyOp.Select_op = None
                elif(MyOp.Select_op.op == 4):
                    if newValue % int(self.text) == 0:
                        #is divisible
                        self.text = str(newValue / int(self.text))
                        MyButton.Select_num = None
                        MyOp.Select_op = None
                    else:
                        #to-do: add screen shake to indicate not being divisible
                        #is not divisible
                        MyButton.Select_num.disabled = False
                        MyButton.Select_num = None
                        MyOp.Select_op = None
            # select
            else:
                MyButton.Select_num = self
                i = 1
                while i < 6 :
                    i+=1
                    #self.parent.ids["num%d" % i].background_color = 1, 1, 1, 1

                self.background_color = 1, 0, 0, 1

class MyOp(Button):
    Select_op = None
    def on_op_pressed(self):
        #Reverse last step from statelog
        if self.op == 5:
            children = self.parent.parent.parent.ids.numbers.children
            if MyButton.stateLog != None and MyButton.stateLog.logs != []:
                print(MyButton.stateLog)
                states = MyButton.stateLog.pop()
                for state in states:
                    child = get_child(children, state.num)
                    child.num = state.num
                    child.text = state.text
                    child.disabled = state.disabled
                    child.background_color = 1, 1, 1, 1
        elif MyButton.Select_num != None and MyOp.Select_op != self:
            #select op
            MyOp.Select_op = self
            self.background_color = 0,0,1,1
        elif MyOp.Select_op == self:
            #deselect op
            self.background_color = 1,1,1,1
            MyOp.Select_op = None


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