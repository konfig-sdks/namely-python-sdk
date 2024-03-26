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

from namely_python_sdk.type.create_job_tier_payload import CreateJobTierPayload

class RequiredCreateJobTier(TypedDict):
    job_tiers: typing.List[CreateJobTierPayload]

class OptionalCreateJobTier(TypedDict, total=False):
    pass

class CreateJobTier(RequiredCreateJobTier, OptionalCreateJobTier):
    pass
