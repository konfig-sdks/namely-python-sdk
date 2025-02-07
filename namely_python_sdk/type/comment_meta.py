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


class RequiredCommentMeta(TypedDict):
    pass

class OptionalCommentMeta(TypedDict, total=False):
    # HTTP response
    status: int

    page: int

    # <code>true</code> if the company has mentioning enabled on the home feed
    use_at_mentions: bool

class CommentMeta(RequiredCommentMeta, OptionalCommentMeta):
    pass
