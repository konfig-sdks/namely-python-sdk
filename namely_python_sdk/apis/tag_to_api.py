import typing_extensions

from namely_python_sdk.apis.tags import TagValues
from namely_python_sdk.apis.tags.home_feed_api import HomeFeedApi
from namely_python_sdk.apis.tags.company_resources_api import CompanyResourcesApi
from namely_python_sdk.apis.tags.jobs_info_api import JobsInfoApi
from namely_python_sdk.apis.tags.groups_teams_api import GroupsTeamsApi
from namely_python_sdk.apis.tags.profile_fields_api import ProfileFieldsApi
from namely_python_sdk.apis.tags.profiles_api import ProfilesApi
from namely_python_sdk.apis.tags.job_tier_api import JobTierApi
from namely_python_sdk.apis.tags.job_title_api import JobTitleApi
from namely_python_sdk.apis.tags.groups_api import GroupsApi
from namely_python_sdk.apis.tags.events_api import EventsApi
from namely_python_sdk.apis.tags.comments_api import CommentsApi
from namely_python_sdk.apis.tags.profile_fields_sections_api import ProfileFieldsSectionsApi
from namely_python_sdk.apis.tags.namely_system_info_api import NamelySystemInfoApi
from namely_python_sdk.apis.tags.countries_api import CountriesApi
from namely_python_sdk.apis.tags.notifications_api import NotificationsApi
from namely_python_sdk.apis.tags.company_info_api import CompanyInfoApi
from namely_python_sdk.apis.tags.teams_api import TeamsApi
from namely_python_sdk.apis.tags.likes_api import LikesApi
from namely_python_sdk.apis.tags.reports_api import ReportsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.HOME_FEED: HomeFeedApi,
        TagValues.COMPANY_RESOURCES: CompanyResourcesApi,
        TagValues.JOBS_INFO: JobsInfoApi,
        TagValues.GROUPS__TEAMS: GroupsTeamsApi,
        TagValues.PROFILE_FIELDS: ProfileFieldsApi,
        TagValues.PROFILES: ProfilesApi,
        TagValues.JOB_TIER: JobTierApi,
        TagValues.JOB_TITLE: JobTitleApi,
        TagValues.GROUPS: GroupsApi,
        TagValues.EVENTS: EventsApi,
        TagValues.COMMENTS: CommentsApi,
        TagValues.PROFILE_FIELDS_SECTIONS: ProfileFieldsSectionsApi,
        TagValues.NAMELY_SYSTEM_INFO: NamelySystemInfoApi,
        TagValues.COUNTRIES: CountriesApi,
        TagValues.NOTIFICATIONS: NotificationsApi,
        TagValues.COMPANY_INFO: CompanyInfoApi,
        TagValues.TEAMS: TeamsApi,
        TagValues.LIKES: LikesApi,
        TagValues.REPORTS: ReportsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.HOME_FEED: HomeFeedApi,
        TagValues.COMPANY_RESOURCES: CompanyResourcesApi,
        TagValues.JOBS_INFO: JobsInfoApi,
        TagValues.GROUPS__TEAMS: GroupsTeamsApi,
        TagValues.PROFILE_FIELDS: ProfileFieldsApi,
        TagValues.PROFILES: ProfilesApi,
        TagValues.JOB_TIER: JobTierApi,
        TagValues.JOB_TITLE: JobTitleApi,
        TagValues.GROUPS: GroupsApi,
        TagValues.EVENTS: EventsApi,
        TagValues.COMMENTS: CommentsApi,
        TagValues.PROFILE_FIELDS_SECTIONS: ProfileFieldsSectionsApi,
        TagValues.NAMELY_SYSTEM_INFO: NamelySystemInfoApi,
        TagValues.COUNTRIES: CountriesApi,
        TagValues.NOTIFICATIONS: NotificationsApi,
        TagValues.COMPANY_INFO: CompanyInfoApi,
        TagValues.TEAMS: TeamsApi,
        TagValues.LIKES: LikesApi,
        TagValues.REPORTS: ReportsApi,
    }
)
