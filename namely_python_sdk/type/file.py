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

from namely_python_sdk.type.thumb import Thumb

class RequiredFile(TypedDict):
    pass

class OptionalFile(TypedDict, total=False):
    id: str

    filename: str

    mime_type: str

    original: str

    thumbs: typing.List[Thumb]

class File(RequiredFile, OptionalFile):
    pass
