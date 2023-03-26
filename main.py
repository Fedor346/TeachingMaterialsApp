from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class TeachingMaterialsApp(MDApp):
    def build(self):
        return MDLabel(text="Hello, Teaching Materials", halign="center")


TeachingMaterialsApp().run()