from ._anvil_designer import SubscriberTemplate
from anvil import *

class Subscriber(SubscriberTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

  def form_show(self, **event_args):
    self.call_js("set_form")