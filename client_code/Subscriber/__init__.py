from ._anvil_designer import SubscriberTemplate
from anvil import *
import anvil.server

class Subscriber(SubscriberTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)


