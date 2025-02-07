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

from namely_python_sdk.pydantic.section_block_titles import SectionBlockTitles
from namely_python_sdk.pydantic.section_links import SectionLinks

class Section(BaseModel):
    # label of the profile field section; only editable on through the API via the #endpoint:eoL989Gmn6vnfSPbE</a> endpoint
    title: typing.Optional[str] = Field(None, alias='title')

    # unique identifier of the profile field section
    id: typing.Optional[str] = Field(None, alias='id')

    block_titles: typing.Optional[SectionBlockTitles] = Field(None, alias='block_titles')

    links: typing.Optional[SectionLinks] = Field(None, alias='links')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
