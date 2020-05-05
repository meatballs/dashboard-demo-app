from ._anvil_designer import ResultTemplate
from anvil import *
import anvil.server

class Result(ResultTemplate):
  def __init__(self, **properties):
    self.subscriber.set_event_handler("x-download-speed-updated", self.refresh_download_speed)
    self.subscriber.set_event_handler("x-cpu-percent-updated", self.refresh_cpu_percent)
    self.init_components(**properties)

  def refresh_download_speed(self, download_speed, timestamp, **event_args):
    display_speed = download_speed / 10 ** 6
    self.item["download_speed"] = f"{display_speed:.2f} Mbps"
    self.refresh_data_bindings()
    
  def refresh_cpu_percent(self, cpu_percent, **event_args):
    self.item["cpu_percent"] = f"{cpu_percent} %"
    self.refresh_data_bindings()