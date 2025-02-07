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

from namely_python_sdk.type.create_job_title_payload import CreateJobTitlePayload

class RequiredCreateJobTitle(TypedDict):
    job_titles: typing.List[CreateJobTitlePayload]

class OptionalCreateJobTitle(TypedDict, total=False):
    pass

class CreateJobTitle(RequiredCreateJobTitle, OptionalCreateJobTitle):
    pass
