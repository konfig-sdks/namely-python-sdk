# coding: utf-8

"""
    Namely API

    Move your app forward with the Namely API Move your app forward with the Namely API

    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING


class RequiredNotificationLinks(TypedDict):
    pass

class OptionalNotificationLinks(TypedDict, total=False):
    # unique identifier of the time off request mentioned in the notification
    time_off_request_id: str

    # id of the profile associated with the time off request mentioned in the notification
    profile_id: str

    # id of the profile that requested the time off mentioned in the notification; requester_id does not have to be the same as profile_id if time off was requested on someone else's behalf
    requester_id: str

    # only present if the request has been responded to; id of the profile that responded to the time off request mentioned in the notification
    responder_id: str

class NotificationLinks(RequiredNotificationLinks, OptionalNotificationLinks):
    pass
