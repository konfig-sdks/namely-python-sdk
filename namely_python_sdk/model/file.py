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


class File(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.StrSchema
            filename = schemas.StrSchema
            mime_type = schemas.StrSchema
            original = schemas.StrSchema
            
            
            class thumbs(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Thumb']:
                        return Thumb
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Thumb'], typing.List['Thumb']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'thumbs':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Thumb':
                    return super().__getitem__(i)
            __annotations__ = {
                "id": id,
                "filename": filename,
                "mime_type": mime_type,
                "original": original,
                "thumbs": thumbs,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["filename"]) -> MetaOapg.properties.filename: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mime_type"]) -> MetaOapg.properties.mime_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["original"]) -> MetaOapg.properties.original: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["thumbs"]) -> MetaOapg.properties.thumbs: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "filename", "mime_type", "original", "thumbs", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["filename"]) -> typing.Union[MetaOapg.properties.filename, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mime_type"]) -> typing.Union[MetaOapg.properties.mime_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["original"]) -> typing.Union[MetaOapg.properties.original, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["thumbs"]) -> typing.Union[MetaOapg.properties.thumbs, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "filename", "mime_type", "original", "thumbs", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        filename: typing.Union[MetaOapg.properties.filename, str, schemas.Unset] = schemas.unset,
        mime_type: typing.Union[MetaOapg.properties.mime_type, str, schemas.Unset] = schemas.unset,
        original: typing.Union[MetaOapg.properties.original, str, schemas.Unset] = schemas.unset,
        thumbs: typing.Union[MetaOapg.properties.thumbs, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'File':
        return super().__new__(
            cls,
            *args,
            id=id,
            filename=filename,
            mime_type=mime_type,
            original=original,
            thumbs=thumbs,
            _configuration=_configuration,
            **kwargs,
        )

from namely_python_sdk.model.thumb import Thumb
