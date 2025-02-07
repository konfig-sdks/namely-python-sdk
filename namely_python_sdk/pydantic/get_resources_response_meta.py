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


class GetResourcesResponseMeta(BaseModel):
    is_super_admin: typing.Optional[bool] = Field(None, alias='is_super_admin')

    accepted_file_extensions: typing.Optional[str] = Field(None, alias='accepted_file_extensions')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
