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


class Dental(BaseModel):
    # relationship of the profile's dental plan's beneficiary to the profile; valid values include <code>Employee Only</code>, <code>Employee/Child</code>, <code>Employee/Spouse</code>, <code>Family</code>, <code>Not Applicable</code>, and <code>Waive</code>; blank if never provided or provided then deleted; cannot be <code>null</code> if any other <code>dental</code> keys provided
    beneficiary: typing.Optional[str] = Field(None, alias='beneficiary')

    # amount of the profile's dental plan; numbers only; cannot be <code>null</code> if any other <code>dental</code> keys provided
    amount: typing.Optional[str] = Field(None, alias='amount')

    # currency type of the profile's dental plan amount; default <code>USD</code>
    currency_type: typing.Optional[str] = Field(None, alias='currency_type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
