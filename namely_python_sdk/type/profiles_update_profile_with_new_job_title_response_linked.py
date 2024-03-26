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
from namely_python_sdk.type.group import Group
from namely_python_sdk.type.job_title import JobTitle
from namely_python_sdk.type.team import Team

class RequiredProfilesUpdateProfileWithNewJobTitleResponseLinked(TypedDict):
    pass

class OptionalProfilesUpdateProfileWithNewJobTitleResponseLinked(TypedDict, total=False):
    job_titles: typing.List[JobTitle]

    files: typing.List[File]

    groups: typing.List[Group]

    teams: typing.List[Team]

class ProfilesUpdateProfileWithNewJobTitleResponseLinked(RequiredProfilesUpdateProfileWithNewJobTitleResponseLinked, OptionalProfilesUpdateProfileWithNewJobTitleResponseLinked):
    pass
