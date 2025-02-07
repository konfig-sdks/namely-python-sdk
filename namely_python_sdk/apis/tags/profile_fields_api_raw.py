# coding: utf-8

"""
    Namely API

    Move your app forward with the Namely API Move your app forward with the Namely API

    Generated by: https://konfigthis.com
"""

from namely_python_sdk.paths.profiles_fields.post import CreateProfileFieldRaw
from namely_python_sdk.paths.profiles_fields_sections.get import GetAllFieldSectionsRaw
from namely_python_sdk.paths.profiles_fields.get import GetAllFieldsRaw
from namely_python_sdk.paths.profiles_fields_id.get import GetFieldInformationRaw
from namely_python_sdk.paths.profiles_fields_sections_id.get import GetFieldSectionRaw
from namely_python_sdk.paths.profiles_fields_id.put import UpdateFieldInSectionRaw
from namely_python_sdk.paths.profiles_fields_sections_id.put import UpdateFieldInSection0Raw


class ProfileFieldsApiRaw(
    CreateProfileFieldRaw,
    GetAllFieldSectionsRaw,
    GetAllFieldsRaw,
    GetFieldInformationRaw,
    GetFieldSectionRaw,
    UpdateFieldInSectionRaw,
    UpdateFieldInSection0Raw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
