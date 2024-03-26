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


class JobsInfoCreateJobTierResponseLinked(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class job_titles(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['JobTitle']:
                        return JobTitle
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['JobTitle'], typing.List['JobTitle']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'job_titles':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'JobTitle':
                    return super().__getitem__(i)
            __annotations__ = {
                "job_titles": job_titles,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["job_titles"]) -> MetaOapg.properties.job_titles: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["job_titles", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["job_titles"]) -> typing.Union[MetaOapg.properties.job_titles, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["job_titles", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        job_titles: typing.Union[MetaOapg.properties.job_titles, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'JobsInfoCreateJobTierResponseLinked':
        return super().__new__(
            cls,
            *args,
            job_titles=job_titles,
            _configuration=_configuration,
            **kwargs,
        )

from namely_python_sdk.model.job_title import JobTitle
