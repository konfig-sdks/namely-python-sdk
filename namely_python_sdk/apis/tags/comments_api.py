# coding: utf-8

"""
    Namely API

    Move your app forward with the Namely API Move your app forward with the Namely API

    Generated by: https://konfigthis.com
"""

from namely_python_sdk.paths.events_id_comments.post import CreateEventComment
from namely_python_sdk.paths.events_event_id_comments.get import GetEventComments
from namely_python_sdk.paths.events_event_id_comments_comment_id.delete import RemoveEventComment
from namely_python_sdk.apis.tags.comments_api_raw import CommentsApiRaw


class CommentsApi(
    CreateEventComment,
    GetEventComments,
    RemoveEventComment,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: CommentsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = CommentsApiRaw(api_client)
