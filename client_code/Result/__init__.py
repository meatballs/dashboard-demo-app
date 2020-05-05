from ._anvil_designer import ResultTemplate
from anvil import *
import anvil.server

class Result(ResultTemplate):
  def __init__(self, **properties):
    self.subscriber.set_event_handler("x-download-speed-updated", self.refresh_download_speed)
    self.subscriber.set_event_handler("x-cpu-percent-updated", self.refresh_cpu_percent)
    self.init_components(**properties)

  def refresh_download_speed(self, **event_args):
    self.item["download_speed"] = download
    self.refresh_data_bindings()
    
  def refresh_cpu_percent(self, cpu_percent, **event_args):
    self.item["cpu_percent"] = cpu_percent