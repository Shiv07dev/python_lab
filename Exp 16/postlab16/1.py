from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

# Set background to white
Window.clearcolor = (1, 1, 1, 1)

class CounterApp(App):
    def build(self):
        self.counter = 0

        layout = BoxLayout(orientation='vertical', padding=40, spacing=30)

        self.label = Label(
            text="You clicked: 0",
            font_size=40,
            color=(0.1, 0.1, 0.1, 1)
        )

        self.button = Button(
            text="Click Me",
            font_size=24,
            size_hint=(1, 0.3),
            background_color=(0.2, 0.5, 0.9, 1),
            color=(1, 1, 1, 1)
        )
        self.button.bind(on_press=self.increment_counter)

        layout.add_widget(self.label)
        layout.add_widget(self.button)

        return layout

    def increment_counter(self, instance):
        self.counter += 1
        self.label.text = f"You clicked: {self.counter}"

if __name__ == '__main__':
    CounterApp().run()
