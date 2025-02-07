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

from namely_python_sdk.pydantic.group_singular import GroupSingular
from namely_python_sdk.pydantic.groups_teams_get_group_details_response_linked import GroupsTeamsGetGroupDetailsResponseLinked
from namely_python_sdk.pydantic.groups_teams_get_group_details_response_links import GroupsTeamsGetGroupDetailsResponseLinks
from namely_python_sdk.pydantic.meta_group import MetaGroup

class GroupsTeamsGetGroupDetailsResponse(BaseModel):
    groups: typing.Optional[typing.List[GroupSingular]] = Field(None, alias='groups')

    meta: typing.Optional[MetaGroup] = Field(None, alias='meta')

    links: typing.Optional[GroupsTeamsGetGroupDetailsResponseLinks] = Field(None, alias='links')

    linked: typing.Optional[GroupsTeamsGetGroupDetailsResponseLinked] = Field(None, alias='linked')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
