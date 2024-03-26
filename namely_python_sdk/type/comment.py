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

from namely_python_sdk.type.comment_links import CommentLinks

class RequiredComment(TypedDict):
    pass

class OptionalComment(TypedDict, total=False):
    # unique identifier of the comment
    id: str

    # content of the comment, displayed in markdown
    content: str

    # content of the comment, displayed in HTML
    html_content: str

    # epoch time that the comment was created
    created_at: int

    # <code>true</code> if the token bearer has a role with permission to delete the comment; will always be <code>true</code> for one's own comment
    can_destroy: bool

    links: CommentLinks

    # the hour difference between UTC and the main office of the company
    utc_offset: int

    # total number of likes on comment
    likes_count: int

    # <code>true</code> if the token bearer has liked this comment
    liked_by_current_profile: bool

class Comment(RequiredComment, OptionalComment):
    pass
