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


class Thumb(BaseModel):
    75x75_: typing.Optional[str] = Field(None, alias='75x75')

    75x75c_: typing.Optional[str] = Field(None, alias='75x75c')

    150x150_: typing.Optional[str] = Field(None, alias='150x150')

    150x150c_: typing.Optional[str] = Field(None, alias='150x150c')

    300x300_: typing.Optional[str] = Field(None, alias='300x300')

    300x300c_: typing.Optional[str] = Field(None, alias='300x300c')

    450x450_: typing.Optional[str] = Field(None, alias='450x450')

    550x450c_: typing.Optional[str] = Field(None, alias='550x450c')

    800x800_: typing.Optional[str] = Field(None, alias='800x800')

    800x800c_: typing.Optional[str] = Field(None, alias='800x800c')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
