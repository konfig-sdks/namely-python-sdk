# coding: utf-8

"""
    Namely API

    Move your app forward with the Namely API Move your app forward with the Namely API

    Generated by: https://konfigthis.com
"""

from namely_python_sdk.paths.profiles_fields_sections.get import GetAllFieldSections
from namely_python_sdk.paths.profiles_fields_sections_id.get import GetFieldSection
from namely_python_sdk.paths.profiles_fields_sections_id.put import UpdateFieldInSection
from namely_python_sdk.apis.tags.profile_fields_sections_api_raw import ProfileFieldsSectionsApiRaw


class ProfileFieldsSectionsApi(
    GetAllFieldSections,
    GetFieldSection,
    UpdateFieldInSection,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ProfileFieldsSectionsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ProfileFieldsSectionsApiRaw(api_client)
