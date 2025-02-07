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

from namely_python_sdk.type.file import File
from namely_python_sdk.type.job_title_link import JobTitleLink
from namely_python_sdk.type.profile import Profile

class RequiredGetNotificationsResponseLinked(TypedDict):
    pass

class OptionalGetNotificationsResponseLinked(TypedDict, total=False):
    profiles: typing.List[Profile]

    job_titles: typing.List[JobTitleLink]

    files: typing.List[File]

class GetNotificationsResponseLinked(RequiredGetNotificationsResponseLinked, OptionalGetNotificationsResponseLinked):
    pass
