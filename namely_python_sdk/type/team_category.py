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


class RequiredTeamCategory(TypedDict):
    pass

class OptionalTeamCategory(TypedDict, total=False):
    # name/label of the team category
    title: str

    # unique identifier of the team category
    id: str

class TeamCategory(RequiredTeamCategory, OptionalTeamCategory):
    pass
