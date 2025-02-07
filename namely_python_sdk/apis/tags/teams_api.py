# coding: utf-8

"""
    Namely API

    Move your app forward with the Namely API Move your app forward with the Namely API

    Generated by: https://konfigthis.com
"""

from namely_python_sdk.paths.teams.get import Teams
from namely_python_sdk.apis.tags.teams_api_raw import TeamsApiRaw


class TeamsApi(
    Teams,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: TeamsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = TeamsApiRaw(api_client)
