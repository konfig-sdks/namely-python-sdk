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


class JobsInfoUpdateLabelResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class job_tiers(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['JobTier']:
                        return JobTier
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['JobTier'], typing.List['JobTier']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'job_tiers':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'JobTier':
                    return super().__getitem__(i)
        
            @staticmethod
            def meta() -> typing.Type['Meta']:
                return Meta
        
            @staticmethod
            def links() -> typing.Type['JobsInfoUpdateLabelResponseLinks']:
                return JobsInfoUpdateLabelResponseLinks
        
            @staticmethod
            def linked() -> typing.Type['JobsInfoUpdateLabelResponseLinked']:
                return JobsInfoUpdateLabelResponseLinked
            __annotations__ = {
                "job_tiers": job_tiers,
                "meta": meta,
                "links": links,
                "linked": linked,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["job_tiers"]) -> MetaOapg.properties.job_tiers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["meta"]) -> 'Meta': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["links"]) -> 'JobsInfoUpdateLabelResponseLinks': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["linked"]) -> 'JobsInfoUpdateLabelResponseLinked': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["job_tiers", "meta", "links", "linked", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["job_tiers"]) -> typing.Union[MetaOapg.properties.job_tiers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["meta"]) -> typing.Union['Meta', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["links"]) -> typing.Union['JobsInfoUpdateLabelResponseLinks', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["linked"]) -> typing.Union['JobsInfoUpdateLabelResponseLinked', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["job_tiers", "meta", "links", "linked", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        job_tiers: typing.Union[MetaOapg.properties.job_tiers, list, tuple, schemas.Unset] = schemas.unset,
        meta: typing.Union['Meta', schemas.Unset] = schemas.unset,
        links: typing.Union['JobsInfoUpdateLabelResponseLinks', schemas.Unset] = schemas.unset,
        linked: typing.Union['JobsInfoUpdateLabelResponseLinked', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'JobsInfoUpdateLabelResponse':
        return super().__new__(
            cls,
            *args,
            job_tiers=job_tiers,
            meta=meta,
            links=links,
            linked=linked,
            _configuration=_configuration,
            **kwargs,
        )

from namely_python_sdk.model.job_tier import JobTier
from namely_python_sdk.model.jobs_info_update_label_response_linked import JobsInfoUpdateLabelResponseLinked
from namely_python_sdk.model.jobs_info_update_label_response_links import JobsInfoUpdateLabelResponseLinks
from namely_python_sdk.model.meta import Meta
