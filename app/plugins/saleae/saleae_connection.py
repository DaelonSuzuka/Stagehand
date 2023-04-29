from qtstrap import *
from saleae import automation


@singleton
class SaleaeConnection:
    def __init__(self):
        self.manager = None

    def connect(self):
        self.manager = automation.Manager.connect()

    def close(self):
        if self.manager is None:
            return
        
        self.manager.close()