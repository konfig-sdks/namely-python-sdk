# coding: utf-8

"""
    Namely API

    Move your app forward with the Namely API Move your app forward with the Namely API

    Generated by: https://konfigthis.com
"""

from namely_python_sdk.paths.events.get import Events
from namely_python_sdk.paths.events.post import Events0
from namely_python_sdk.paths.events_id.get import GetEvent
from namely_python_sdk.apis.tags.events_api_raw import EventsApiRaw


class EventsApi(
    Events,
    Events0,
    GetEvent,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: EventsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = EventsApiRaw(api_client)
