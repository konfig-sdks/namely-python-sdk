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


class ProfileFieldsGetAllFieldSectionsResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class sections(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Section']:
                        return Section
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Section'], typing.List['Section']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'sections':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Section':
                    return super().__getitem__(i)
        
            @staticmethod
            def meta() -> typing.Type['Meta']:
                return Meta
        
            @staticmethod
            def links() -> typing.Type['ProfileFieldsGetAllFieldSectionsResponseLinks']:
                return ProfileFieldsGetAllFieldSectionsResponseLinks
        
            @staticmethod
            def linked() -> typing.Type['ProfileFieldsGetAllFieldSectionsResponseLinked']:
                return ProfileFieldsGetAllFieldSectionsResponseLinked
            __annotations__ = {
                "sections": sections,
                "meta": meta,
                "links": links,
                "linked": linked,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sections"]) -> MetaOapg.properties.sections: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["meta"]) -> 'Meta': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["links"]) -> 'ProfileFieldsGetAllFieldSectionsResponseLinks': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["linked"]) -> 'ProfileFieldsGetAllFieldSectionsResponseLinked': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["sections", "meta", "links", "linked", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sections"]) -> typing.Union[MetaOapg.properties.sections, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["meta"]) -> typing.Union['Meta', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["links"]) -> typing.Union['ProfileFieldsGetAllFieldSectionsResponseLinks', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["linked"]) -> typing.Union['ProfileFieldsGetAllFieldSectionsResponseLinked', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["sections", "meta", "links", "linked", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        sections: typing.Union[MetaOapg.properties.sections, list, tuple, schemas.Unset] = schemas.unset,
        meta: typing.Union['Meta', schemas.Unset] = schemas.unset,
        links: typing.Union['ProfileFieldsGetAllFieldSectionsResponseLinks', schemas.Unset] = schemas.unset,
        linked: typing.Union['ProfileFieldsGetAllFieldSectionsResponseLinked', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProfileFieldsGetAllFieldSectionsResponse':
        return super().__new__(
            cls,
            *args,
            sections=sections,
            meta=meta,
            links=links,
            linked=linked,
            _configuration=_configuration,
            **kwargs,
        )

from namely_python_sdk.model.meta import Meta
from namely_python_sdk.model.profile_fields_get_all_field_sections_response_linked import ProfileFieldsGetAllFieldSectionsResponseLinked
from namely_python_sdk.model.profile_fields_get_all_field_sections_response_links import ProfileFieldsGetAllFieldSectionsResponseLinks
from namely_python_sdk.model.section import Section
