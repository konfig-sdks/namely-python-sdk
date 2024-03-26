# coding: utf-8

"""
    Namely API

    Move your app forward with the Namely API Move your app forward with the Namely API

    Generated by: https://konfigthis.com
"""

from namely_python_sdk.paths.teams_id.get import GetRaw
from namely_python_sdk.paths.group_types.get import GetAllGroupTypesRaw
from namely_python_sdk.paths.groups_id.get import GetGroupDetailsRaw
from namely_python_sdk.paths.group_types_id.get import GetGroupTypeDetailsRaw
from namely_python_sdk.paths.group_types_id_groups.get import GetGroupTypeGroupsRaw
from namely_python_sdk.paths.groups.get import GroupsRaw
from namely_python_sdk.paths.teams.get import TeamsRaw


class GroupsTeamsApiRaw(
    GetRaw,
    GetAllGroupTypesRaw,
    GetGroupDetailsRaw,
    GetGroupTypeDetailsRaw,
    GetGroupTypeGroupsRaw,
    GroupsRaw,
    TeamsRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
