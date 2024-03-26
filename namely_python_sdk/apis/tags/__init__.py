# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from namely_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    HOME_FEED = "Home Feed"
    COMPANY_RESOURCES = "Company Resources"
    JOBS_INFO = "Jobs Info"
    GROUPS__TEAMS = "Groups &amp; Teams"
    PROFILE_FIELDS = "Profile Fields"
    PROFILES = "Profiles"
    JOB_TIER = "Job Tier"
    JOB_TITLE = "Job Title"
    GROUPS = "Groups"
    EVENTS = "Events"
    COMMENTS = "Comments"
    PROFILE_FIELDS_SECTIONS = "Profile Fields Sections"
    NAMELY_SYSTEM_INFO = "Namely System Info"
    COUNTRIES = "Countries"
    NOTIFICATIONS = "Notifications"
    COMPANY_INFO = "Company Info"
    TEAMS = "Teams"
    LIKES = "Likes"
    REPORTS = "Reports"
