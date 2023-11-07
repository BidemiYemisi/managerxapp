from ricxappframe.xapp_frame import Xapp
from abc import ABC

class _BaseManager(ABC):
    """
    Represents base Manager Abstract class
    Here initialize variables which will be common to all xapp

    Parameters:
        rmr_xapp: Reference to original RMRxappframe object
    """
    
    
    def __init__(self, xapp: Xapp):  # Constructor
        self._xapp = xapp
        self.logger = self._xapp.logger
        
        