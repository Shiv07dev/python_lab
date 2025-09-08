from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.anchorlayout import AnchorLayout

# Set background color for the window
Window.clearcolor = (0.95, 0.95, 1, 1)

class LoginApp(App):
    def build(self):
        # Main vertical layout
        main_layout = BoxLayout(orientation='vertical', padding=40, spacing=25)

        # Title Label
        title = Label(
            text="Login Portal",
            font_size='28sp',
            bold=True,
            color=(0.15, 0.2, 0.5, 1)
        )
        main_layout.add_widget(title)

        # Username Field
        main_layout.add_widget(Label(
            text="Username:",
            font_size='18sp',
            color=(0.2, 0.2, 0.5, 1)
        ))
        self.username_input = TextInput(
            multiline=False,
            font_size='16sp',
            background_normal='',
            background_color=(1, 1, 1, 1),
            foreground_color=(0, 0, 0, 1),
            cursor_color=(0.2, 0.2, 0.5, 1),
            size_hint=(1, None),
            height=40
        )
        main_layout.add_widget(self.username_input)

        # Password Field
        main_layout.add_widget(Label(
            text="Password:",
            font_size='18sp',
            color=(0.2, 0.2, 0.5, 1)
        ))
        self.password_input = TextInput(
            password=True,
            multiline=False,
            font_size='16sp',
            background_normal='',
            background_color=(1, 1, 1, 1),
            foreground_color=(0, 0, 0, 1),
            cursor_color=(0.2, 0.2, 0.5, 1),
            size_hint=(1, None),
            height=40
        )
        main_layout.add_widget(self.password_input)

        # AnchorLayout for centering the login button
        button_layout = AnchorLayout(anchor_x='center', anchor_y='center')
        self.login_button = Button(
            text="Login",
            font_size='18sp',
            background_normal='',
            background_color=(0.2, 0.5, 0.8, 1),
            color=(1, 1, 1, 1),
            size_hint=(None, None),
            size=(160, 50)
        )
        self.login_button.bind(on_press=self.check_credentials)
        button_layout.add_widget(self.login_button)
        main_layout.add_widget(button_layout)

        # Status Label
        self.status_label = Label(
            text="",
            font_size='16sp',
            color=(0.2, 0.2, 0.2, 1)
        )
        main_layout.add_widget(self.status_label)

        return main_layout

    def check_credentials(self, instance):
        username = self.username_input.text.strip()
        password = self.password_input.text.strip()

        if username == "admin" and password == "password":
            self.status_label.text = "✅ Login Successful"
            self.status_label.color = (0, 0.6, 0, 1)
        else:
            self.status_label.text = "❌ Invalid Credentials"
            self.status_label.color = (1, 0, 0, 1)

# Run the app
if __name__ == '__main__':
    LoginApp().run()
