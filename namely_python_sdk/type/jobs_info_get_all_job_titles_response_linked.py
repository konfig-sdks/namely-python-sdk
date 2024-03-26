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

from namely_python_sdk.type.job_tier import JobTier

class RequiredJobsInfoGetAllJobTitlesResponseLinked(TypedDict):
    pass

class OptionalJobsInfoGetAllJobTitlesResponseLinked(TypedDict, total=False):
    job_tiers: typing.List[JobTier]

class JobsInfoGetAllJobTitlesResponseLinked(RequiredJobsInfoGetAllJobTitlesResponseLinked, OptionalJobsInfoGetAllJobTitlesResponseLinked):
    pass
