from kivy.app import App
from kivy.uix.image import AsyncImage

class MainApp(App):
    def build(self):
        aimg = AsyncImage(source='https://www.python.org/static/community_logos/python-logo-inkscape.svg',
                    size_hint=(1, .5),
                    pos_hint={'center_x':.5, 'center_y':.5})

        return aimg

if __name__ == '__main__':
    app = MainApp()
    app.run()