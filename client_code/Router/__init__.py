from ._anvil_designer import RouterTemplate
from anvil import *

class Router(RouterTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)


  def ok_button_click(self, **event_args):
    self.call_js("set_router_url", self.url_text_box.text)
    self.raise_event("x-close-alert")
    

