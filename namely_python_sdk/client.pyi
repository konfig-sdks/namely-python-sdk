# coding: utf-8
"""
    Namely API

    Move your app forward with the Namely API Move your app forward with the Namely API

    Generated by: https://konfigthis.com
"""

import typing
import inspect
from datetime import date, datetime
from namely_python_sdk.client_custom import ClientCustom
from namely_python_sdk.configuration import Configuration
from namely_python_sdk.api_client import ApiClient
from namely_python_sdk.type_util import copy_signature
from namely_python_sdk.apis.tags.comments_api import CommentsApi
from namely_python_sdk.apis.tags.company_info_api import CompanyInfoApi
from namely_python_sdk.apis.tags.company_resources_api import CompanyResourcesApi
from namely_python_sdk.apis.tags.countries_api import CountriesApi
from namely_python_sdk.apis.tags.events_api import EventsApi
from namely_python_sdk.apis.tags.groups_api import GroupsApi
from namely_python_sdk.apis.tags.groups_teams_api import GroupsTeamsApi
from namely_python_sdk.apis.tags.home_feed_api import HomeFeedApi
from namely_python_sdk.apis.tags.job_tier_api import JobTierApi
from namely_python_sdk.apis.tags.job_title_api import JobTitleApi
from namely_python_sdk.apis.tags.jobs_info_api import JobsInfoApi
from namely_python_sdk.apis.tags.likes_api import LikesApi
from namely_python_sdk.apis.tags.namely_system_info_api import NamelySystemInfoApi
from namely_python_sdk.apis.tags.notifications_api import NotificationsApi
from namely_python_sdk.apis.tags.profile_fields_api import ProfileFieldsApi
from namely_python_sdk.apis.tags.profile_fields_sections_api import ProfileFieldsSectionsApi
from namely_python_sdk.apis.tags.profiles_api import ProfilesApi
from namely_python_sdk.apis.tags.reports_api import ReportsApi
from namely_python_sdk.apis.tags.teams_api import TeamsApi



class Namely(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.comments: CommentsApi = CommentsApi(api_client)
        self.company_info: CompanyInfoApi = CompanyInfoApi(api_client)
        self.company_resources: CompanyResourcesApi = CompanyResourcesApi(api_client)
        self.countries: CountriesApi = CountriesApi(api_client)
        self.events: EventsApi = EventsApi(api_client)
        self.groups: GroupsApi = GroupsApi(api_client)
        self.groups_&amp;_teams: GroupsTeamsApi = GroupsTeamsApi(api_client)
        self.home_feed: HomeFeedApi = HomeFeedApi(api_client)
        self.job_tier: JobTierApi = JobTierApi(api_client)
        self.job_title: JobTitleApi = JobTitleApi(api_client)
        self.jobs_info: JobsInfoApi = JobsInfoApi(api_client)
        self.likes: LikesApi = LikesApi(api_client)
        self.namely_system_info: NamelySystemInfoApi = NamelySystemInfoApi(api_client)
        self.notifications: NotificationsApi = NotificationsApi(api_client)
        self.profile_fields: ProfileFieldsApi = ProfileFieldsApi(api_client)
        self.profile_fields_sections: ProfileFieldsSectionsApi = ProfileFieldsSectionsApi(api_client)
        self.profiles: ProfilesApi = ProfilesApi(api_client)
        self.reports: ReportsApi = ReportsApi(api_client)
        self.teams: TeamsApi = TeamsApi(api_client)
