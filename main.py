from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout

Builder.load_file('design.kv')

class Calculator(FloatLayout):
    calculator = ObjectProperty(None)
    display = ObjectProperty(None)
    nums = ObjectProperty(None)
    ops = ObjectProperty(None)
    # Your Calculator class implementation goes here
    pass

class EZCalculatorApp(App):
    def build(self):       
        return Calculator()
   
if __name__ == "__main__":
    EZCalculatorApp().run()



# class Display(TextInput):
#     def __init__(self, **kwargs):
#         super(Display, self).__init__(**kwargs)
#         # self.size_hint = (.5, .25)
#         # self.multiline=False
#         # self.font_size=70
#         # self.pos_hint_x=.5

# class Buttons(GridLayout):
#     def __init__(self, **kwargs):
#         super(Buttons, self).__init__(**kwargs)
#         # self.cols = 2
#         # self.spacing = 50
#         # self.add_widget(NumButtons())
#         # self.add_widget(OpsButtons())

# class OpsButtons(GridLayout):
#     def __init__(self, **kwargs):
#         super(OpsButtons, self).__init__(**kwargs)
#         # self.cols = 1
#         # self.size_hint_x=None
#         # self.width=200
       
#         ops = ['/', '*', '-', '+']

#         for sign in ops:
#             button = Button(text=str(sign), font_size=50, size_hint=(.3,.3))
#             self.add_widget(button)


# class NumButtons(GridLayout):
#     def __init__(self, **kwargs):
#         super(NumButtons, self).__init__(**kwargs)
#         # self.cols = 3  # Set the number of columns in the grid

#         for digit in range(1, 10):  # Start from 1 to 9
#             button = Button(text=str(digit), font_size=32)
#             button.bind(on_press=self.on_button_press)  # Bind a function to button press
#             self.add_widget(button)

#         # Add '0' button separately
#         zero_button = Button(text='0', font_size=32)
#         zero_button.bind(on_press=self.on_button_press)
#         self.add_widget(zero_button)

#         dec_button = Button(text='.', font_size=32, pos=self.center)
#         dec_button.bind(on_press=self.on_button_press)
#         self.add_widget(dec_button)

#         equal_button = Button(text='=', font_size=50, color=[0, 1, 1, .5])
#         self.add_widget(equal_button)


#     def on_button_press(self, instance):
#         # Example function to handle button press
#         print(f'Button {instance.text} pressed')


# class Calculator(Widget):
#     # def __init__(self, **kwargs):
#     #     super(Calculator,self).__init__(**kwargs)
#     #     self.rows=2
#     #     self.spacing=10
#     #     self.padding=[100, 50, 100, 20]
#         # self.add_widget(Display())
#         # self.add_widget(Buttons())
#        pass
      
# class EZCalculatorApp(App):
#     def build(self):
#         root_widget = FloatLayout()
#         root_widget.add_widget(Calculator()) 
#         return root_widget
   
# if __name__ == "__main__":
#     EZCalculatorApp().run()


