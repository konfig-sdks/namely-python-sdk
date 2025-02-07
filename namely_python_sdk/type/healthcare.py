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


class RequiredHealthcare(TypedDict):
    pass

class OptionalHealthcare(TypedDict, total=False):
    # relationship of the profile's healthcare plan's beneficiary to the profile; valid values include <code>Employee Only</code>, <code>Employee/Child</code>, <code>Employee/Spouse</code>, <code>Family</code>, <code>Not Applicable</code>, and <code>Waive</code>; blank if never provided or provided then deleted; cannot be <code>null</code> if any other <code>healthcare</code> keys provided
    beneficiary: str

    # amount of the profile's healthcare plan; numbers only; cannot be <code>null</code> if any other <code>healthcare</code> keys provided
    amount: str

    # currency type of the profile's healthcare plan amount; default <code>USD</code>
    currency_type: str

class Healthcare(RequiredHealthcare, OptionalHealthcare):
    pass
