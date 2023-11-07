from os import getenv
from ricxappframe.xapp_frame import Xapp, rmr
from .utils.constants import Constants
from .manager.A1PolicyManager import A1PolicyManager
from mdclogpy import Logger


managerxapp = None
logger = Logger(name=__name__)
            
def _entry(self):
    """
    Function that processes messages for which no handler is defined. This is the default handler
    """
    #Check healthcheck of xapp

    logger.debug("Managerxapp health is:: {}".format(managerxapp.healthcheck()))

    a1_mgr = A1PolicyManager(managerxapp)
    a1_mgr.startup()
    
    for (summary, sbuf) in self.rmr_get_messages():
        logger.debug("Managerxapp.A1PolicyHandler.default_handler called for msg type = " + str(summary[rmr.RMR_MS_MSG_TYPE]))
        logger.debug("Managerxapp.A1PolicyHandler.default_handler called and says:: Received summary is {}".format(summary))
        self.rmr_free(sbuf)

    
    

    
def start():
    """
    This is a convenience function that allows this xapp to run in Docker
    for "real" (no thread, real SDL), but also easily modified for unit testing
    (e.g., use_fake_sdl). The defaults for this function are for the Dockerized xapp.
    """ 

    logger.debug("Managerxapp is starting.......")
    global managerxapp 
    fake_sdl = getenv("USE_FAKE_SDL", None)
    managerxapp = Xapp(entrypoint= _entry,
                       rmr_port=4560,
                       use_fake_sdl=bool(fake_sdl))
    logger.debug("Managerxapp created .......")

    

     #self.createHandlers()
    managerxapp.run()
     
    
def stop(self):
    """
    can only be called if thread=True when started
    TODO: could we register a signal handler for Docker SIGTERM that calls this?
    """
    managerxapp.stop()
    