from ._anvil_designer import DashboardTemplate
from anvil import *
import anvil.server

class Dashboard(DashboardTemplate):
  def __init__(self, **properties):
    self.subscriber.set_event_handler("x-download-speed-updated", self.refresh_download_speed)
    self.subscriber.set_event_handler("x-cpu-percent-updated", self.refresh_cpu_percent)
    self.init_components(**properties)

  def refresh_download_speed(self, download_speed, timestamp, **event_args):
    display_speed = download_speed / 10 ** 6
    self.download_speed_label.text = f"{display_speed:.1f} Mbps"
    
  def refresh_cpu_percent(self, cpu_percent, **event_args):
    self.cpu_percent_label.text = f"{cpu_percent} %"