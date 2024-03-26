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


class RequiredSubdivision(TypedDict):
    pass

class OptionalSubdivision(TypedDict, total=False):
    # unique identifier of the subdivision unit (e.g. NJ); abbreviation of the name; used in the #model:yq9tkBR24wuBhzizY model
    id: str

    # name of the subdivision unit (e.g. New Jersey)
    name: str

class Subdivision(RequiredSubdivision, OptionalSubdivision):
    pass
