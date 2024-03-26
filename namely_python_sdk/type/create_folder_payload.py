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


class RequiredCreateFolderPayload(TypedDict):
    title: str

class OptionalCreateFolderPayload(TypedDict, total=False):
    pass

class CreateFolderPayload(RequiredCreateFolderPayload, OptionalCreateFolderPayload):
    pass
