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


class Home(BaseModel):
    # address line 1 of the home address
    address1: typing.Optional[str] = Field(None, alias='address1')

    # address line 2 of the home address
    address2: typing.Optional[str] = Field(None, alias='address2')

    # city of the home address
    city: typing.Optional[str] = Field(None, alias='city')

    # state of the home address; for US, must be the 2-digit code; for other countries, refer to the #docTextSection:7izuT4kPbi3FngZbD endpoints
    state_id: typing.Optional[str] = Field(None, alias='state_id')

    # \"US\" for the US; must be the ISO Alpha-2 code; for other countries, refer to the #docTextSection:7izuT4kPbi3FngZbD endpoints or just use the ISO Alpha-2 code
    country_id: typing.Optional[str] = Field(None, alias='country_id')

    # zip or postal code of the home address
    zip: typing.Optional[str] = Field(None, alias='zip')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
