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

from namely_python_sdk.type.field import Field

class RequiredProfileFieldsGetAllFieldSectionsResponseLinked(TypedDict):
    pass

class OptionalProfileFieldsGetAllFieldSectionsResponseLinked(TypedDict, total=False):
    fields: typing.List[Field]

class ProfileFieldsGetAllFieldSectionsResponseLinked(RequiredProfileFieldsGetAllFieldSectionsResponseLinked, OptionalProfileFieldsGetAllFieldSectionsResponseLinked):
    pass
