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

from namely_python_sdk.type.countries import Countries

class RequiredGetCountriesResponse(TypedDict):
    pass

class OptionalGetCountriesResponse(TypedDict, total=False):
    countries: typing.List[Countries]

class GetCountriesResponse(RequiredGetCountriesResponse, OptionalGetCountriesResponse):
    pass
