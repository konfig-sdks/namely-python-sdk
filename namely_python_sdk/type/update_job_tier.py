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

from namely_python_sdk.type.update_job_tier_payload import UpdateJobTierPayload

class RequiredUpdateJobTier(TypedDict):
    job_tiers: typing.List[UpdateJobTierPayload]

class OptionalUpdateJobTier(TypedDict, total=False):
    pass

class UpdateJobTier(RequiredUpdateJobTier, OptionalUpdateJobTier):
    pass
