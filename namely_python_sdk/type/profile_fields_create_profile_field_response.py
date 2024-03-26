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
from namely_python_sdk.type.meta import Meta
from namely_python_sdk.type.profile_fields_create_profile_field_response_linked import ProfileFieldsCreateProfileFieldResponseLinked
from namely_python_sdk.type.profile_fields_create_profile_field_response_links import ProfileFieldsCreateProfileFieldResponseLinks

class RequiredProfileFieldsCreateProfileFieldResponse(TypedDict):
    pass

class OptionalProfileFieldsCreateProfileFieldResponse(TypedDict, total=False):
    fields: typing.List[Field]

    meta: Meta

    links: ProfileFieldsCreateProfileFieldResponseLinks

    linked: ProfileFieldsCreateProfileFieldResponseLinked

class ProfileFieldsCreateProfileFieldResponse(RequiredProfileFieldsCreateProfileFieldResponse, OptionalProfileFieldsCreateProfileFieldResponse):
    pass
