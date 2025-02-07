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

from namely_python_sdk.type.section import Section

class RequiredProfileFieldsGetAllFieldsResponseLinked(TypedDict):
    pass

class OptionalProfileFieldsGetAllFieldsResponseLinked(TypedDict, total=False):
    sections: typing.List[Section]

class ProfileFieldsGetAllFieldsResponseLinked(RequiredProfileFieldsGetAllFieldsResponseLinked, OptionalProfileFieldsGetAllFieldsResponseLinked):
    pass
