from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

# Set background color of the window
Window.clearcolor = (0.95, 0.95, 1, 1)  # Soft light purple

# Defining the calculator layout and logic
class CalculatorGrid(GridLayout):
    def __init__(self, **kwargs):
        super(CalculatorGrid, self).__init__(**kwargs)
        self.cols = 4
        self.padding = [20, 20, 20, 20]
        self.spacing = [10, 10]

        # Result display
        self.result = TextInput(
            font_size=36,
            readonly=True,
            halign="right",
            multiline=False,
            background_color=(1, 1, 1, 1),
            foreground_color=(0, 0, 0, 1),
            size_hint=(1, 0.2),
            padding_y=(10, 10)
        )
        self.add_widget(self.result)

        # Buttons for numbers and operations
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '.', '0', '=', '+'
        ]

        for button in buttons:
            self.add_widget(Button(
                text=button,
                font_size=26,
                background_color=(0.2, 0.6, 0.9, 1),
                color=(1, 1, 1, 1),
                size_hint=(1, 0.2),
                on_press=self.on_button_press
            ))

        # Clear Button
        self.add_widget(Button(
            text="C",
            font_size=26,
            background_color=(1, 0.4, 0.4, 1),
            color=(1, 1, 1, 1),
            size_hint=(1, 0.2),
            on_press=self.clear_result
        ))

    def on_button_press(self, instance):
        current_text = self.result.text
        button_text = instance.text

        if button_text == "=":
            try:
                self.result.text = str(eval(current_text))
            except Exception:
                self.result.text = "Error"
        else:
            if current_text == "Error":
                self.result.text = button_text
            else:
                self.result.text += button_text

    def clear_result(self, instance):
        self.result.text = ""

# Main App class
class CalculatorApp(App):
    def build(self):
        return CalculatorGrid()

# Run the app
if __name__ == '__main__':
    CalculatorApp().run()
