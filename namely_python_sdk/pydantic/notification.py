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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from namely_python_sdk.pydantic.notification_links import NotificationLinks

class Notification(BaseModel):
    # unique identifier of the notification
    id: typing.Optional[int] = Field(None, alias='id')

    # content of the notification
    text: typing.Optional[str] = Field(None, alias='text')

    # type of notification; type = pto.responded, pto.new, pto.deleted
    type: typing.Optional[str] = Field(None, alias='type')

    # epoch time that the event was created/generated
    timestamp: typing.Optional[int] = Field(None, alias='timestamp')

    # <code>true</code> if the token bearer has viewed the list of notifications since this notification was created
    seen: typing.Optional[str] = Field(None, alias='seen')

    # <code>true</code> if the token bearer has clicked/tapped on the the notification
    read: typing.Optional[str] = Field(None, alias='read')

    links: typing.Optional[NotificationLinks] = Field(None, alias='links')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
