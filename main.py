from cgitb import text
from random import random
from turtle import Screen
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
import time
import random

class MainApp(App):
    txtfappl = {'Compartment 1' : 0,
        'Compartment 2' : 0,
        'Compartment 3' : 0,
        'Compartment 4' : 0}
    turns = 0
    randomint = random.randint(1,15)
    txtfappl[random.choice(["Compartment 1", "Compartment 2", "Compartment 3", "Compartment 4"])] += randomint
    print ('After/Initial:',txtfappl)
    time.sleep(2)

    def build(self):
        
        main_layout = BoxLayout(orientation="vertical")
        self.display = Label(text=str(self.txtfappl),
                            size_hint = (.5, .5),
                            pos_hint = {'center_x': 0.5, 'center_y': 0.75})
        self.solution = TextInput(
            multiline=False, readonly=True, halign="right", font_size=55
        )
        main_layout.add_widget(self.display)
        main_layout.add_widget(self.solution)
        buttons = [
            ["Compartment 1", "Compartment 2", "Compartment 3", "Compartment 4"],
        ]
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        equals_button = Button(
            text="Enter", pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)
        
        return main_layout

    def on_button_press(self, instance):
      print (self.display.text)
      current = self.solution.text
      button_text = instance.text
      randomint1 = random.randint(1,15)
      new_text = button_text
      self.solution.text = new_text
      self.last_button = button_text

    def on_solution(self, instance):
      
      self.txtfappl[self.solution.text] -= random.randint(1,self.randomint)
      self.turns += 1
      print ('Before:',self.txtfappl)
      print ('---------------')
      self.display.text = str(self.txtfappl)
      randomint = random.randint(1,10)
      self.txtfappl[random.choice(["Compartment 1", "Compartment 2", "Compartment 3", "Compartment 4"])] += randomint
      self.display.text = str(self.txtfappl)
      if (self.txtfappl['Compartment 1'] >= 50) or (self.txtfappl['Compartment 2'] >= 50) or (self.txtfappl['Compartment 3'] >= 50) or (self.txtfappl['Compartment 4'] >= 50):
        print ('you scored',self.turns)
        App.get_running_app().stop()
      print ('After/Initial:',self.txtfappl)
      
if __name__ == '__main__':
    app = MainApp()
    app.run()