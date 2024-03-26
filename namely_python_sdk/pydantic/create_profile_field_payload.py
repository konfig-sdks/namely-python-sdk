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


class CreateProfileFieldPayload(BaseModel):
    # label of the profile field; cannot contain special characters; cannot contain word \"id\"; must be unique; immutable <code>name</code> will be auto-generated based on label
    label: str = Field(alias='label')

    # id of the profile field section in which you want the place the field
    section: str = Field(alias='section')

    # field type; valid values are <code>text</code>, <code>long_text</code>, <code>date</code>, <code>file</code>, and <code>number</code>
    type: str = Field(alias='type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
