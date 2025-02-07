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


class GroupSingularLinks(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            group_type = schemas.StrSchema
        
            @staticmethod
            def profiles() -> typing.Type['GroupSingularLinksProfiles']:
                return GroupSingularLinksProfiles
            __annotations__ = {
                "group_type": group_type,
                "profiles": profiles,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["group_type"]) -> MetaOapg.properties.group_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["profiles"]) -> 'GroupSingularLinksProfiles': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["group_type", "profiles", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["group_type"]) -> typing.Union[MetaOapg.properties.group_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["profiles"]) -> typing.Union['GroupSingularLinksProfiles', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["group_type", "profiles", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        group_type: typing.Union[MetaOapg.properties.group_type, str, schemas.Unset] = schemas.unset,
        profiles: typing.Union['GroupSingularLinksProfiles', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GroupSingularLinks':
        return super().__new__(
            cls,
            *args,
            group_type=group_type,
            profiles=profiles,
            _configuration=_configuration,
            **kwargs,
        )

from namely_python_sdk.model.group_singular_links_profiles import GroupSingularLinksProfiles
