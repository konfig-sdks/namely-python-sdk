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


class CreateResource(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "resources",
        }
        
        class properties:
            
            
            class resources(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['CreateResourcePayload']:
                        return CreateResourcePayload
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['CreateResourcePayload'], typing.List['CreateResourcePayload']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'resources':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'CreateResourcePayload':
                    return super().__getitem__(i)
            __annotations__ = {
                "resources": resources,
            }
    
    resources: MetaOapg.properties.resources
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resources"]) -> MetaOapg.properties.resources: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["resources", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resources"]) -> MetaOapg.properties.resources: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["resources", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        resources: typing.Union[MetaOapg.properties.resources, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateResource':
        return super().__new__(
            cls,
            *args,
            resources=resources,
            _configuration=_configuration,
            **kwargs,
        )

from namely_python_sdk.model.create_resource_payload import CreateResourcePayload
