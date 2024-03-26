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


class RequiredSalary(TypedDict):
    pass

class OptionalSalary(TypedDict, total=False):
    # currency of the profile's <strong>current</strong> salary; <code>null</code> if never provided or no <strong>current</strong> salary; cannot be <code>null</code> if any other salary keys provided
    currency_type: str

    # start date of the profile's <strong>current</strong> salary; <code>null</code> if never provided or no <strong>current</strong> salary; cannot be <code>null</code> if any other salary keys provided
    date: str

    # unique identifier of the profile's <strong>current</strong> salary; <code>null</code> if never provided or no <strong>current</strong> salary; cannot be <code>null</code> if any other salary keys provided
    guid: str

    # unique identifier of the pay group associated with the profile's <strong>current</strong> salary; <code>null</code> if never provided or no <strong>current</strong> salary
    pay_group_id: int

    # unique identifier of the payroll job associated with the profile's <strong>current</strong> salary; <code>null</code> if never provided or no <strong>current</strong> salary
    payroll_job_id: str

    # rate of the profile's <strong>current</strong> salary; valid values include <code>annually</code>, <code>weekly</code>, <code>biweekly</code>, <code>bimonthly</code>, <code>semimonthly</code>, <code>monthly</code>, <code>quarterly</code>, <code>semiannually</code>, and <code>thirteen_monthly</code>; <code>null</code> if never provided; blank if provided then deleted; cannot be <code>null</code> if any other salary keys provided
    rate: str

    # annualized amount (\"amount_raw\" * # of pay periods based on the \"rate\") of the profile's <strong>current</strong> salary; all salaries are annualized; <code>null</code> if never provided; blank if provided then deleted; cannot be <code>null</code> if any other salary keys provided
    yearly_amount: int

    # true if the salary is hourly, and false if yearly; cannot be <code>null</code> if any other salary keys provided. Known as is_hourly elsewhere in the app.
    hourly: bool

    # returns the amount as it was inputted on the UI; if yearly, will be the amount per pay period; if hourly, will be the hourly rate; cannot be <code>null</code> if any other salary keys provided
    amount_raw: str

    # The Payroll Company associated with this salary. Required if multiple Payroll Companies. \"Company name\" defaults to first Payroll Company.
    payroll_company: str

    # Name of the Payroll Job for this Salary. Required if multiple Payroll Companies. Value of \"Job name\" will take first Payroll Job from specified Payroll Company.
    payroll_job: str

class Salary(RequiredSalary, OptionalSalary):
    pass
