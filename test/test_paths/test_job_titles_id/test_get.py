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
from namely_python_sdk.paths.job_titles_id import get
from namely_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestJobTitlesId(ApiTestMixin, unittest.TestCase):
    """
    JobTitlesId unit test stubs
        Get a Job Title
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
