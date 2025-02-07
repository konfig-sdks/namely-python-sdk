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

from namely_python_sdk.pydantic.job_title_links import JobTitleLinks

class JobTitle(BaseModel):
    # name/label of the job title
    title: typing.Optional[str] = Field(None, alias='title')

    # unique identifier of the job title
    id: typing.Optional[str] = Field(None, alias='id')

    # id of the job tier associated with the job title (when creating a job title, the key is \"parent\")
    parent_id: typing.Optional[str] = Field(None, alias='parent_id')

    links: typing.Optional[JobTitleLinks] = Field(None, alias='links')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
