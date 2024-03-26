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

from namely_python_sdk.pydantic.column import Column
from namely_python_sdk.pydantic.content import Content

class Report(BaseModel):
    # unique identifier of the report; identical to the <code>id</code> in the path parameters
    id: typing.Optional[str] = Field(None, alias='id')

    # describes the type of report (e.g. salary_history)
    type: typing.Optional[str] = Field(None, alias='type')

    columns: typing.Optional[typing.List[Column]] = Field(None, alias='columns')

    content: typing.Optional[typing.List[Content]] = Field(None, alias='content')

    links: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='links')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
