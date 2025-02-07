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

from namely_python_sdk.type.update_profile_field_payload import UpdateProfileFieldPayload

class RequiredUpdateProfileField(TypedDict):
    fields: typing.List[UpdateProfileFieldPayload]

class OptionalUpdateProfileField(TypedDict, total=False):
    pass

class UpdateProfileField(RequiredUpdateProfileField, OptionalUpdateProfileField):
    pass
