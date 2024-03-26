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

from namely_python_sdk.type.job_title import JobTitle

class RequiredJobsInfoCreateJobTierResponseLinked(TypedDict):
    pass

class OptionalJobsInfoCreateJobTierResponseLinked(TypedDict, total=False):
    job_titles: typing.List[JobTitle]

class JobsInfoCreateJobTierResponseLinked(RequiredJobsInfoCreateJobTierResponseLinked, OptionalJobsInfoCreateJobTierResponseLinked):
    pass
