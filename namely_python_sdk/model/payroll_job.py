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


class PayrollJob(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.StrSchema
            name = schemas.StrSchema
            code = schemas.StrSchema
            is_active = schemas.BoolSchema
            is_default = schemas.BoolSchema
            is_active_formatted = schemas.StrSchema
            payroll_company_id = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "name": name,
                "code": code,
                "is_active": is_active,
                "is_default": is_default,
                "is_active_formatted": is_active_formatted,
                "payroll_company_id": payroll_company_id,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_active"]) -> MetaOapg.properties.is_active: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_default"]) -> MetaOapg.properties.is_default: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_active_formatted"]) -> MetaOapg.properties.is_active_formatted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payroll_company_id"]) -> MetaOapg.properties.payroll_company_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "code", "is_active", "is_default", "is_active_formatted", "payroll_company_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["code"]) -> typing.Union[MetaOapg.properties.code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_active"]) -> typing.Union[MetaOapg.properties.is_active, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_default"]) -> typing.Union[MetaOapg.properties.is_default, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_active_formatted"]) -> typing.Union[MetaOapg.properties.is_active_formatted, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payroll_company_id"]) -> typing.Union[MetaOapg.properties.payroll_company_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "code", "is_active", "is_default", "is_active_formatted", "payroll_company_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        code: typing.Union[MetaOapg.properties.code, str, schemas.Unset] = schemas.unset,
        is_active: typing.Union[MetaOapg.properties.is_active, bool, schemas.Unset] = schemas.unset,
        is_default: typing.Union[MetaOapg.properties.is_default, bool, schemas.Unset] = schemas.unset,
        is_active_formatted: typing.Union[MetaOapg.properties.is_active_formatted, str, schemas.Unset] = schemas.unset,
        payroll_company_id: typing.Union[MetaOapg.properties.payroll_company_id, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PayrollJob':
        return super().__new__(
            cls,
            *args,
            id=id,
            name=name,
            code=code,
            is_active=is_active,
            is_default=is_default,
            is_active_formatted=is_active_formatted,
            payroll_company_id=payroll_company_id,
            _configuration=_configuration,
            **kwargs,
        )
