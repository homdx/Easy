# custombutton.py

import os

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty, ListProperty

from . imagebutton import ImageButton


root = os.path.split(__file__)[0]
Builder.load_file('{}/kv/custombutton.kv'.format(
    root if root != '' else os.getcwd())
)


class CustomButton(BoxLayout, Button):
    icon = StringProperty('')
    icon_map = StringProperty('')
    icon_people = StringProperty('')
    text = StringProperty('')
    button_color = ListProperty([0, 0, 0, .2])
    text_color = ListProperty([0, 0, 0, .1])
    events_callback = ObjectProperty(None)
