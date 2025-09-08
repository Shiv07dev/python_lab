# Importing necessary modules from kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

# Set a background color for the entire window (light blue)
Window.clearcolor = (0.9, 0.95, 1, 1)

# Defining the main application class
class SimpleApp(App):
    def build(self):
        # Creating a layout with padding and spacing
        layout = BoxLayout(
            orientation='vertical',
            padding=40,
            spacing=20
        )
        
        # Creating a styled label and adding it to the layout
        self.label = Label(
            text="Hello, Shivkumar Paun",
            font_size='24sp',
            color=(0.2, 0.2, 0.5, 1),  # Dark blue text
            bold=True
        )
        layout.add_widget(self.label)
        
        # Creating a styled button, binding it, and adding it to the layout
        button = Button(
            text="Click Me!",
            font_size='20sp',
            background_color=(0.1, 0.5, 0.8, 1),  # Blue background
            color=(1, 1, 1, 1),  # White text
            size_hint=(1, 0.3)
        )
        button.bind(on_press=self.on_button_press)
        layout.add_widget(button)
        
        # Returning the layout to be displayed
        return layout
    
    # Function to handle button click event
    def on_button_press(self, instance):
        self.label.text = "Button Clicked!"

# Running the application
if __name__ == '__main__':
    SimpleApp().run()
