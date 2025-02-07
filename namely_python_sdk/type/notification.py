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

from namely_python_sdk.type.notification_links import NotificationLinks

class RequiredNotification(TypedDict):
    pass

class OptionalNotification(TypedDict, total=False):
    # unique identifier of the notification
    id: int

    # content of the notification
    text: str

    # type of notification; type = pto.responded, pto.new, pto.deleted
    type: str

    # epoch time that the event was created/generated
    timestamp: int

    # <code>true</code> if the token bearer has viewed the list of notifications since this notification was created
    seen: str

    # <code>true</code> if the token bearer has clicked/tapped on the the notification
    read: str

    links: NotificationLinks

class Notification(RequiredNotification, OptionalNotification):
    pass
