import pygame

from states.base_state import BaseState
from ui.widget import Widget
from ui.text import SingleLineText
from ui.link import LinkByMethod

from myapp.UI_elements.state_selector_top_bar import build as state_selector_top_bar

class TreeEditor(BaseState):
    def __init__(self, app):
        super().__init__(app)

        self.font = pygame.font.Font(self.app_state.text_font, 20)
        top_right_pos_link = LinkByMethod(self.app_state, lambda x: (x.screen_size[0] - 300, 50))
        self.ui_context.add_widget(Widget(top_right_pos_link, (300, 50), "yup", self.app, on_click=self.app.quit, background_color=(255, 0, 0)))

        self.ui_context.add_widget(state_selector_top_bar(LinkByMethod(self.app_state, lambda x: x.screen_size), self.app, self.font))

        self.ui_context.add_widget(SingleLineText((100, 100), (300, 50), "text", self.app, text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed eu.", font=self.font, background_color=(255, 0, 255), size_auto_fit=True, can_be_selected=True, editable=False))

    def update(self):
        self.ui_context.remove_widget(self.ui_context.getbywidget(self.ui_context["top_bar"]))
        self.ui_context.add_widget(state_selector_top_bar(LinkByMethod(self.app_state, lambda x: x.screen_size), self.app, self.font))
        super().update()
