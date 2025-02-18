from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from repositories import FileUserRepository
from services import UserService

class CreateAccountWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    created = ObjectProperty(None)

    def submit(self):
        if user_service.create_user(self.email.text, self.password.text, self.namee.text, self.created.text):
            self.reset()
            sm.current = "login"
        else:
            self.show_popup("Error", "E-mail already exists")

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    @staticmethod
    def show_popup(title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(None, None), size=(400, 400))
        popup.open()

class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def login(self):
        if user_service.login(self.email.text, self.password.text):
            main_window = sm.get_screen('main')
            user_info = user_service.get_user_info(self.email.text)
            main_window.n.text = user_info[1]
            main_window.email.text = self.email.text
            main_window.created.text = user_info[2]
            sm.current = "main"
        else:
            self.show_popup("Error", "Invalid email or password")

    @staticmethod
    def show_popup(title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(None, None), size=(400, 400))
        popup.open()

class MainWindow(Screen):
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    current = ""

class WindowManager(ScreenManager):
    pass

kv_path = "mnt/c/temp/Interface-python-bradesco/statics/layout.kv"
kv = Builder.load_file(kv_path)

sm = WindowManager()
user_repository = FileUserRepository("mnt/c/temp/Interface-python-bradesco/users.txt")
user_service = UserService(user_repository)
screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"), MainWindow(name="main")]
for screen in screens:
    sm.add_widget(screen)
sm.current = "login"

class MyMainApp(App):
    def build(self):
        return sm

if __name__ == "__main__":
    MyMainApp().run()
