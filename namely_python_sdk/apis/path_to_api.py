import typing_extensions

from namely_python_sdk.paths import PathValues
from namely_python_sdk.apis.paths.companies_info import CompaniesInfo
from namely_python_sdk.apis.paths.folders import Folders
from namely_python_sdk.apis.paths.resources_id import ResourcesId
from namely_python_sdk.apis.paths.folders_id_resources import FoldersIdResources
from namely_python_sdk.apis.paths.resources import Resources
from namely_python_sdk.apis.paths.folders_id import FoldersId
from namely_python_sdk.apis.paths.groups import Groups
from namely_python_sdk.apis.paths.groups_id import GroupsId
from namely_python_sdk.apis.paths.group_types import GroupTypes
from namely_python_sdk.apis.paths.group_types_id import GroupTypesId
from namely_python_sdk.apis.paths.group_types_id_groups import GroupTypesIdGroups
from namely_python_sdk.apis.paths.teams import Teams
from namely_python_sdk.apis.paths.teams_id import TeamsId
from namely_python_sdk.apis.paths.events import Events
from namely_python_sdk.apis.paths.events_id import EventsId
from namely_python_sdk.apis.paths.events_event_id_comments import EventsEventIdComments
from namely_python_sdk.apis.paths.likes_event_event_id_recent import LikesEventEventIdRecent
from namely_python_sdk.apis.paths.likes_event_comment_comment_id_recent import LikesEventCommentCommentIdRecent
from namely_python_sdk.apis.paths.events_id_comments import EventsIdComments
from namely_python_sdk.apis.paths.likes_event_id import LikesEventId
from namely_python_sdk.apis.paths.likes_event_comment_comment_id import LikesEventCommentCommentId
from namely_python_sdk.apis.paths.events_event_id_comments_comment_id import EventsEventIdCommentsCommentId
from namely_python_sdk.apis.paths.likes_event_event_id import LikesEventEventId
from namely_python_sdk.apis.paths.job_tiers import JobTiers
from namely_python_sdk.apis.paths.job_tiers_id import JobTiersId
from namely_python_sdk.apis.paths.job_titles import JobTitles
from namely_python_sdk.apis.paths.job_titles_id import JobTitlesId
from namely_python_sdk.apis.paths.countries import Countries
from namely_python_sdk.apis.paths.countries_id import CountriesId
from namely_python_sdk.apis.paths.notifications import Notifications
from namely_python_sdk.apis.paths.profiles_id_notifications import ProfilesIdNotifications
from namely_python_sdk.apis.paths.profiles_fields import ProfilesFields
from namely_python_sdk.apis.paths.profiles_fields_id import ProfilesFieldsId
from namely_python_sdk.apis.paths.profiles_fields_sections import ProfilesFieldsSections
from namely_python_sdk.apis.paths.profiles_fields_sections_id import ProfilesFieldsSectionsId
from namely_python_sdk.apis.paths.profiles import Profiles
from namely_python_sdk.apis.paths.profiles_id import ProfilesId
from namely_python_sdk.apis.paths.profiles_me import ProfilesMe
from namely_python_sdk.apis.paths.reports_id import ReportsId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.COMPANIES_INFO: CompaniesInfo,
        PathValues.FOLDERS: Folders,
        PathValues.RESOURCES_ID: ResourcesId,
        PathValues.FOLDERS_ID_RESOURCES: FoldersIdResources,
        PathValues.RESOURCES: Resources,
        PathValues.FOLDERS_ID: FoldersId,
        PathValues.GROUPS: Groups,
        PathValues.GROUPS_ID: GroupsId,
        PathValues.GROUP_TYPES: GroupTypes,
        PathValues.GROUP_TYPES_ID: GroupTypesId,
        PathValues.GROUP_TYPES_ID_GROUPS: GroupTypesIdGroups,
        PathValues.TEAMS: Teams,
        PathValues.TEAMS_ID: TeamsId,
        PathValues.EVENTS: Events,
        PathValues.EVENTS_ID: EventsId,
        PathValues.EVENTS_EVENTID_COMMENTS: EventsEventIdComments,
        PathValues.LIKES_EVENT_EVENTID_RECENT: LikesEventEventIdRecent,
        PathValues.LIKES_EVENT_COMMENT_COMMENTID_RECENT: LikesEventCommentCommentIdRecent,
        PathValues.EVENTS_ID_COMMENTS: EventsIdComments,
        PathValues.LIKES_EVENT_ID: LikesEventId,
        PathValues.LIKES_EVENT_COMMENT_COMMENTID: LikesEventCommentCommentId,
        PathValues.EVENTS_EVENTID_COMMENTS_COMMENTID: EventsEventIdCommentsCommentId,
        PathValues.LIKES_EVENT_EVENTID: LikesEventEventId,
        PathValues.JOB_TIERS: JobTiers,
        PathValues.JOB_TIERS_ID: JobTiersId,
        PathValues.JOB_TITLES: JobTitles,
        PathValues.JOB_TITLES_ID: JobTitlesId,
        PathValues.COUNTRIES: Countries,
        PathValues.COUNTRIES_ID: CountriesId,
        PathValues.NOTIFICATIONS: Notifications,
        PathValues.PROFILES_ID_NOTIFICATIONS: ProfilesIdNotifications,
        PathValues.PROFILES_FIELDS: ProfilesFields,
        PathValues.PROFILES_FIELDS_ID: ProfilesFieldsId,
        PathValues.PROFILES_FIELDS_SECTIONS: ProfilesFieldsSections,
        PathValues.PROFILES_FIELDS_SECTIONS_ID: ProfilesFieldsSectionsId,
        PathValues.PROFILES: Profiles,
        PathValues.PROFILES_ID: ProfilesId,
        PathValues.PROFILES_ME: ProfilesMe,
        PathValues.REPORTS_ID: ReportsId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.COMPANIES_INFO: CompaniesInfo,
        PathValues.FOLDERS: Folders,
        PathValues.RESOURCES_ID: ResourcesId,
        PathValues.FOLDERS_ID_RESOURCES: FoldersIdResources,
        PathValues.RESOURCES: Resources,
        PathValues.FOLDERS_ID: FoldersId,
        PathValues.GROUPS: Groups,
        PathValues.GROUPS_ID: GroupsId,
        PathValues.GROUP_TYPES: GroupTypes,
        PathValues.GROUP_TYPES_ID: GroupTypesId,
        PathValues.GROUP_TYPES_ID_GROUPS: GroupTypesIdGroups,
        PathValues.TEAMS: Teams,
        PathValues.TEAMS_ID: TeamsId,
        PathValues.EVENTS: Events,
        PathValues.EVENTS_ID: EventsId,
        PathValues.EVENTS_EVENTID_COMMENTS: EventsEventIdComments,
        PathValues.LIKES_EVENT_EVENTID_RECENT: LikesEventEventIdRecent,
        PathValues.LIKES_EVENT_COMMENT_COMMENTID_RECENT: LikesEventCommentCommentIdRecent,
        PathValues.EVENTS_ID_COMMENTS: EventsIdComments,
        PathValues.LIKES_EVENT_ID: LikesEventId,
        PathValues.LIKES_EVENT_COMMENT_COMMENTID: LikesEventCommentCommentId,
        PathValues.EVENTS_EVENTID_COMMENTS_COMMENTID: EventsEventIdCommentsCommentId,
        PathValues.LIKES_EVENT_EVENTID: LikesEventEventId,
        PathValues.JOB_TIERS: JobTiers,
        PathValues.JOB_TIERS_ID: JobTiersId,
        PathValues.JOB_TITLES: JobTitles,
        PathValues.JOB_TITLES_ID: JobTitlesId,
        PathValues.COUNTRIES: Countries,
        PathValues.COUNTRIES_ID: CountriesId,
        PathValues.NOTIFICATIONS: Notifications,
        PathValues.PROFILES_ID_NOTIFICATIONS: ProfilesIdNotifications,
        PathValues.PROFILES_FIELDS: ProfilesFields,
        PathValues.PROFILES_FIELDS_ID: ProfilesFieldsId,
        PathValues.PROFILES_FIELDS_SECTIONS: ProfilesFieldsSections,
        PathValues.PROFILES_FIELDS_SECTIONS_ID: ProfilesFieldsSectionsId,
        PathValues.PROFILES: Profiles,
        PathValues.PROFILES_ID: ProfilesId,
        PathValues.PROFILES_ME: ProfilesMe,
        PathValues.REPORTS_ID: ReportsId,
    }
)
