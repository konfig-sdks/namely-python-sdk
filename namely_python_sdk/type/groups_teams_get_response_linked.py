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

from namely_python_sdk.type.team_category import TeamCategory

class RequiredGroupsTeamsGetResponseLinked(TypedDict):
    pass

class OptionalGroupsTeamsGetResponseLinked(TypedDict, total=False):
    categories: typing.List[TeamCategory]

class GroupsTeamsGetResponseLinked(RequiredGroupsTeamsGetResponseLinked, OptionalGroupsTeamsGetResponseLinked):
    pass
