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

from namely_python_sdk.type.group import Group
from namely_python_sdk.type.groups_teams_get_group_type_groups_response_linked import GroupsTeamsGetGroupTypeGroupsResponseLinked
from namely_python_sdk.type.groups_teams_get_group_type_groups_response_links import GroupsTeamsGetGroupTypeGroupsResponseLinks
from namely_python_sdk.type.meta_group import MetaGroup

class RequiredGroupsTeamsGetGroupTypeGroupsResponse(TypedDict):
    pass

class OptionalGroupsTeamsGetGroupTypeGroupsResponse(TypedDict, total=False):
    groups: typing.List[Group]

    meta: MetaGroup

    links: GroupsTeamsGetGroupTypeGroupsResponseLinks

    linked: GroupsTeamsGetGroupTypeGroupsResponseLinked

class GroupsTeamsGetGroupTypeGroupsResponse(RequiredGroupsTeamsGetGroupTypeGroupsResponse, OptionalGroupsTeamsGetGroupTypeGroupsResponse):
    pass
