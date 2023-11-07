import json
from ricxappframe.xapp_frame import Xapp, rmr
from ..utils.constants import Constants
from ._BaseManager import _BaseManager


class A1PolicyManager(_BaseManager):
    def __init__(self, xapp: Xapp):
        super().__init__(xapp)

    # Send A1 policy query
    def startup(self):
        policy_query = ('{"policy_type_id":"' + str(Constants.MANAGERXAPP_POLICY_ID) + '"}')  # this will construct a json byte obj in the form "{"policy_type_id":"2"}", key:value can be anything
        self._xapp.rmr_send(policy_query.encode(), Constants.A1_POLICY_QUERY)  # this will be "b'{"policy_type_id":"2"}', 20012" b'{"policy_type_id":"2"}' IS THE PAYLOAD and the 20012 which is the msg_type will be the value we will query for in the A1 polices. There will be a callback function registered to react to the 20012 msg_type in another xapp function. The callback function that will react to it will be the one passed to register_callback() method
        self.logger.info("A1PolicyManager.startup:: Sent A1 policy query = " + policy_query)
