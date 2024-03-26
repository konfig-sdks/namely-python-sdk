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

from namely_python_sdk.pydantic.company_info_get_info_response_authentications import CompanyInfoGetInfoResponseAuthentications

class CompanyInfoGetInfoResponse(BaseModel):
    # Compay name
    name: typing.Optional[str] = Field(None, alias='name')

    # Company permalink, the subdomain before namely.com
    permalink: typing.Optional[str] = Field(None, alias='permalink')

    # Background image on the login page.
    background_url: typing.Optional[str] = Field(None, alias='background_url')

    # Logo image on the home page.
    logo_url: typing.Optional[str] = Field(None, alias='logo_url')

    authentications: typing.Optional[CompanyInfoGetInfoResponseAuthentications] = Field(None, alias='authentications')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
