# coding: utf-8

"""
    Namely API

    Move your app forward with the Namely API Move your app forward with the Namely API

    Generated by: https://konfigthis.com
"""

from namely_python_sdk.paths.group_types.get import GetAllGroupTypesRaw
from namely_python_sdk.paths.groups_id.get import GetGroupDetailsRaw
from namely_python_sdk.paths.groups.get import GroupsRaw


class GroupsApiRaw(
    GetAllGroupTypesRaw,
    GetGroupDetailsRaw,
    GroupsRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
