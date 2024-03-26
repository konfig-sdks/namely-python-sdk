# coding: utf-8

# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from namely_python_sdk.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from namely_python_sdk.model.address import Address
from namely_python_sdk.model.column import Column
from namely_python_sdk.model.column_item import ColumnItem
from namely_python_sdk.model.comment import Comment
from namely_python_sdk.model.comment_links import CommentLinks
from namely_python_sdk.model.comment_meta import CommentMeta
from namely_python_sdk.model.company_info_get_info_response import CompanyInfoGetInfoResponse
from namely_python_sdk.model.company_info_get_info_response_authentications import CompanyInfoGetInfoResponseAuthentications
from namely_python_sdk.model.company_info_get_info_response_authentications_item import CompanyInfoGetInfoResponseAuthenticationsItem
from namely_python_sdk.model.company_resources_get_by_id_response import CompanyResourcesGetByIdResponse
from namely_python_sdk.model.company_resources_get_folder_resources_response import CompanyResourcesGetFolderResourcesResponse
from namely_python_sdk.model.company_resources_get_folder_resources_response_meta import CompanyResourcesGetFolderResourcesResponseMeta
from namely_python_sdk.model.company_resources_update_folder_name_response import CompanyResourcesUpdateFolderNameResponse
from namely_python_sdk.model.compensation_benefits import CompensationBenefits
from namely_python_sdk.model.content import Content
from namely_python_sdk.model.content_item import ContentItem
from namely_python_sdk.model.countries import Countries
from namely_python_sdk.model.country import Country
from namely_python_sdk.model.country_links import CountryLinks
from namely_python_sdk.model.country_links_item import CountryLinksItem
from namely_python_sdk.model.create_comment import CreateComment
from namely_python_sdk.model.create_comment_payload import CreateCommentPayload
from namely_python_sdk.model.create_event import CreateEvent
from namely_python_sdk.model.create_event_payload import CreateEventPayload
from namely_python_sdk.model.create_folder import CreateFolder
from namely_python_sdk.model.create_folder_payload import CreateFolderPayload
from namely_python_sdk.model.create_group import CreateGroup
from namely_python_sdk.model.create_group_payload import CreateGroupPayload
from namely_python_sdk.model.create_group_type import CreateGroupType
from namely_python_sdk.model.create_group_type_payload import CreateGroupTypePayload
from namely_python_sdk.model.create_job_tier import CreateJobTier
from namely_python_sdk.model.create_job_tier_payload import CreateJobTierPayload
from namely_python_sdk.model.create_job_title import CreateJobTitle
from namely_python_sdk.model.create_job_title_payload import CreateJobTitlePayload
from namely_python_sdk.model.create_like import CreateLike
from namely_python_sdk.model.create_like_payload import CreateLikePayload
from namely_python_sdk.model.create_profile import CreateProfile
from namely_python_sdk.model.create_profile_field import CreateProfileField
from namely_python_sdk.model.create_profile_field_payload import CreateProfileFieldPayload
from namely_python_sdk.model.create_profile_payload import CreateProfilePayload
from namely_python_sdk.model.create_resource import CreateResource
from namely_python_sdk.model.create_resource_payload import CreateResourcePayload
from namely_python_sdk.model.create_section import CreateSection
from namely_python_sdk.model.create_section_payload import CreateSectionPayload
from namely_python_sdk.model.currency_type import CurrencyType
from namely_python_sdk.model.delete_like import DeleteLike
from namely_python_sdk.model.delete_like_payload import DeleteLikePayload
from namely_python_sdk.model.dental import Dental
from namely_python_sdk.model.event import Event
from namely_python_sdk.model.event_links import EventLinks
from namely_python_sdk.model.event_links_comments import EventLinksComments
from namely_python_sdk.model.events_meta import EventsMeta
from namely_python_sdk.model.field import Field
from namely_python_sdk.model.field_links import FieldLinks
from namely_python_sdk.model.file import File
from namely_python_sdk.model.folder import Folder
from namely_python_sdk.model.generic_notification import GenericNotification
from namely_python_sdk.model.get_countries_response import GetCountriesResponse
from namely_python_sdk.model.get_events_response import GetEventsResponse
from namely_python_sdk.model.get_events_response_linked import GetEventsResponseLinked
from namely_python_sdk.model.get_events_response_links import GetEventsResponseLinks
from namely_python_sdk.model.get_folders_response import GetFoldersResponse
from namely_python_sdk.model.get_groups_response import GetGroupsResponse
from namely_python_sdk.model.get_groups_response_linked import GetGroupsResponseLinked
from namely_python_sdk.model.get_groups_response_links import GetGroupsResponseLinks
from namely_python_sdk.model.get_notifications_response import GetNotificationsResponse
from namely_python_sdk.model.get_notifications_response_linked import GetNotificationsResponseLinked
from namely_python_sdk.model.get_notifications_response_links import GetNotificationsResponseLinks
from namely_python_sdk.model.get_profiles_response import GetProfilesResponse
from namely_python_sdk.model.get_profiles_response_linked import GetProfilesResponseLinked
from namely_python_sdk.model.get_resources_response import GetResourcesResponse
from namely_python_sdk.model.get_resources_response_meta import GetResourcesResponseMeta
from namely_python_sdk.model.get_teams_response import GetTeamsResponse
from namely_python_sdk.model.get_teams_response_linked import GetTeamsResponseLinked
from namely_python_sdk.model.get_teams_response_links import GetTeamsResponseLinks
from namely_python_sdk.model.group import Group
from namely_python_sdk.model.group_link import GroupLink
from namely_python_sdk.model.group_links import GroupLinks
from namely_python_sdk.model.group_singular import GroupSingular
from namely_python_sdk.model.group_singular_links import GroupSingularLinks
from namely_python_sdk.model.group_singular_links_profiles import GroupSingularLinksProfiles
from namely_python_sdk.model.group_type import GroupType
from namely_python_sdk.model.groups_teams_get_all_group_types_response import GroupsTeamsGetAllGroupTypesResponse
from namely_python_sdk.model.groups_teams_get_all_group_types_response_linked import GroupsTeamsGetAllGroupTypesResponseLinked
from namely_python_sdk.model.groups_teams_get_all_group_types_response_links import GroupsTeamsGetAllGroupTypesResponseLinks
from namely_python_sdk.model.groups_teams_get_group_details_response import GroupsTeamsGetGroupDetailsResponse
from namely_python_sdk.model.groups_teams_get_group_details_response_linked import GroupsTeamsGetGroupDetailsResponseLinked
from namely_python_sdk.model.groups_teams_get_group_details_response_links import GroupsTeamsGetGroupDetailsResponseLinks
from namely_python_sdk.model.groups_teams_get_group_type_details_response import GroupsTeamsGetGroupTypeDetailsResponse
from namely_python_sdk.model.groups_teams_get_group_type_details_response_linked import GroupsTeamsGetGroupTypeDetailsResponseLinked
from namely_python_sdk.model.groups_teams_get_group_type_details_response_links import GroupsTeamsGetGroupTypeDetailsResponseLinks
from namely_python_sdk.model.groups_teams_get_group_type_groups_response import GroupsTeamsGetGroupTypeGroupsResponse
from namely_python_sdk.model.groups_teams_get_group_type_groups_response_linked import GroupsTeamsGetGroupTypeGroupsResponseLinked
from namely_python_sdk.model.groups_teams_get_group_type_groups_response_links import GroupsTeamsGetGroupTypeGroupsResponseLinks
from namely_python_sdk.model.groups_teams_get_response import GroupsTeamsGetResponse
from namely_python_sdk.model.groups_teams_get_response_linked import GroupsTeamsGetResponseLinked
from namely_python_sdk.model.groups_teams_get_response_links import GroupsTeamsGetResponseLinks
from namely_python_sdk.model.healthcare import Healthcare
from namely_python_sdk.model.home import Home
from namely_python_sdk.model.home_feed_create_event_comment_response import HomeFeedCreateEventCommentResponse
from namely_python_sdk.model.home_feed_create_event_comment_response_linked import HomeFeedCreateEventCommentResponseLinked
from namely_python_sdk.model.home_feed_create_event_comment_response_links import HomeFeedCreateEventCommentResponseLinks
from namely_python_sdk.model.home_feed_create_event_like_response import HomeFeedCreateEventLikeResponse
from namely_python_sdk.model.home_feed_create_event_like_response_message import HomeFeedCreateEventLikeResponseMessage
from namely_python_sdk.model.home_feed_delete_announcement_response import HomeFeedDeleteAnnouncementResponse
from namely_python_sdk.model.home_feed_delete_event_comment_like_response import HomeFeedDeleteEventCommentLikeResponse
from namely_python_sdk.model.home_feed_get_event_comment_likes_response import HomeFeedGetEventCommentLikesResponse
from namely_python_sdk.model.home_feed_get_event_comments_response import HomeFeedGetEventCommentsResponse
from namely_python_sdk.model.home_feed_get_event_comments_response_linked import HomeFeedGetEventCommentsResponseLinked
from namely_python_sdk.model.home_feed_get_event_comments_response_links import HomeFeedGetEventCommentsResponseLinks
from namely_python_sdk.model.home_feed_get_event_likes_response import HomeFeedGetEventLikesResponse
from namely_python_sdk.model.home_feed_get_event_response import HomeFeedGetEventResponse
from namely_python_sdk.model.home_feed_get_event_response_linked import HomeFeedGetEventResponseLinked
from namely_python_sdk.model.home_feed_get_event_response_links import HomeFeedGetEventResponseLinks
from namely_python_sdk.model.home_feed_remove_event_comment_response import HomeFeedRemoveEventCommentResponse
from namely_python_sdk.model.home_feed_remove_event_like_response import HomeFeedRemoveEventLikeResponse
from namely_python_sdk.model.image import Image
from namely_python_sdk.model.job_tier import JobTier
from namely_python_sdk.model.job_tier_links import JobTierLinks
from namely_python_sdk.model.job_tier_links_job_titles import JobTierLinksJobTitles
from namely_python_sdk.model.job_title import JobTitle
from namely_python_sdk.model.job_title_link import JobTitleLink
from namely_python_sdk.model.job_title_links import JobTitleLinks
from namely_python_sdk.model.jobs_info_create_job_tier_response import JobsInfoCreateJobTierResponse
from namely_python_sdk.model.jobs_info_create_job_tier_response_linked import JobsInfoCreateJobTierResponseLinked
from namely_python_sdk.model.jobs_info_create_job_tier_response_links import JobsInfoCreateJobTierResponseLinks
from namely_python_sdk.model.jobs_info_create_job_title_response import JobsInfoCreateJobTitleResponse
from namely_python_sdk.model.jobs_info_create_job_title_response_linked import JobsInfoCreateJobTitleResponseLinked
from namely_python_sdk.model.jobs_info_create_job_title_response_links import JobsInfoCreateJobTitleResponseLinks
from namely_python_sdk.model.jobs_info_get_all_job_tiers_response import JobsInfoGetAllJobTiersResponse
from namely_python_sdk.model.jobs_info_get_all_job_tiers_response_linked import JobsInfoGetAllJobTiersResponseLinked
from namely_python_sdk.model.jobs_info_get_all_job_tiers_response_links import JobsInfoGetAllJobTiersResponseLinks
from namely_python_sdk.model.jobs_info_get_all_job_titles_response import JobsInfoGetAllJobTitlesResponse
from namely_python_sdk.model.jobs_info_get_all_job_titles_response_linked import JobsInfoGetAllJobTitlesResponseLinked
from namely_python_sdk.model.jobs_info_get_all_job_titles_response_links import JobsInfoGetAllJobTitlesResponseLinks
from namely_python_sdk.model.jobs_info_get_all_job_titles_response_links_job_titles_job_tier import JobsInfoGetAllJobTitlesResponseLinksJobTitlesJobTier
from namely_python_sdk.model.jobs_info_get_job_tier_response import JobsInfoGetJobTierResponse
from namely_python_sdk.model.jobs_info_get_job_tier_response_linked import JobsInfoGetJobTierResponseLinked
from namely_python_sdk.model.jobs_info_get_job_tier_response_links import JobsInfoGetJobTierResponseLinks
from namely_python_sdk.model.jobs_info_get_job_title_by_id_response import JobsInfoGetJobTitleByIdResponse
from namely_python_sdk.model.jobs_info_get_job_title_by_id_response_linked import JobsInfoGetJobTitleByIdResponseLinked
from namely_python_sdk.model.jobs_info_get_job_title_by_id_response_links import JobsInfoGetJobTitleByIdResponseLinks
from namely_python_sdk.model.jobs_info_update_job_title_response import JobsInfoUpdateJobTitleResponse
from namely_python_sdk.model.jobs_info_update_job_title_response_linked import JobsInfoUpdateJobTitleResponseLinked
from namely_python_sdk.model.jobs_info_update_job_title_response_links import JobsInfoUpdateJobTitleResponseLinks
from namely_python_sdk.model.jobs_info_update_label_response import JobsInfoUpdateLabelResponse
from namely_python_sdk.model.jobs_info_update_label_response_linked import JobsInfoUpdateLabelResponseLinked
from namely_python_sdk.model.jobs_info_update_label_response_links import JobsInfoUpdateLabelResponseLinks
from namely_python_sdk.model.like import Like
from namely_python_sdk.model.like_links import LikeLinks
from namely_python_sdk.model.link import Link
from namely_python_sdk.model.linked import Linked
from namely_python_sdk.model.linked_profile import LinkedProfile
from namely_python_sdk.model.linked_profile_image import LinkedProfileImage
from namely_python_sdk.model.mention_notification import MentionNotification
from namely_python_sdk.model.mention_notification_links import MentionNotificationLinks
from namely_python_sdk.model.mention_notification_links_team_ids import MentionNotificationLinksTeamIds
from namely_python_sdk.model.meta import Meta
from namely_python_sdk.model.meta_group import MetaGroup
from namely_python_sdk.model.namely_system_info_get_country_details_response import NamelySystemInfoGetCountryDetailsResponse
from namely_python_sdk.model.notification import Notification
from namely_python_sdk.model.notification_links import NotificationLinks
from namely_python_sdk.model.notifications_get_profile_notifications_response import NotificationsGetProfileNotificationsResponse
from namely_python_sdk.model.notifications_get_profile_notifications_response_linked import NotificationsGetProfileNotificationsResponseLinked
from namely_python_sdk.model.notifications_get_profile_notifications_response_links import NotificationsGetProfileNotificationsResponseLinks
from namely_python_sdk.model.office import Office
from namely_python_sdk.model.pay_group import PayGroup
from namely_python_sdk.model.payroll_company import PayrollCompany
from namely_python_sdk.model.payroll_job import PayrollJob
from namely_python_sdk.model.post_events_response import PostEventsResponse
from namely_python_sdk.model.post_events_response_linked import PostEventsResponseLinked
from namely_python_sdk.model.post_events_response_links import PostEventsResponseLinks
from namely_python_sdk.model.post_folders_response import PostFoldersResponse
from namely_python_sdk.model.post_profiles_response import PostProfilesResponse
from namely_python_sdk.model.post_profiles_response_linked import PostProfilesResponseLinked
from namely_python_sdk.model.profile import Profile
from namely_python_sdk.model.profile_employee_type import ProfileEmployeeType
from namely_python_sdk.model.profile_fields_create_profile_field_response import ProfileFieldsCreateProfileFieldResponse
from namely_python_sdk.model.profile_fields_create_profile_field_response_linked import ProfileFieldsCreateProfileFieldResponseLinked
from namely_python_sdk.model.profile_fields_create_profile_field_response_links import ProfileFieldsCreateProfileFieldResponseLinks
from namely_python_sdk.model.profile_fields_get_all_field_sections_response import ProfileFieldsGetAllFieldSectionsResponse
from namely_python_sdk.model.profile_fields_get_all_field_sections_response_linked import ProfileFieldsGetAllFieldSectionsResponseLinked
from namely_python_sdk.model.profile_fields_get_all_field_sections_response_links import ProfileFieldsGetAllFieldSectionsResponseLinks
from namely_python_sdk.model.profile_fields_get_all_fields_response import ProfileFieldsGetAllFieldsResponse
from namely_python_sdk.model.profile_fields_get_all_fields_response_linked import ProfileFieldsGetAllFieldsResponseLinked
from namely_python_sdk.model.profile_fields_get_all_fields_response_links import ProfileFieldsGetAllFieldsResponseLinks
from namely_python_sdk.model.profile_fields_get_field_information_response import ProfileFieldsGetFieldInformationResponse
from namely_python_sdk.model.profile_fields_get_field_information_response_linked import ProfileFieldsGetFieldInformationResponseLinked
from namely_python_sdk.model.profile_fields_get_field_information_response_links import ProfileFieldsGetFieldInformationResponseLinks
from namely_python_sdk.model.profile_fields_get_field_section_response import ProfileFieldsGetFieldSectionResponse
from namely_python_sdk.model.profile_fields_get_field_section_response_linked import ProfileFieldsGetFieldSectionResponseLinked
from namely_python_sdk.model.profile_fields_get_field_section_response_links import ProfileFieldsGetFieldSectionResponseLinks
from namely_python_sdk.model.profile_fields_update_field_in_section200_response import ProfileFieldsUpdateFieldInSection200Response
from namely_python_sdk.model.profile_fields_update_field_in_section200_response_linked import ProfileFieldsUpdateFieldInSection200ResponseLinked
from namely_python_sdk.model.profile_fields_update_field_in_section200_response_links import ProfileFieldsUpdateFieldInSection200ResponseLinks
from namely_python_sdk.model.profile_fields_update_field_in_section_response import ProfileFieldsUpdateFieldInSectionResponse
from namely_python_sdk.model.profile_fields_update_field_in_section_response_linked import ProfileFieldsUpdateFieldInSectionResponseLinked
from namely_python_sdk.model.profile_fields_update_field_in_section_response_links import ProfileFieldsUpdateFieldInSectionResponseLinks
from namely_python_sdk.model.profile_fields_update_field_in_section_response_meta import ProfileFieldsUpdateFieldInSectionResponseMeta
from namely_python_sdk.model.profile_links import ProfileLinks
from namely_python_sdk.model.profile_meta import ProfileMeta
from namely_python_sdk.model.profile_reports_to import ProfileReportsTo
from namely_python_sdk.model.profile_reports_to_item import ProfileReportsToItem
from namely_python_sdk.model.profiles_get_current_user_profile_response import ProfilesGetCurrentUserProfileResponse
from namely_python_sdk.model.profiles_get_current_user_profile_response_linked import ProfilesGetCurrentUserProfileResponseLinked
from namely_python_sdk.model.profiles_get_profile_by_id_response import ProfilesGetProfileByIdResponse
from namely_python_sdk.model.profiles_get_profile_by_id_response_linked import ProfilesGetProfileByIdResponseLinked
from namely_python_sdk.model.profiles_update_profile_with_new_job_title_response import ProfilesUpdateProfileWithNewJobTitleResponse
from namely_python_sdk.model.profiles_update_profile_with_new_job_title_response_linked import ProfilesUpdateProfileWithNewJobTitleResponseLinked
from namely_python_sdk.model.profiles_update_profile_with_new_job_title_response_links import ProfilesUpdateProfileWithNewJobTitleResponseLinks
from namely_python_sdk.model.profiles_update_profile_with_new_job_title_response_meta import ProfilesUpdateProfileWithNewJobTitleResponseMeta
from namely_python_sdk.model.report import Report
from namely_python_sdk.model.reports_get_report_data_response import ReportsGetReportDataResponse
from namely_python_sdk.model.resource import Resource
from namely_python_sdk.model.salary import Salary
from namely_python_sdk.model.section import Section
from namely_python_sdk.model.section_block_titles import SectionBlockTitles
from namely_python_sdk.model.section_links import SectionLinks
from namely_python_sdk.model.section_links_fields import SectionLinksFields
from namely_python_sdk.model.subdivision import Subdivision
from namely_python_sdk.model.team import Team
from namely_python_sdk.model.team_category import TeamCategory
from namely_python_sdk.model.team_link import TeamLink
from namely_python_sdk.model.team_links import TeamLinks
from namely_python_sdk.model.team_links_team_categories import TeamLinksTeamCategories
from namely_python_sdk.model.thumb import Thumb
from namely_python_sdk.model.update_folder import UpdateFolder
from namely_python_sdk.model.update_folder_payload import UpdateFolderPayload
from namely_python_sdk.model.update_group import UpdateGroup
from namely_python_sdk.model.update_group_payload import UpdateGroupPayload
from namely_python_sdk.model.update_group_type import UpdateGroupType
from namely_python_sdk.model.update_group_type_payload import UpdateGroupTypePayload
from namely_python_sdk.model.update_job_tier import UpdateJobTier
from namely_python_sdk.model.update_job_tier_payload import UpdateJobTierPayload
from namely_python_sdk.model.update_job_title import UpdateJobTitle
from namely_python_sdk.model.update_job_title_payload import UpdateJobTitlePayload
from namely_python_sdk.model.update_profile import UpdateProfile
from namely_python_sdk.model.update_profile_field import UpdateProfileField
from namely_python_sdk.model.update_profile_field_payload import UpdateProfileFieldPayload
from namely_python_sdk.model.update_profile_payload import UpdateProfilePayload
from namely_python_sdk.model.update_resource import UpdateResource
from namely_python_sdk.model.update_resource_payload import UpdateResourcePayload
from namely_python_sdk.model.update_section import UpdateSection
from namely_python_sdk.model.update_section_payload import UpdateSectionPayload
