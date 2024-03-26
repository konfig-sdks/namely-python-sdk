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


class RequiredMeta(TypedDict):
    pass

class OptionalMeta(TypedDict, total=False):
    # number of total objects
    count: int

    # HTTP response
    status: int

class Meta(RequiredMeta, OptionalMeta):
    pass
