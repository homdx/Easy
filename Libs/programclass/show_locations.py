# -*- coding: utf-8 -*-
#
# show_locations.py
#

from kivy.uix.gridlayout import GridLayout


class ShowLocations(object):
    def show_locations(self, *args):
        screen = self.Screen(name='locations')

        # self.screen.ids.action_previous.previous_image = \
        #    'atlas://data/images/defaulttheme/previous_normal'
        # self.screen.ids.action_previous.app_icon = \
        #    'Data/Images/shops/{}.png'.format(self.shop)

        # scroll_icons.add_widget(box_locations)
        box_menu = GridLayout(cols=2)

        for i, location in enumerate(self.locations):
            box_menu.add_widget(
                self.CustomMenuItem(
                    background_item=self.core.background_locations[i],
                    icon_item='Data/Images/locations/{}.png'.format(location),
                    text_item=self.core.dict_locations[location],
                    id_item=location, text_color=self.get_color_from_hex(
                        self.core.theme_text_color),
                    events_callback=self.events_program
                )
            )

        screen.add_widget(box_menu)
        self.screen.ids.screen_manager.add_widget(screen)
        effect = self.choice(self.effects_transition)
        self.screen.ids.screen_manager.transition = effect()
        self.screen.ids.screen_manager.current = 'locations'
        # self.screen.ids.action_previous.title = \
        #    self.core.string_name_shop.format(self.shop.capitalize())
        self.set_current_item_tabbed_panel(
            self.get_hex_from_color(self.core.color_action_bar),
            self.core.theme_text_color
        )
