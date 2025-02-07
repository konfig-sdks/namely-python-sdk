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

from namely_python_sdk.pydantic.address import Address
from namely_python_sdk.pydantic.group_links import GroupLinks

class Group(BaseModel):
    # name/label of the group
    title: typing.Optional[str] = Field(None, alias='title')

    # unique identifier of the group
    id: typing.Optional[str] = Field(None, alias='id')

    # name of the group type to which the group belongs
    type: typing.Optional[str] = Field(None, alias='type')

    # true if the group is a team
    is_team: typing.Optional[bool] = Field(None, alias='is_team')

    address: typing.Optional[Address] = Field(None, alias='address')

    # number of profiles associated with this group
    count: typing.Optional[int] = Field(None, alias='count')

    links: typing.Optional[GroupLinks] = Field(None, alias='links')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
