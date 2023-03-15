from kivy.uix.label import Label
from kivy.app import App

class MainApp(App):
    def build(self):
        label = Label(text="Hello Wolrd!")

        return label
    
app = MainApp()
app.run()