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

from namely_python_sdk.pydantic.group_type import GroupType

class GroupsTeamsGetAllGroupTypesResponseLinked(BaseModel):
    group_types: typing.Optional[typing.List[GroupType]] = Field(None, alias='group_types')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
