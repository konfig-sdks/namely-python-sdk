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

from namely_python_sdk.pydantic.file import File
from namely_python_sdk.pydantic.linked_profile import LinkedProfile

class HomeFeedCreateEventCommentResponseLinked(BaseModel):
    profiles: typing.Optional[typing.List[LinkedProfile]] = Field(None, alias='profiles')

    files: typing.Optional[typing.List[File]] = Field(None, alias='files')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
