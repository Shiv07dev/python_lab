from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

# Set white background
Window.clearcolor = (1, 1, 1, 1)

class TextInputApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=40, spacing=30)

        self.text_input = TextInput(
            hint_text="Type something...",
            font_size=20,
            size_hint=(1, 0.3),
            multiline=False,
            foreground_color=(0, 0, 0, 1),
            background_color=(0.95, 0.95, 0.95, 1),
            padding=(10, 10),
            cursor_color=(0.2, 0.6, 1, 1)
        )

        self.button = Button(
            text="Display Text",
            font_size=22,
            size_hint=(1, 0.3),
            background_color=(0.1, 0.7, 0.6, 1),
            color=(1, 1, 1, 1)
        )
        self.button.bind(on_press=self.show_text)

        self.label = Label(
            text="",
            font_size=30,
            color=(0, 0, 0, 1)
        )

        layout.add_widget(self.text_input)
        layout.add_widget(self.button)
        layout.add_widget(self.label)

        return layout

    def show_text(self, instance):
        self.label.text = self.text_input.text

if __name__ == '__main__':
    TextInputApp().run()
