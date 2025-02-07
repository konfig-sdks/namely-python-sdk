# coding: utf-8

"""
    Namely API

    Move your app forward with the Namely API Move your app forward with the Namely API

    Generated by: https://konfigthis.com
"""

from namely_python_sdk.paths.events_id_comments.post import CreateEventComment
from namely_python_sdk.paths.likes_event_id.post import CreateEventLike
from namely_python_sdk.paths.events_id.delete import DeleteAnnouncement
from namely_python_sdk.paths.likes_event_comment_comment_id.delete import DeleteEventCommentLike
from namely_python_sdk.paths.events.get import Events
from namely_python_sdk.paths.events.post import Events0
from namely_python_sdk.paths.events_id.get import GetEvent
from namely_python_sdk.paths.likes_event_comment_comment_id_recent.get import GetEventCommentLikes
from namely_python_sdk.paths.events_event_id_comments.get import GetEventComments
from namely_python_sdk.paths.likes_event_event_id_recent.get import GetEventLikes
from namely_python_sdk.paths.likes_event_comment_comment_id.post import LikeEventComment
from namely_python_sdk.paths.events_event_id_comments_comment_id.delete import RemoveEventComment
from namely_python_sdk.paths.likes_event_event_id.delete import RemoveEventLike
from namely_python_sdk.apis.tags.home_feed_api_raw import HomeFeedApiRaw


class HomeFeedApi(
    CreateEventComment,
    CreateEventLike,
    DeleteAnnouncement,
    DeleteEventCommentLike,
    Events,
    Events0,
    GetEvent,
    GetEventCommentLikes,
    GetEventComments,
    GetEventLikes,
    LikeEventComment,
    RemoveEventComment,
    RemoveEventLike,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: HomeFeedApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = HomeFeedApiRaw(api_client)
