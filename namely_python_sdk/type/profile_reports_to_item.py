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


class RequiredProfileReportsToItem(TypedDict):
    pass

class OptionalProfileReportsToItem(TypedDict, total=False):
    # unique identifier of the profile to whom the profile of this object reports; <code>no_guid</code> if null; cannot be <code>null</code> if any other <code>reports_to</code> keys provided
    id: str

    # first name of the profile to whom the profile of this object reports; <code>Nobody</code> if null; cannot be <code>null</code> if any other <code>reports_to</code> keys provided
    first_name: str

    # last name of the profile to whom the profile of this object reports; <code>Nobody</code> if null; cannot be <code>null</code> if any other <code>reports_to</code> keys provided
    last_name: str

    # company email of the profile to whom the profile of this object reports; <code>None</code> if null; cannot be <code>null</code> if any other <code>reports_to</code> keys provided
    email: str

class ProfileReportsToItem(RequiredProfileReportsToItem, OptionalProfileReportsToItem):
    pass
