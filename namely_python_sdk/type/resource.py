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


class RequiredResource(TypedDict):
    pass

class OptionalResource(TypedDict, total=False):
    # name/label of the resource file
    title: str

    # unique identifier of the resource file
    id: str

    link: str

    # file name of the resource file
    file_name: str

    file_format: str

    file_size: str

    file_url: str

    last_edited: str

    # <code>id</code> of the folder in which the resource file sits; <code>null</code> if not in a folder
    folder_id: int

class Resource(RequiredResource, OptionalResource):
    pass
