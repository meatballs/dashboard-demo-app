from ._anvil_designer import MainTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from ..Result import Result

class Main(MainTemplate):
  def __init__(self, **properties):
    self.add_component(Result())
    self.init_components(**properties)

    # Any code you write here will run when the form opens.


