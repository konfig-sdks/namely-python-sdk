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

from namely_python_sdk.pydantic.event import Event
from namely_python_sdk.pydantic.events_meta import EventsMeta
from namely_python_sdk.pydantic.post_events_response_linked import PostEventsResponseLinked
from namely_python_sdk.pydantic.post_events_response_links import PostEventsResponseLinks

class PostEventsResponse(BaseModel):
    events: typing.Optional[typing.List[Event]] = Field(None, alias='events')

    meta: typing.Optional[EventsMeta] = Field(None, alias='meta')

    links: typing.Optional[PostEventsResponseLinks] = Field(None, alias='links')

    linked: typing.Optional[PostEventsResponseLinked] = Field(None, alias='linked')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
