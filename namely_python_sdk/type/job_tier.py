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

from namely_python_sdk.type.job_tier_links import JobTierLinks

class RequiredJobTier(TypedDict):
    pass

class OptionalJobTier(TypedDict, total=False):
    # name/label of the job tier
    title: str

    # unique identifier of the job tier
    id: str

    numerical_id: str

    links: JobTierLinks

class JobTier(RequiredJobTier, OptionalJobTier):
    pass
