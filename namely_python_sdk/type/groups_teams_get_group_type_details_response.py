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

from namely_python_sdk.type.group_type import GroupType
from namely_python_sdk.type.groups_teams_get_group_type_details_response_linked import GroupsTeamsGetGroupTypeDetailsResponseLinked
from namely_python_sdk.type.groups_teams_get_group_type_details_response_links import GroupsTeamsGetGroupTypeDetailsResponseLinks
from namely_python_sdk.type.meta import Meta

class RequiredGroupsTeamsGetGroupTypeDetailsResponse(TypedDict):
    pass

class OptionalGroupsTeamsGetGroupTypeDetailsResponse(TypedDict, total=False):
    group_types: typing.List[GroupType]

    meta: Meta

    links: GroupsTeamsGetGroupTypeDetailsResponseLinks

    linked: GroupsTeamsGetGroupTypeDetailsResponseLinked

class GroupsTeamsGetGroupTypeDetailsResponse(RequiredGroupsTeamsGetGroupTypeDetailsResponse, OptionalGroupsTeamsGetGroupTypeDetailsResponse):
    pass
