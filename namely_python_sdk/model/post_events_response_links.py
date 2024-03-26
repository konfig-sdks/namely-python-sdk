# coding: utf-8

"""
    Namely API

    Move your app forward with the Namely API Move your app forward with the Namely API

    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from namely_python_sdk import schemas  # noqa: F401


class PostEventsResponseLinks(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def events_profile() -> typing.Type['Link']:
                return Link
        
            @staticmethod
            def events_comments() -> typing.Type['Link']:
                return Link
        
            @staticmethod
            def events_file() -> typing.Type['Link']:
                return Link
        
            @staticmethod
            def comments_profile() -> typing.Type['Link']:
                return Link
        
            @staticmethod
            def profile_image() -> typing.Type['Link']:
                return Link
            __annotations__ = {
                "events.profile": events_profile,
                "events.comments": events_comments,
                "events.file": events_file,
                "comments.profile": comments_profile,
                "profile.image": profile_image,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["events.profile"]) -> 'Link': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["events.comments"]) -> 'Link': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["events.file"]) -> 'Link': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["comments.profile"]) -> 'Link': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["profile.image"]) -> 'Link': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["events.profile", "events.comments", "events.file", "comments.profile", "profile.image", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["events.profile"]) -> typing.Union['Link', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["events.comments"]) -> typing.Union['Link', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["events.file"]) -> typing.Union['Link', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["comments.profile"]) -> typing.Union['Link', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["profile.image"]) -> typing.Union['Link', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["events.profile", "events.comments", "events.file", "comments.profile", "profile.image", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PostEventsResponseLinks':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from namely_python_sdk.model.link import Link
