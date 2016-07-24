# custommenu.py

import os

from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import ListProperty, StringProperty, ObjectProperty


root = os.path.split(__file__)[0]
Builder.load_file('{}/kv/custommenu.kv'.format(
    root if root != '' else os.getcwd())
)


class CustomMenuItem(BoxLayout):
    background_item = ListProperty([.1, .1, .1, 1])
    text_color = ListProperty([.1, .1, .1, 1])
    icon_item = StringProperty('')
    text_item = StringProperty('')
    id_item = StringProperty('')
    events_callback = ObjectProperty(None)
