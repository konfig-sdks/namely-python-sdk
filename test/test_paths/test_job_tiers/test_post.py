# coding: utf-8

"""
    Namely API

    Move your app forward with the Namely API Move your app forward with the Namely API

    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import namely_python_sdk
from namely_python_sdk.paths.job_tiers import post
from namely_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestJobTiers(ApiTestMixin, unittest.TestCase):
    """
    JobTiers unit test stubs
        Create a Job Tier
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 201




if __name__ == '__main__':
    unittest.main()
