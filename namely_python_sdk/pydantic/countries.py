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


class Countries(BaseModel):
    # unique identifier of the profile; 2-digit ISO code; used when passing home or office <code>address</code>
    id: typing.Optional[str] = Field(None, alias='id')

    # name of the country
    name: typing.Optional[str] = Field(None, alias='name')

    # name of the country's subdivision (e.g. State, Province)
    subdivision_type: typing.Optional[str] = Field(None, alias='subdivision_type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
