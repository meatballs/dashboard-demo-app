from ._anvil_designer import MainTemplate
from anvil import *
from ..Dashboard import Dashboard
from ..Router import Router

class Main(MainTemplate):
  def __init__(self, **properties):
    alert(content=Router(), large=True, buttons=[])
    self.add_component(Dashboard())
    self.init_components(**properties)
