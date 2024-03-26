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


class HomeFeedCreateEventLikeResponseMessage(BaseModel):
    # total number of likes on event
    likes_count: typing.Optional[int] = Field(None, alias='likes_count')

    # <code>true</code> if the token bearer has liked this event (will always be true with a 200 response)
    liked_by_current_profile: typing.Optional[bool] = Field(None, alias='liked_by_current_profile')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
