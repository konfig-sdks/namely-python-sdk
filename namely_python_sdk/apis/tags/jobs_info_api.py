# coding: utf-8

"""
    Namely API

    Move your app forward with the Namely API Move your app forward with the Namely API

    Generated by: https://konfigthis.com
"""

from namely_python_sdk.paths.job_tiers.post import CreateJobTier
from namely_python_sdk.paths.job_titles.post import CreateJobTitle
from namely_python_sdk.paths.job_tiers.get import GetAllJobTiers
from namely_python_sdk.paths.job_titles.get import GetAllJobTitles
from namely_python_sdk.paths.job_tiers_id.get import GetJobTier
from namely_python_sdk.paths.job_titles_id.get import GetJobTitleById
from namely_python_sdk.paths.job_titles_id.put import UpdateJobTitle
from namely_python_sdk.paths.job_tiers_id.put import UpdateLabel
from namely_python_sdk.apis.tags.jobs_info_api_raw import JobsInfoApiRaw


class JobsInfoApi(
    CreateJobTier,
    CreateJobTitle,
    GetAllJobTiers,
    GetAllJobTitles,
    GetJobTier,
    GetJobTitleById,
    UpdateJobTitle,
    UpdateLabel,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: JobsInfoApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = JobsInfoApiRaw(api_client)
