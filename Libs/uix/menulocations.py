# menulocations.py

from kivy.uix.gridlayout import GridLayout
from kivy.properties import ListProperty

from custommenu import CustomMenuItem


class MenuLocations(GridLayout):
    icons_menu = ListProperty([])
    icons_backgrounds = ListProperty([])

    def __init__(self, **kwargs):
        super(MenuLocations, self).__init__(cols=2)

        for i, icon in enumerate(self.icons_menu):
            self.add_widget(
                CustomMenuItem(
                    text_item=icon, events_callback=self.on_click,
                    icon_item='Data/Images/locations/{}'.format(icon),
                    id_item=icon, background_item=self.icons_backgrounds[i]
                )
            )

    def on_click(self, name_locations):
        '''
        :type name_locations: str;

        '''

        return name_locations
