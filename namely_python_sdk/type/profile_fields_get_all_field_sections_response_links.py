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


RequiredProfileFieldsGetAllFieldSectionsResponseLinks = TypedDict("RequiredProfileFieldsGetAllFieldSectionsResponseLinks", {
    })

OptionalProfileFieldsGetAllFieldSectionsResponseLinks = TypedDict("OptionalProfileFieldsGetAllFieldSectionsResponseLinks", {
    "sections.fields": str,
    }, total=False)

class ProfileFieldsGetAllFieldSectionsResponseLinks(RequiredProfileFieldsGetAllFieldSectionsResponseLinks, OptionalProfileFieldsGetAllFieldSectionsResponseLinks):
    pass
