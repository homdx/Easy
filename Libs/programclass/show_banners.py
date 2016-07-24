# -*- coding: utf-8 -*-
#
# show_banners.py
#

import os

from kivy.uix.boxlayout import BoxLayout

from Libs.uix.imagebutton import ImageButton


class ShowBanners(object):
    '''Меняет и выводит на главном экране рекламные баннеры.'''

    def __init__(self):
        self.banner_list = os.listdir(
            '{}/Data/Images/banners'.format(self.directory)
        )
        # Направление смены слайдов баннеров.
        self.directions = ('up', 'down', 'left', 'right')

    def show_banners(self, interval):
        if self.screen.ids.screen_manager.current == '':
            name_banner = self.choice(self.banner_list)

            box_banner = BoxLayout()
            new_banner = ImageButton(
                id=name_banner.split('.')[0],
                source='Data/Images/banners/{}'.format(name_banner),
                on_release=self.press_banner
            )
            box_banner.add_widget(new_banner)

            name_screen = name_banner
            banner = self.Screen(name=name_screen)
            banner.add_widget(box_banner)
            self.screen.ids.banner_manager.add_widget(banner)
            effect = self.choice(self.effects_transition)
            direction = self.choice(self.directions)
            if effect != self.SwapTransition:
                self.screen.ids.banner_manager.transition = effect(
                    direction=direction
                )
            else:
                self.screen.ids.banner_manager.transition = effect()
            self.screen.ids.banner_manager.current = name_screen
            self.screen.ids.banner_manager.screens.pop()

    def press_banner(self, instance_banner):
        if isinstance(instance_banner, str):
            print(instance_banner)
        else:
            print(instance_banner.id)
