from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image, AsyncImage

class MyApp(App):
    def build(self):
        label = Label(
            text="Hello world",
            size_hint=(.5, .5),
            pos_hint={"center_x": .5, "center_y": .5}
        )
        return label



if __name__ == "__main__":
    MyApp().run()