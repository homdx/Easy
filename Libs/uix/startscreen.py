# -*- coding: utf-8 -*-
#
# startscreen.py
#

import os

from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import ObjectProperty, ListProperty, StringProperty

from Libs.uix.custombutton import CustomButton


root = os.path.split(__file__)[0]
root = root if root != '' else os.getcwd()


class StartScreen(BoxLayout):
    events_callback = ObjectProperty(None)
    '''Функция обработки сигналов экрана.'''

    core = ObjectProperty(None)
    '''module 'Libs.programdata' '''

    color_action_bar = ListProperty(
        [0.4, 0.11764705882352941, 0.2901960784313726, 0.5607843137254902]
    )
    '''Цвет ActionBar.'''

    color_body_program = ListProperty(
        [0.15294117647058825, 0.0392156862745098, 0.11764705882352941, 1]
    )
    '''Цвет фона экранов программы.'''

    color_tabbed_panel = ListProperty(
        [0.15294117647058825, 0.0392156862745098, 0.11764705882352941, 1]
    )
    '''Цвет фона tabbed panel.'''

    title_previous = StringProperty('')
    '''Заголовок ActionBar.'''

    tabbed_text = StringProperty('')
    '''Текст пунктов кастомной tabbed panel.'''

    Builder.load_file('{}/kv/startscreen.kv'.format(root))

    def __init__(self, **kvargs):
        super(StartScreen, self).__init__(**kvargs)
        self.ids.custom_tabbed.bind(on_ref_press=self.events_callback)

        # Cписок магазинов.
        for name_shop in self.core.dict_shops.keys():
            self.ids.shops_list.add_widget(
                CustomButton(
                    text=self.core.dict_shops[name_shop],
                    icon='Data/Images/shops/{}.png'.format(name_shop),
                    icon_people='Data/Images/people.png',
                    icon_map='Data/Images/mapmarker.png',
                    events_callback=self.events_callback,
                )
            )
