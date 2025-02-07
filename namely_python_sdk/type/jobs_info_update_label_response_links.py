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

from namely_python_sdk.type.link import Link

RequiredJobsInfoUpdateLabelResponseLinks = TypedDict("RequiredJobsInfoUpdateLabelResponseLinks", {
    })

OptionalJobsInfoUpdateLabelResponseLinks = TypedDict("OptionalJobsInfoUpdateLabelResponseLinks", {
    "job_tiers.job_titles": Link,
    }, total=False)

class JobsInfoUpdateLabelResponseLinks(RequiredJobsInfoUpdateLabelResponseLinks, OptionalJobsInfoUpdateLabelResponseLinks):
    pass
