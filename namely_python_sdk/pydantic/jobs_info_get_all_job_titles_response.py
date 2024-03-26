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

from namely_python_sdk.pydantic.job_title import JobTitle
from namely_python_sdk.pydantic.jobs_info_get_all_job_titles_response_linked import JobsInfoGetAllJobTitlesResponseLinked
from namely_python_sdk.pydantic.jobs_info_get_all_job_titles_response_links import JobsInfoGetAllJobTitlesResponseLinks
from namely_python_sdk.pydantic.meta import Meta

class JobsInfoGetAllJobTitlesResponse(BaseModel):
    job_titles: typing.Optional[typing.List[JobTitle]] = Field(None, alias='job_titles')

    meta: typing.Optional[Meta] = Field(None, alias='meta')

    links: typing.Optional[JobsInfoGetAllJobTitlesResponseLinks] = Field(None, alias='links')

    linked: typing.Optional[JobsInfoGetAllJobTitlesResponseLinked] = Field(None, alias='linked')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
