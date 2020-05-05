from ._anvil_designer import MainTemplate
from anvil import *
from ..Dashboard import Dashboard

class Main(MainTemplate):
  def __init__(self, **properties):
    self.add_component(Result())
    self.init_components(**properties)
