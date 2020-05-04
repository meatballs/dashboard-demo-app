from ._anvil_designer import ResultTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Result(ResultTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
