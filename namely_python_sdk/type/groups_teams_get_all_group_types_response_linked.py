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

from namely_python_sdk.type.group_type import GroupType

class RequiredGroupsTeamsGetAllGroupTypesResponseLinked(TypedDict):
    pass

class OptionalGroupsTeamsGetAllGroupTypesResponseLinked(TypedDict, total=False):
    group_types: typing.List[GroupType]

class GroupsTeamsGetAllGroupTypesResponseLinked(RequiredGroupsTeamsGetAllGroupTypesResponseLinked, OptionalGroupsTeamsGetAllGroupTypesResponseLinked):
    pass
