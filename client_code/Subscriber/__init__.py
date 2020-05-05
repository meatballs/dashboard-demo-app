from ._anvil_designer import SubscriberTemplate
from anvil import *

class Subscriber(SubscriberTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

  def form_show(self, **event_args):
    self.call_js("set_form")
    
  def raise_download_speed_event(self, download_speed, timestamp):
    self.raise_event("x-download-speed-updated", download_speed, timestamp)
    
  def raise_cpu_percent_event(self, cpu_percent):
    self.raise_event("x-cpu-percent-updated", cpu_percent=cpu_percent)