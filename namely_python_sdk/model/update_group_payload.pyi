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


class UpdateGroupPayload(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "address",
            "group_type",
            "title",
        }
        
        class properties:
            title = schemas.StrSchema
        
            @staticmethod
            def address() -> typing.Type['Address']:
                return Address
            group_type = schemas.StrSchema
            __annotations__ = {
                "title": title,
                "address": address,
                "group_type": group_type,
            }
    
    address: 'Address'
    group_type: MetaOapg.properties.group_type
    title: MetaOapg.properties.title
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address"]) -> 'Address': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["group_type"]) -> MetaOapg.properties.group_type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "address", "group_type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> 'Address': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["group_type"]) -> MetaOapg.properties.group_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "address", "group_type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        address: 'Address',
        group_type: typing.Union[MetaOapg.properties.group_type, str, ],
        title: typing.Union[MetaOapg.properties.title, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UpdateGroupPayload':
        return super().__new__(
            cls,
            *args,
            address=address,
            group_type=group_type,
            title=title,
            _configuration=_configuration,
            **kwargs,
        )

from namely_python_sdk.model.address import Address
