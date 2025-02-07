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


class ProfileReportsToItem(BaseModel):
    # unique identifier of the profile to whom the profile of this object reports; <code>no_guid</code> if null; cannot be <code>null</code> if any other <code>reports_to</code> keys provided
    id: typing.Optional[str] = Field(None, alias='id')

    # first name of the profile to whom the profile of this object reports; <code>Nobody</code> if null; cannot be <code>null</code> if any other <code>reports_to</code> keys provided
    first_name: typing.Optional[str] = Field(None, alias='first_name')

    # last name of the profile to whom the profile of this object reports; <code>Nobody</code> if null; cannot be <code>null</code> if any other <code>reports_to</code> keys provided
    last_name: typing.Optional[str] = Field(None, alias='last_name')

    # company email of the profile to whom the profile of this object reports; <code>None</code> if null; cannot be <code>null</code> if any other <code>reports_to</code> keys provided
    email: typing.Optional[str] = Field(None, alias='email')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
