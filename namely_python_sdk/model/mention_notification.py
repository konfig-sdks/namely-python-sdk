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


class MentionNotification(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.IntSchema
            
            
            class text(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'[Full name] has [mentioned/appreciated] [you/team name] in a [post/comment].',
                    }]
            
            
            class type(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'com.<<company>>.namely.notifications.<<type>>',
                    }]
            timestamp = schemas.IntSchema
            seen = schemas.StrSchema
            read = schemas.StrSchema
        
            @staticmethod
            def links() -> typing.Type['MentionNotificationLinks']:
                return MentionNotificationLinks
            __annotations__ = {
                "id": id,
                "text": text,
                "type": type,
                "timestamp": timestamp,
                "seen": seen,
                "read": read,
                "links": links,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["text"]) -> MetaOapg.properties.text: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["seen"]) -> MetaOapg.properties.seen: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["read"]) -> MetaOapg.properties.read: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["links"]) -> 'MentionNotificationLinks': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "text", "type", "timestamp", "seen", "read", "links", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["text"]) -> typing.Union[MetaOapg.properties.text, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timestamp"]) -> typing.Union[MetaOapg.properties.timestamp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["seen"]) -> typing.Union[MetaOapg.properties.seen, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["read"]) -> typing.Union[MetaOapg.properties.read, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["links"]) -> typing.Union['MentionNotificationLinks', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "text", "type", "timestamp", "seen", "read", "links", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        text: typing.Union[MetaOapg.properties.text, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        timestamp: typing.Union[MetaOapg.properties.timestamp, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        seen: typing.Union[MetaOapg.properties.seen, str, schemas.Unset] = schemas.unset,
        read: typing.Union[MetaOapg.properties.read, str, schemas.Unset] = schemas.unset,
        links: typing.Union['MentionNotificationLinks', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MentionNotification':
        return super().__new__(
            cls,
            *args,
            id=id,
            text=text,
            type=type,
            timestamp=timestamp,
            seen=seen,
            read=read,
            links=links,
            _configuration=_configuration,
            **kwargs,
        )

from namely_python_sdk.model.mention_notification_links import MentionNotificationLinks
