# coding: utf-8

"""
    Namely API

    Move your app forward with the Namely API Move your app forward with the Namely API

    Generated by: https://konfigthis.com
"""

from namely_python_sdk.paths.job_titles.post import CreateJobTitle
from namely_python_sdk.paths.job_titles.get import GetAllJobTitles
from namely_python_sdk.paths.job_titles_id.get import GetJobTitleById
from namely_python_sdk.paths.job_titles_id.put import UpdateJobTitle
from namely_python_sdk.apis.tags.job_title_api_raw import JobTitleApiRaw


class JobTitleApi(
    CreateJobTitle,
    GetAllJobTitles,
    GetJobTitleById,
    UpdateJobTitle,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: JobTitleApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = JobTitleApiRaw(api_client)
