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

from namely_python_sdk.type.create_folder_payload import CreateFolderPayload

class RequiredCreateFolder(TypedDict):
    folders: typing.List[CreateFolderPayload]

class OptionalCreateFolder(TypedDict, total=False):
    pass

class CreateFolder(RequiredCreateFolder, OptionalCreateFolder):
    pass
