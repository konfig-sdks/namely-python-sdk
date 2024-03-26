# coding: utf-8

"""
    Namely API

    Move your app forward with the Namely API Move your app forward with the Namely API

    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict

from namely_python_sdk.pydantic.get_resources_response_meta import GetResourcesResponseMeta
from namely_python_sdk.pydantic.resource import Resource

class GetResourcesResponse(BaseModel):
    resources: typing.Optional[typing.List[Resource]] = Field(None, alias='resources')

    meta: typing.Optional[GetResourcesResponseMeta] = Field(None, alias='meta')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
