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


class EventsMeta(BaseModel):
    # HTTP response
    response: typing.Optional[int] = Field(None, alias='response')

    # <code>true</code> if the company has commenting enabled on the home feed; same on the <code>event</code> object
    use_comments: typing.Optional[bool] = Field(None, alias='use_comments')

    # <code>true</code> if the token bearer has a role with permission to post announcements on the home feed
    use_updates: typing.Optional[bool] = Field(None, alias='use_updates')

    # <code>true</code> if the company has mentioning enabled on the home feed
    use_mentions: typing.Optional[bool] = Field(None, alias='use_mentions')

    # <code>true</code> if the company has appreciations enabled on the home feed
    use_appreciations: typing.Optional[bool] = Field(None, alias='use_appreciations')

    # <code>true</code> if the company has likes enabled on the home feed
    use_likes: typing.Optional[bool] = Field(None, alias='use_likes')

    # number of events returned on the page
    count: typing.Optional[int] = Field(None, alias='count')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
