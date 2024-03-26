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


class RequiredCompanyResourcesGetFolderResourcesResponseMeta(TypedDict):
    pass

class OptionalCompanyResourcesGetFolderResourcesResponseMeta(TypedDict, total=False):
    is_super_admin: bool

    accepted_file_extensions: str

class CompanyResourcesGetFolderResourcesResponseMeta(RequiredCompanyResourcesGetFolderResourcesResponseMeta, OptionalCompanyResourcesGetFolderResourcesResponseMeta):
    pass
