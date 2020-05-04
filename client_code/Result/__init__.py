from ._anvil_designer import ResultTemplate
from anvil import *
import anvil.server

class Result(ResultTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
