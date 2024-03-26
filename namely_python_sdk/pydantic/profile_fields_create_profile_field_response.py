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

from namely_python_sdk.pydantic.field import Field
from namely_python_sdk.pydantic.meta import Meta
from namely_python_sdk.pydantic.profile_fields_create_profile_field_response_linked import ProfileFieldsCreateProfileFieldResponseLinked
from namely_python_sdk.pydantic.profile_fields_create_profile_field_response_links import ProfileFieldsCreateProfileFieldResponseLinks

class ProfileFieldsCreateProfileFieldResponse(BaseModel):
    fields: typing.Optional[typing.List[Field]] = Field(None, alias='fields')

    meta: typing.Optional[Meta] = Field(None, alias='meta')

    links: typing.Optional[ProfileFieldsCreateProfileFieldResponseLinks] = Field(None, alias='links')

    linked: typing.Optional[ProfileFieldsCreateProfileFieldResponseLinked] = Field(None, alias='linked')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
