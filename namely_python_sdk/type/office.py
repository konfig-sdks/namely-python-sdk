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


class RequiredOffice(TypedDict):
    pass

class OptionalOffice(TypedDict, total=False):
    # address line 1 of the office address
    address1: str

    # address line 2 of the office address
    address2: str

    # city of the office address
    city: str

    # state of the office address; for US, must be the 2-digit code; for other countries, refer to the #docTextSection:7izuT4kPbi3FngZbD endpoints
    state_id: str

    # \"US\" for the US; must be the ISO Alpha-2 code; for other countries, refer to the #docTextSection:7izuT4kPbi3FngZbD endpoints or just use the ISO Alpha-2 code
    country_id: str

    # zip or postal code of the office address
    zip: str

    # phone number associated with the office location
    phone: str

class Office(RequiredOffice, OptionalOffice):
    pass
