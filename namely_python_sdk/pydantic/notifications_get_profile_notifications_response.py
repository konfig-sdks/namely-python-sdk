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

from namely_python_sdk.pydantic.generic_notification import GenericNotification
from namely_python_sdk.pydantic.notifications_get_profile_notifications_response_linked import NotificationsGetProfileNotificationsResponseLinked
from namely_python_sdk.pydantic.notifications_get_profile_notifications_response_links import NotificationsGetProfileNotificationsResponseLinks

class NotificationsGetProfileNotificationsResponse(BaseModel):
    notifications: typing.Optional[GenericNotification] = Field(None, alias='notifications')

    links: typing.Optional[NotificationsGetProfileNotificationsResponseLinks] = Field(None, alias='links')

    linked: typing.Optional[NotificationsGetProfileNotificationsResponseLinked] = Field(None, alias='linked')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
