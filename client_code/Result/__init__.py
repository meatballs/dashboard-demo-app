from ._anvil_designer import ResultTemplate
from anvil import *
import anvil.server

class Result(ResultTemplate):
  def __init__(self, **properties):
    self.subscriber.set_event_handler("x-download-speed-updated", self.refresh_download_speed)
    self.init_components(**properties)

  def refresh_download_speed(self, **event_args):
    self.item["download_speed"] = event_args["download"]