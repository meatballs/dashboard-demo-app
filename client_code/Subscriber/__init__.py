from ._anvil_designer import SubscriberTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class Subscriber(SubscriberTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def refresh_download_speed(self, speed):
    self.label_1.text = f"{speed:.0f}"

  def form_show(self, **event_args):
    self.call_js("set_form")


