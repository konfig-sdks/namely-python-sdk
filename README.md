<div align="center">

[![Visit Namely](./header.png)](https://namely.com)

# Namely<a id="namely"></a>

Move your app forward with the Namely API Move your app forward with the Namely API


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`namely.comments.create_event_comment`](#namelycommentscreate_event_comment)
  * [`namely.comments.get_event_comments`](#namelycommentsget_event_comments)
  * [`namely.comments.remove_event_comment`](#namelycommentsremove_event_comment)
  * [`namely.company_info.get_info`](#namelycompany_infoget_info)
  * [`namely.company_resources.delete_folder_by_id`](#namelycompany_resourcesdelete_folder_by_id)
  * [`namely.company_resources.delete_resource_by_id`](#namelycompany_resourcesdelete_resource_by_id)
  * [`namely.company_resources.folders`](#namelycompany_resourcesfolders)
  * [`namely.company_resources.folders_0`](#namelycompany_resourcesfolders_0)
  * [`namely.company_resources.get_by_id`](#namelycompany_resourcesget_by_id)
  * [`namely.company_resources.get_folder_resources`](#namelycompany_resourcesget_folder_resources)
  * [`namely.company_resources.resources`](#namelycompany_resourcesresources)
  * [`namely.company_resources.update_folder_name`](#namelycompany_resourcesupdate_folder_name)
  * [`namely.countries.countries`](#namelycountriescountries)
  * [`namely.countries.get_country_details`](#namelycountriesget_country_details)
  * [`namely.events.events`](#namelyeventsevents)
  * [`namely.events.events_0`](#namelyeventsevents_0)
  * [`namely.events.get_event`](#namelyeventsget_event)
  * [`namely.groups.get_all_group_types`](#namelygroupsget_all_group_types)
  * [`namely.groups.get_group_details`](#namelygroupsget_group_details)
  * [`namely.groups.groups`](#namelygroupsgroups)
  * [`namely.groups_&amp;_teams.get`](#namelygroups_amp_teamsget)
  * [`namely.groups_&amp;_teams.get_all_group_types`](#namelygroups_amp_teamsget_all_group_types)
  * [`namely.groups_&amp;_teams.get_group_details`](#namelygroups_amp_teamsget_group_details)
  * [`namely.groups_&amp;_teams.get_group_type_details`](#namelygroups_amp_teamsget_group_type_details)
  * [`namely.groups_&amp;_teams.get_group_type_groups`](#namelygroups_amp_teamsget_group_type_groups)
  * [`namely.groups_&amp;_teams.groups`](#namelygroups_amp_teamsgroups)
  * [`namely.groups_&amp;_teams.teams`](#namelygroups_amp_teamsteams)
  * [`namely.home_feed.create_event_comment`](#namelyhome_feedcreate_event_comment)
  * [`namely.home_feed.create_event_like`](#namelyhome_feedcreate_event_like)
  * [`namely.home_feed.delete_announcement`](#namelyhome_feeddelete_announcement)
  * [`namely.home_feed.delete_event_comment_like`](#namelyhome_feeddelete_event_comment_like)
  * [`namely.home_feed.events`](#namelyhome_feedevents)
  * [`namely.home_feed.events_0`](#namelyhome_feedevents_0)
  * [`namely.home_feed.get_event`](#namelyhome_feedget_event)
  * [`namely.home_feed.get_event_comment_likes`](#namelyhome_feedget_event_comment_likes)
  * [`namely.home_feed.get_event_comments`](#namelyhome_feedget_event_comments)
  * [`namely.home_feed.get_event_likes`](#namelyhome_feedget_event_likes)
  * [`namely.home_feed.like_event_comment`](#namelyhome_feedlike_event_comment)
  * [`namely.home_feed.remove_event_comment`](#namelyhome_feedremove_event_comment)
  * [`namely.home_feed.remove_event_like`](#namelyhome_feedremove_event_like)
  * [`namely.job_tier.create_job_tier`](#namelyjob_tiercreate_job_tier)
  * [`namely.job_tier.get_all_job_tiers`](#namelyjob_tierget_all_job_tiers)
  * [`namely.job_tier.get_job_tier`](#namelyjob_tierget_job_tier)
  * [`namely.job_tier.update_label`](#namelyjob_tierupdate_label)
  * [`namely.job_title.create_job_title`](#namelyjob_titlecreate_job_title)
  * [`namely.job_title.get_all_job_titles`](#namelyjob_titleget_all_job_titles)
  * [`namely.job_title.get_job_title_by_id`](#namelyjob_titleget_job_title_by_id)
  * [`namely.job_title.update_job_title`](#namelyjob_titleupdate_job_title)
  * [`namely.jobs_info.create_job_tier`](#namelyjobs_infocreate_job_tier)
  * [`namely.jobs_info.create_job_title`](#namelyjobs_infocreate_job_title)
  * [`namely.jobs_info.get_all_job_tiers`](#namelyjobs_infoget_all_job_tiers)
  * [`namely.jobs_info.get_all_job_titles`](#namelyjobs_infoget_all_job_titles)
  * [`namely.jobs_info.get_job_tier`](#namelyjobs_infoget_job_tier)
  * [`namely.jobs_info.get_job_title_by_id`](#namelyjobs_infoget_job_title_by_id)
  * [`namely.jobs_info.update_job_title`](#namelyjobs_infoupdate_job_title)
  * [`namely.jobs_info.update_label`](#namelyjobs_infoupdate_label)
  * [`namely.likes.get_event_likes`](#namelylikesget_event_likes)
  * [`namely.namely_system_info.countries`](#namelynamely_system_infocountries)
  * [`namely.namely_system_info.get_country_details`](#namelynamely_system_infoget_country_details)
  * [`namely.notifications.get_profile_notifications`](#namelynotificationsget_profile_notifications)
  * [`namely.notifications.notifications`](#namelynotificationsnotifications)
  * [`namely.profile_fields.create_profile_field`](#namelyprofile_fieldscreate_profile_field)
  * [`namely.profile_fields.get_all_field_sections`](#namelyprofile_fieldsget_all_field_sections)
  * [`namely.profile_fields.get_all_fields`](#namelyprofile_fieldsget_all_fields)
  * [`namely.profile_fields.get_field_information`](#namelyprofile_fieldsget_field_information)
  * [`namely.profile_fields.get_field_section`](#namelyprofile_fieldsget_field_section)
  * [`namely.profile_fields.update_field_in_section`](#namelyprofile_fieldsupdate_field_in_section)
  * [`namely.profile_fields.update_field_in_section_0`](#namelyprofile_fieldsupdate_field_in_section_0)
  * [`namely.profile_fields_sections.get_all_field_sections`](#namelyprofile_fields_sectionsget_all_field_sections)
  * [`namely.profile_fields_sections.get_field_section`](#namelyprofile_fields_sectionsget_field_section)
  * [`namely.profile_fields_sections.update_field_in_section`](#namelyprofile_fields_sectionsupdate_field_in_section)
  * [`namely.profiles.get_current_user_profile`](#namelyprofilesget_current_user_profile)
  * [`namely.profiles.get_profile_by_id`](#namelyprofilesget_profile_by_id)
  * [`namely.profiles.profiles`](#namelyprofilesprofiles)
  * [Important Note About the Endpoint](#important-note-about-the-endpoint)
  * [`namely.profiles.profiles_0`](#namelyprofilesprofiles_0)
  * [`namely.profiles.update_profile_with_new_job_title`](#namelyprofilesupdate_profile_with_new_job_title)
  * [`namely.reports.get_report_data`](#namelyreportsget_report_data)
  * [`namely.teams.teams`](#namelyteamsteams)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Namely&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from namely_python_sdk import Namely, ApiException

namely = Namely(

        authorization = 'YOUR_API_KEY',
)

try:
    # Create an Event's Comment
    create_event_comment_response = namely.comments.create_event_comment(
        comments=[
        {
            "content": "content_example",
        }
    ],
        id="id_example",
    )
    print(create_event_comment_response)
except ApiException as e:
    print("Exception when calling CommentsApi.create_event_comment: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from namely_python_sdk import Namely, ApiException

namely = Namely(

        authorization = 'YOUR_API_KEY',
)

async def main():
    try:
        # Create an Event's Comment
        create_event_comment_response = await namely.comments.acreate_event_comment(
            comments=[
        {
            "content": "content_example",
        }
    ],
            id="id_example",
        )
        print(create_event_comment_response)
    except ApiException as e:
        print("Exception when calling CommentsApi.create_event_comment: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from namely_python_sdk import Namely, ApiException

namely = Namely(

        authorization = 'YOUR_API_KEY',
)

try:
    # Create an Event's Comment
    create_event_comment_response = namely.comments.raw.create_event_comment(
        comments=[
        {
            "content": "content_example",
        }
    ],
        id="id_example",
    )
    pprint(create_event_comment_response.body)
    pprint(create_event_comment_response.body["events"])
    pprint(create_event_comment_response.body["meta"])
    pprint(create_event_comment_response.body["links"])
    pprint(create_event_comment_response.body["linked"])
    pprint(create_event_comment_response.headers)
    pprint(create_event_comment_response.status)
    pprint(create_event_comment_response.round_trip_time)
except ApiException as e:
    print("Exception when calling CommentsApi.create_event_comment: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `namely.comments.create_event_comment`<a id="namelycommentscreate_event_comment"></a>

Creates a comment on a particular event.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_event_comment_response = namely.comments.create_event_comment(
    comments=[
        {
            "content": "content_example",
        }
    ],
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### comments: List[`CreateCommentPayload`]<a id="comments-listcreatecommentpayload"></a>

##### id: `str`<a id="id-str"></a>

id of event.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateComment`](./namely_python_sdk/type/create_comment.py)
#### 🔄 Return<a id="🔄-return"></a>

[`HomeFeedCreateEventCommentResponse`](./namely_python_sdk/pydantic/home_feed_create_event_comment_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/events/{id}/comments` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.comments.get_event_comments`<a id="namelycommentsget_event_comments"></a>

Returns all comments associated with a particular event.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_event_comments_response = namely.comments.get_event_comments(
    event_id="event-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### event_id: `str`<a id="event_id-str"></a>

<code>id</code> of the event whose comments you want to view

#### 🔄 Return<a id="🔄-return"></a>

[`HomeFeedGetEventCommentsResponse`](./namely_python_sdk/pydantic/home_feed_get_event_comments_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/events/{event-id}/comments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.comments.remove_event_comment`<a id="namelycommentsremove_event_comment"></a>

Delete a particular comment on an event.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_event_comment_response = namely.comments.remove_event_comment(
    event_id="event-id_example",
    comment_id="comment-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### event_id: `str`<a id="event_id-str"></a>

<code>id</code> of the event to which the comment belongs

##### comment_id: `str`<a id="comment_id-str"></a>

<code>id</code> of the comment you want to delete from the event

#### 🔄 Return<a id="🔄-return"></a>

[`HomeFeedRemoveEventCommentResponse`](./namely_python_sdk/pydantic/home_feed_remove_event_comment_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/events/{event-id}/comments/{comment-id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.company_info.get_info`<a id="namelycompany_infoget_info"></a>

Get company related information. This includes authentication methods, name, permalink, and background image.

Note: Authentication is **not** required for this endpoint because the data (company name, background image, etc.) are required for displaying the public home page of a Namely company.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_info_response = namely.company_info.get_info()
```

#### 🔄 Return<a id="🔄-return"></a>

[`CompanyInfoGetInfoResponse`](./namely_python_sdk/pydantic/company_info_get_info_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/companies/info` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.company_resources.delete_folder_by_id`<a id="namelycompany_resourcesdelete_folder_by_id"></a>

You must pass in the folder id to delete a specific folder.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
namely.company_resources.delete_folder_by_id(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

<code>id</code> of the folder you want to update

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/folders/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.company_resources.delete_resource_by_id`<a id="namelycompany_resourcesdelete_resource_by_id"></a>

This endpoint deletes a specified resource.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
namely.company_resources.delete_resource_by_id(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Use the folder id to pull the resources you want to see.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/folders/{id}/resources` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.company_resources.folders`<a id="namelycompany_resourcesfolders"></a>

This endpoint returns a list of folders and their information.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
folders_response = namely.company_resources.folders()
```

#### 🔄 Return<a id="🔄-return"></a>

[`GetFoldersResponse`](./namely_python_sdk/pydantic/get_folders_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/folders` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.company_resources.folders_0`<a id="namelycompany_resourcesfolders_0"></a>

To create a folder, a title is required. An array of folders will be returned upon success, similar to folders index endpoint.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
folders_0_response = namely.company_resources.folders_0(
    folders=[
        {
            "title": "title_example",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### folders: List[`CreateFolderPayload`]<a id="folders-listcreatefolderpayload"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateFolder`](./namely_python_sdk/type/create_folder.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PostFoldersResponse`](./namely_python_sdk/pydantic/post_folders_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/folders` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.company_resources.get_by_id`<a id="namelycompany_resourcesget_by_id"></a>

Specify the id of the resource to get a complete description. Please see "Download Resource" documentation to actually download a specific resource.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = namely.company_resources.get_by_id(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The resource's id.

#### 🔄 Return<a id="🔄-return"></a>

[`CompanyResourcesGetByIdResponse`](./namely_python_sdk/pydantic/company_resources_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.company_resources.get_folder_resources`<a id="namelycompany_resourcesget_folder_resources"></a>

This method returns an array of resources, whose format and content will be the same as the show resource endpoint.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_folder_resources_response = namely.company_resources.get_folder_resources(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Use the folder id to pull the resources you want to see.

#### 🔄 Return<a id="🔄-return"></a>

[`CompanyResourcesGetFolderResourcesResponse`](./namely_python_sdk/pydantic/company_resources_get_folder_resources_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/folders/{id}/resources` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.company_resources.resources`<a id="namelycompany_resourcesresources"></a>

Get Resources not in a Folder

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
resources_response = namely.company_resources.resources()
```

#### 🔄 Return<a id="🔄-return"></a>

[`GetResourcesResponse`](./namely_python_sdk/pydantic/get_resources_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.company_resources.update_folder_name`<a id="namelycompany_resourcesupdate_folder_name"></a>

Updates the name of a folder.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_folder_name_response = namely.company_resources.update_folder_name(
    folders=[
        {
            "title": "title_example",
        }
    ],
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### folders: List[`UpdateFolderPayload`]<a id="folders-listupdatefolderpayload"></a>

##### id: `str`<a id="id-str"></a>

<code>id</code> of the folder you want to update

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateFolder`](./namely_python_sdk/type/update_folder.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CompanyResourcesUpdateFolderNameResponse`](./namely_python_sdk/pydantic/company_resources_update_folder_name_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/folders/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.countries.countries`<a id="namelycountriescountries"></a>

Returns all valid countries in Namely. A country is universal and may not be modified.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
countries_response = namely.countries.countries()
```

#### 🔄 Return<a id="🔄-return"></a>

[`GetCountriesResponse`](./namely_python_sdk/pydantic/get_countries_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/countries` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.countries.get_country_details`<a id="namelycountriesget_country_details"></a>

Returns one country, as well as a list of a country’s subdivisions (e.g. a list of its states or provinces).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_country_details_response = namely.countries.get_country_details(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

id of the country (an abbreviation of the country's name) you want to view

#### 🔄 Return<a id="🔄-return"></a>

[`NamelySystemInfoGetCountryDetailsResponse`](./namely_python_sdk/pydantic/namely_system_info_get_country_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/countries/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.events.events`<a id="namelyeventsevents"></a>

Returns all events, paginated. Linked to the event is an array of any profiles that commented on the event. Only events associated with the profiles of active employees are eligible to appear.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
events_response = namely.events.events(
    limit=,
    after="string_example",
    filter_type="string_example",
    profile_id="string_example",
    order="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

Limit of records to be retrieved

##### after: `str`<a id="after-str"></a>

<code>id</code> of the first record BEFORE the events you want to retrieve

##### filter_type: `str`<a id="filter_type-str"></a>

The type of event you want to retrieve; examples include `birthday`, `announcement`, `recent_arrival` or `anniversary`

##### profile_id: `str`<a id="profile_id-str"></a>

<code>id</code> of the profile that you wish to pull all associated events from

##### order: `str`<a id="order-str"></a>

This parameter allows you to change how results are ordered. Valid values are `asc` and `desc` - It defaults to `desc`

#### 🔄 Return<a id="🔄-return"></a>

[`GetEventsResponse`](./namely_python_sdk/pydantic/get_events_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/events` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.events.events_0`<a id="namelyeventsevents_0"></a>

Creates an announcement. Other event types are auto-generated and cannot be manually created.

The file parameters allow you to include a file which is located in the announcement. As with uploading a file to a profile, the file must be previously uploaded via the `file create` endpoint.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
events_0_response = namely.events.events_0(
    events=[
        {
            "content": "content_example",
            "is_appreciation": False,
            "email_all": False,
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### events: List[`CreateEventPayload`]<a id="events-listcreateeventpayload"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateEvent`](./namely_python_sdk/type/create_event.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PostEventsResponse`](./namely_python_sdk/pydantic/post_events_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/events` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.events.get_event`<a id="namelyeventsget_event"></a>

Returns information about a single event.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_event_response = namely.events.get_event(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

id of event.

#### 🔄 Return<a id="🔄-return"></a>

[`HomeFeedGetEventResponse`](./namely_python_sdk/pydantic/home_feed_get_event_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/events/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.groups.get_all_group_types`<a id="namelygroupsget_all_group_types"></a>

Returns an array of all group types. Although not present in this endpoint, every group must belong to one and only one group type. Each group type can have zero to many associated groups. Each group type can also have zero to many associated profiles (i.e. people within groups that belong to those group types).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_group_types_response = namely.groups.get_all_group_types()
```

#### 🔄 Return<a id="🔄-return"></a>

[`GroupsTeamsGetAllGroupTypesResponse`](./namely_python_sdk/pydantic/groups_teams_get_all_group_types_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/group_types` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.groups.get_group_details`<a id="namelygroupsget_group_details"></a>

Returns same information about the group as in the #endpoint:Z6r47eQWjcuNA9mq5 endpoint, as well as linked any profiles associated with that group (zero to many).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_group_details_response = namely.groups.get_group_details(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

id of the group you want to view

#### 🔄 Return<a id="🔄-return"></a>

[`GroupsTeamsGetGroupDetailsResponse`](./namely_python_sdk/pydantic/groups_teams_get_group_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/groups/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.groups.groups`<a id="namelygroupsgroups"></a>

Returns an array of all groups. Every group must belong to one and only one group type. Each group type can have zero to many associated groups. Although not present in this endpoint, each group can also have zero to many associated profiles (i.e. people within groups).

Office Locations and Departments are groups.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
groups_response = namely.groups.groups()
```

#### 🔄 Return<a id="🔄-return"></a>

[`GetGroupsResponse`](./namely_python_sdk/pydantic/get_groups_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/groups` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.groups_&amp;_teams.get`<a id="namelygroups_amp_teamsget"></a>

Get a Team

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = namely.groups_&amp;_teams.get(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

<code>id</code> of the team you want to view

#### 🔄 Return<a id="🔄-return"></a>

[`GroupsTeamsGetResponse`](./namely_python_sdk/pydantic/groups_teams_get_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.groups_&amp;_teams.get_all_group_types`<a id="namelygroups_amp_teamsget_all_group_types"></a>

Returns an array of all group types. Although not present in this endpoint, every group must belong to one and only one group type. Each group type can have zero to many associated groups. Each group type can also have zero to many associated profiles (i.e. people within groups that belong to those group types).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_group_types_response = namely.groups_&amp;_teams.get_all_group_types()
```

#### 🔄 Return<a id="🔄-return"></a>

[`GroupsTeamsGetAllGroupTypesResponse`](./namely_python_sdk/pydantic/groups_teams_get_all_group_types_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/group_types` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.groups_&amp;_teams.get_group_details`<a id="namelygroups_amp_teamsget_group_details"></a>

Returns same information about the group as in the #endpoint:Z6r47eQWjcuNA9mq5 endpoint, as well as linked any profiles associated with that group (zero to many).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_group_details_response = namely.groups_&amp;_teams.get_group_details(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

id of the group you want to view

#### 🔄 Return<a id="🔄-return"></a>

[`GroupsTeamsGetGroupDetailsResponse`](./namely_python_sdk/pydantic/groups_teams_get_group_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/groups/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.groups_&amp;_teams.get_group_type_details`<a id="namelygroups_amp_teamsget_group_type_details"></a>

Returns same information about the group as in the #endpoint:27wPhQbAeFhxwiHkp endpoint, as well as linked any profiles associated with that group type (zero to many).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_group_type_details_response = namely.groups_&amp;_teams.get_group_type_details(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

id of the group type you want to view

#### 🔄 Return<a id="🔄-return"></a>

[`GroupsTeamsGetGroupTypeDetailsResponse`](./namely_python_sdk/pydantic/groups_teams_get_group_type_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/group_types/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.groups_&amp;_teams.get_group_type_groups`<a id="namelygroups_amp_teamsget_group_type_groups"></a>

Returns an array of all groups associated with the `id` of the group_type.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_group_type_groups_response = namely.groups_&amp;_teams.get_group_type_groups(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`GroupsTeamsGetGroupTypeGroupsResponse`](./namely_python_sdk/pydantic/groups_teams_get_group_type_groups_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/group_types/{id}/groups` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.groups_&amp;_teams.groups`<a id="namelygroups_amp_teamsgroups"></a>

Returns an array of all groups. Every group must belong to one and only one group type. Each group type can have zero to many associated groups. Although not present in this endpoint, each group can also have zero to many associated profiles (i.e. people within groups).

Office Locations and Departments are groups.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
groups_response = namely.groups_&amp;_teams.groups()
```

#### 🔄 Return<a id="🔄-return"></a>

[`GetGroupsResponse`](./namely_python_sdk/pydantic/get_groups_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/groups` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.groups_&amp;_teams.teams`<a id="namelygroups_amp_teamsteams"></a>

Returns an array of all teams as well as linked, a list of team categories. Every team can belong to zero to many team categories. Each team category can have zero to many associated teams. Although not present in this endpoint, each team can also have zero to many associated profiles (i.e. people within teams).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
teams_response = namely.groups_&amp;_teams.teams()
```

#### 🔄 Return<a id="🔄-return"></a>

[`GetTeamsResponse`](./namely_python_sdk/pydantic/get_teams_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.home_feed.create_event_comment`<a id="namelyhome_feedcreate_event_comment"></a>

Creates a comment on a particular event.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_event_comment_response = namely.home_feed.create_event_comment(
    comments=[
        {
            "content": "content_example",
        }
    ],
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### comments: List[`CreateCommentPayload`]<a id="comments-listcreatecommentpayload"></a>

##### id: `str`<a id="id-str"></a>

id of event.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateComment`](./namely_python_sdk/type/create_comment.py)
#### 🔄 Return<a id="🔄-return"></a>

[`HomeFeedCreateEventCommentResponse`](./namely_python_sdk/pydantic/home_feed_create_event_comment_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/events/{id}/comments` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.home_feed.create_event_like`<a id="namelyhome_feedcreate_event_like"></a>

Like a particular event simply by `POST`ing to the endpoint with its <code>id</code> in the path parameters.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_event_like_response = namely.home_feed.create_event_like(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

<code>id</code> of the event you want to like

#### 🔄 Return<a id="🔄-return"></a>

[`HomeFeedCreateEventLikeResponse`](./namely_python_sdk/pydantic/home_feed_create_event_like_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/likes/event/{id}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.home_feed.delete_announcement`<a id="namelyhome_feeddelete_announcement"></a>

Delete a particular event.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_announcement_response = namely.home_feed.delete_announcement(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

id of event.

#### 🔄 Return<a id="🔄-return"></a>

[`HomeFeedDeleteAnnouncementResponse`](./namely_python_sdk/pydantic/home_feed_delete_announcement_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/events/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.home_feed.delete_event_comment_like`<a id="namelyhome_feeddelete_event_comment_like"></a>

Delete your like from a particular comment. You can only delete your own like (from the profile related to the token).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_event_comment_like_response = namely.home_feed.delete_event_comment_like(
    comment_id="comment-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### comment_id: `str`<a id="comment_id-str"></a>

<code>id</code> of the comment you want to like

#### 🔄 Return<a id="🔄-return"></a>

[`HomeFeedDeleteEventCommentLikeResponse`](./namely_python_sdk/pydantic/home_feed_delete_event_comment_like_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/likes/event_comment/{comment-id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.home_feed.events`<a id="namelyhome_feedevents"></a>

Returns all events, paginated. Linked to the event is an array of any profiles that commented on the event. Only events associated with the profiles of active employees are eligible to appear.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
events_response = namely.home_feed.events(
    limit=,
    after="string_example",
    filter_type="string_example",
    profile_id="string_example",
    order="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

Limit of records to be retrieved

##### after: `str`<a id="after-str"></a>

<code>id</code> of the first record BEFORE the events you want to retrieve

##### filter_type: `str`<a id="filter_type-str"></a>

The type of event you want to retrieve; examples include `birthday`, `announcement`, `recent_arrival` or `anniversary`

##### profile_id: `str`<a id="profile_id-str"></a>

<code>id</code> of the profile that you wish to pull all associated events from

##### order: `str`<a id="order-str"></a>

This parameter allows you to change how results are ordered. Valid values are `asc` and `desc` - It defaults to `desc`

#### 🔄 Return<a id="🔄-return"></a>

[`GetEventsResponse`](./namely_python_sdk/pydantic/get_events_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/events` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.home_feed.events_0`<a id="namelyhome_feedevents_0"></a>

Creates an announcement. Other event types are auto-generated and cannot be manually created.

The file parameters allow you to include a file which is located in the announcement. As with uploading a file to a profile, the file must be previously uploaded via the `file create` endpoint.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
events_0_response = namely.home_feed.events_0(
    events=[
        {
            "content": "content_example",
            "is_appreciation": False,
            "email_all": False,
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### events: List[`CreateEventPayload`]<a id="events-listcreateeventpayload"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateEvent`](./namely_python_sdk/type/create_event.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PostEventsResponse`](./namely_python_sdk/pydantic/post_events_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/events` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.home_feed.get_event`<a id="namelyhome_feedget_event"></a>

Returns information about a single event.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_event_response = namely.home_feed.get_event(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

id of event.

#### 🔄 Return<a id="🔄-return"></a>

[`HomeFeedGetEventResponse`](./namely_python_sdk/pydantic/home_feed_get_event_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/events/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.home_feed.get_event_comment_likes`<a id="namelyhome_feedget_event_comment_likes"></a>

Returns a list of profiles that liked a particular comment on a particular event.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_event_comment_likes_response = namely.home_feed.get_event_comment_likes(
    comment_id="comment-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### comment_id: `str`<a id="comment_id-str"></a>

<code>id</code> of the comment whose likes you want to view

#### 🔄 Return<a id="🔄-return"></a>

[`HomeFeedGetEventCommentLikesResponse`](./namely_python_sdk/pydantic/home_feed_get_event_comment_likes_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/likes/event_comment/{comment-id}/recent` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.home_feed.get_event_comments`<a id="namelyhome_feedget_event_comments"></a>

Returns all comments associated with a particular event.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_event_comments_response = namely.home_feed.get_event_comments(
    event_id="event-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### event_id: `str`<a id="event_id-str"></a>

<code>id</code> of the event whose comments you want to view

#### 🔄 Return<a id="🔄-return"></a>

[`HomeFeedGetEventCommentsResponse`](./namely_python_sdk/pydantic/home_feed_get_event_comments_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/events/{event-id}/comments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.home_feed.get_event_likes`<a id="namelyhome_feedget_event_likes"></a>

Returns a list of profiles that liked a particular event.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_event_likes_response = namely.home_feed.get_event_likes(
    event_id="event-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### event_id: `str`<a id="event_id-str"></a>

<code>id</code> of the event whose likes you want to view

#### 🔄 Return<a id="🔄-return"></a>

[`HomeFeedGetEventLikesResponse`](./namely_python_sdk/pydantic/home_feed_get_event_likes_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/likes/event/{event-id}/recent` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.home_feed.like_event_comment`<a id="namelyhome_feedlike_event_comment"></a>

Like a particular comment simply by `POST`ing to the endpoint with its <code>id</code> in the path parameters.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
like_event_comment_response = namely.home_feed.like_event_comment(
    comment_id="comment-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### comment_id: `str`<a id="comment_id-str"></a>

<code>id</code> of the comment you want to like

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/likes/event_comment/{comment-id}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.home_feed.remove_event_comment`<a id="namelyhome_feedremove_event_comment"></a>

Delete a particular comment on an event.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_event_comment_response = namely.home_feed.remove_event_comment(
    event_id="event-id_example",
    comment_id="comment-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### event_id: `str`<a id="event_id-str"></a>

<code>id</code> of the event to which the comment belongs

##### comment_id: `str`<a id="comment_id-str"></a>

<code>id</code> of the comment you want to delete from the event

#### 🔄 Return<a id="🔄-return"></a>

[`HomeFeedRemoveEventCommentResponse`](./namely_python_sdk/pydantic/home_feed_remove_event_comment_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/events/{event-id}/comments/{comment-id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.home_feed.remove_event_like`<a id="namelyhome_feedremove_event_like"></a>

Delete a particular like from an event.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_event_like_response = namely.home_feed.remove_event_like(
    message=[
        {
            "liked_by_current_profile": True,
            "likes_count": 1,
        }
    ],
    event_id="event-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### message: List[`DeleteLikePayload`]<a id="message-listdeletelikepayload"></a>

##### event_id: `str`<a id="event_id-str"></a>

<code>id</code> of the event from which you want to delete the like

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DeleteLike`](./namely_python_sdk/type/delete_like.py)
#### 🔄 Return<a id="🔄-return"></a>

[`HomeFeedRemoveEventLikeResponse`](./namely_python_sdk/pydantic/home_feed_remove_event_like_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/likes/event/{event-id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.job_tier.create_job_tier`<a id="namelyjob_tiercreate_job_tier"></a>

Creates a job tier.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_job_tier_response = namely.job_tier.create_job_tier(
    job_tiers=[
        {
            "title": "title_example",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### job_tiers: List[`CreateJobTierPayload`]<a id="job_tiers-listcreatejobtierpayload"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateJobTier`](./namely_python_sdk/type/create_job_tier.py)
#### 🔄 Return<a id="🔄-return"></a>

[`JobsInfoCreateJobTierResponse`](./namely_python_sdk/pydantic/jobs_info_create_job_tier_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/job_tiers` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.job_tier.get_all_job_tiers`<a id="namelyjob_tierget_all_job_tiers"></a>

Returns an array of all job tiers. Each job tier can have zero to many linked job titles (while each job title must have one and only one linked job tier).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_job_tiers_response = namely.job_tier.get_all_job_tiers()
```

#### 🔄 Return<a id="🔄-return"></a>

[`JobsInfoGetAllJobTiersResponse`](./namely_python_sdk/pydantic/jobs_info_get_all_job_tiers_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/job_tiers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.job_tier.get_job_tier`<a id="namelyjob_tierget_job_tier"></a>

Returns information about a single job tier.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_job_tier_response = namely.job_tier.get_job_tier(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

<code>id</code> of the job tier you want to view

#### 🔄 Return<a id="🔄-return"></a>

[`JobsInfoGetJobTierResponse`](./namely_python_sdk/pydantic/jobs_info_get_job_tier_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/job_tiers/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.job_tier.update_label`<a id="namelyjob_tierupdate_label"></a>

Updates the label of a job tier.

Use the #endpoint:3iHo6fSyKNs2dsaSC endpoint to get a list of job tiers, whose <code>id</code> is used in the path parameters.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_label_response = namely.job_tier.update_label(
    job_tiers=[
        {
            "title": "title_example",
        }
    ],
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### job_tiers: List[`UpdateJobTierPayload`]<a id="job_tiers-listupdatejobtierpayload"></a>

##### id: `str`<a id="id-str"></a>

<code>id</code> of the job tier you want to view

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateJobTier`](./namely_python_sdk/type/update_job_tier.py)
#### 🔄 Return<a id="🔄-return"></a>

[`JobsInfoUpdateLabelResponse`](./namely_python_sdk/pydantic/jobs_info_update_label_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/job_tiers/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.job_title.create_job_title`<a id="namelyjob_titlecreate_job_title"></a>

Creates a job title.

Use the #endpoint:xfyRRDnWE32d5PNBZ endpoint to get a list of job tiers, whose <code>id</code> is used to populate the value for the <code>parent</code> (job tier) key in the request body.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_job_title_response = namely.job_title.create_job_title(
    job_titles=[
        {
            "title": "title_example",
            "parent": "parent_example",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### job_titles: List[`CreateJobTitlePayload`]<a id="job_titles-listcreatejobtitlepayload"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateJobTitle`](./namely_python_sdk/type/create_job_title.py)
#### 🔄 Return<a id="🔄-return"></a>

[`JobsInfoCreateJobTitleResponse`](./namely_python_sdk/pydantic/jobs_info_create_job_title_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/job_titles` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.job_title.get_all_job_titles`<a id="namelyjob_titleget_all_job_titles"></a>

Returns all job titles. Each job title must have one and only one linked job tier (and each job tier can have zero to many linked job titles).

When using the #endpoint:K6iFb2x6z2yTM9jev endpoint, the API user must either use the <code>title</code> or <code>id</code> of a <code>job_title</code>.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_job_titles_response = namely.job_title.get_all_job_titles()
```

#### 🔄 Return<a id="🔄-return"></a>

[`JobsInfoGetAllJobTitlesResponse`](./namely_python_sdk/pydantic/jobs_info_get_all_job_titles_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/job_titles` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.job_title.get_job_title_by_id`<a id="namelyjob_titleget_job_title_by_id"></a>

Returns information about a single Job Title..

When using the #endpoint:K6iFb2x6z2yTM9jev endpoint, the API user must either use the <code>title</code> or <code>id</code> of a <code>job_title</code>.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_job_title_by_id_response = namely.job_title.get_job_title_by_id(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

id of the job title you want to view

#### 🔄 Return<a id="🔄-return"></a>

[`JobsInfoGetJobTitleByIdResponse`](./namely_python_sdk/pydantic/jobs_info_get_job_title_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/job_titles/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.job_title.update_job_title`<a id="namelyjob_titleupdate_job_title"></a>

Updates the label and/or parent (job tier) of a job title.

Use the #endpoint:xfyRRDnWE32d5PNBZ endpoint to get a list of job tiers, whose <code>id</code> is used to populate the value for the <code>parent</code> (job tier) key in the request body. 

If not updating the <code>parent</code>, use the <code>id</code> of the current <code>parent</code> value; if not updating the <code>title</code>, use the current job title <code>title</code>.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_job_title_response = namely.job_title.update_job_title(
    job_titles=[
        {
            "title": "title_example",
            "parent": "parent_example",
        }
    ],
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### job_titles: List[`UpdateJobTitlePayload`]<a id="job_titles-listupdatejobtitlepayload"></a>

##### id: `str`<a id="id-str"></a>

id of the job title you want to view

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateJobTitle`](./namely_python_sdk/type/update_job_title.py)
#### 🔄 Return<a id="🔄-return"></a>

[`JobsInfoUpdateJobTitleResponse`](./namely_python_sdk/pydantic/jobs_info_update_job_title_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/job_titles/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.jobs_info.create_job_tier`<a id="namelyjobs_infocreate_job_tier"></a>

Creates a job tier.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_job_tier_response = namely.jobs_info.create_job_tier(
    job_tiers=[
        {
            "title": "title_example",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### job_tiers: List[`CreateJobTierPayload`]<a id="job_tiers-listcreatejobtierpayload"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateJobTier`](./namely_python_sdk/type/create_job_tier.py)
#### 🔄 Return<a id="🔄-return"></a>

[`JobsInfoCreateJobTierResponse`](./namely_python_sdk/pydantic/jobs_info_create_job_tier_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/job_tiers` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.jobs_info.create_job_title`<a id="namelyjobs_infocreate_job_title"></a>

Creates a job title.

Use the #endpoint:xfyRRDnWE32d5PNBZ endpoint to get a list of job tiers, whose <code>id</code> is used to populate the value for the <code>parent</code> (job tier) key in the request body.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_job_title_response = namely.jobs_info.create_job_title(
    job_titles=[
        {
            "title": "title_example",
            "parent": "parent_example",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### job_titles: List[`CreateJobTitlePayload`]<a id="job_titles-listcreatejobtitlepayload"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateJobTitle`](./namely_python_sdk/type/create_job_title.py)
#### 🔄 Return<a id="🔄-return"></a>

[`JobsInfoCreateJobTitleResponse`](./namely_python_sdk/pydantic/jobs_info_create_job_title_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/job_titles` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.jobs_info.get_all_job_tiers`<a id="namelyjobs_infoget_all_job_tiers"></a>

Returns an array of all job tiers. Each job tier can have zero to many linked job titles (while each job title must have one and only one linked job tier).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_job_tiers_response = namely.jobs_info.get_all_job_tiers()
```

#### 🔄 Return<a id="🔄-return"></a>

[`JobsInfoGetAllJobTiersResponse`](./namely_python_sdk/pydantic/jobs_info_get_all_job_tiers_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/job_tiers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.jobs_info.get_all_job_titles`<a id="namelyjobs_infoget_all_job_titles"></a>

Returns all job titles. Each job title must have one and only one linked job tier (and each job tier can have zero to many linked job titles).

When using the #endpoint:K6iFb2x6z2yTM9jev endpoint, the API user must either use the <code>title</code> or <code>id</code> of a <code>job_title</code>.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_job_titles_response = namely.jobs_info.get_all_job_titles()
```

#### 🔄 Return<a id="🔄-return"></a>

[`JobsInfoGetAllJobTitlesResponse`](./namely_python_sdk/pydantic/jobs_info_get_all_job_titles_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/job_titles` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.jobs_info.get_job_tier`<a id="namelyjobs_infoget_job_tier"></a>

Returns information about a single job tier.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_job_tier_response = namely.jobs_info.get_job_tier(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

<code>id</code> of the job tier you want to view

#### 🔄 Return<a id="🔄-return"></a>

[`JobsInfoGetJobTierResponse`](./namely_python_sdk/pydantic/jobs_info_get_job_tier_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/job_tiers/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.jobs_info.get_job_title_by_id`<a id="namelyjobs_infoget_job_title_by_id"></a>

Returns information about a single Job Title..

When using the #endpoint:K6iFb2x6z2yTM9jev endpoint, the API user must either use the <code>title</code> or <code>id</code> of a <code>job_title</code>.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_job_title_by_id_response = namely.jobs_info.get_job_title_by_id(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

id of the job title you want to view

#### 🔄 Return<a id="🔄-return"></a>

[`JobsInfoGetJobTitleByIdResponse`](./namely_python_sdk/pydantic/jobs_info_get_job_title_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/job_titles/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.jobs_info.update_job_title`<a id="namelyjobs_infoupdate_job_title"></a>

Updates the label and/or parent (job tier) of a job title.

Use the #endpoint:xfyRRDnWE32d5PNBZ endpoint to get a list of job tiers, whose <code>id</code> is used to populate the value for the <code>parent</code> (job tier) key in the request body. 

If not updating the <code>parent</code>, use the <code>id</code> of the current <code>parent</code> value; if not updating the <code>title</code>, use the current job title <code>title</code>.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_job_title_response = namely.jobs_info.update_job_title(
    job_titles=[
        {
            "title": "title_example",
            "parent": "parent_example",
        }
    ],
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### job_titles: List[`UpdateJobTitlePayload`]<a id="job_titles-listupdatejobtitlepayload"></a>

##### id: `str`<a id="id-str"></a>

id of the job title you want to view

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateJobTitle`](./namely_python_sdk/type/update_job_title.py)
#### 🔄 Return<a id="🔄-return"></a>

[`JobsInfoUpdateJobTitleResponse`](./namely_python_sdk/pydantic/jobs_info_update_job_title_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/job_titles/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.jobs_info.update_label`<a id="namelyjobs_infoupdate_label"></a>

Updates the label of a job tier.

Use the #endpoint:3iHo6fSyKNs2dsaSC endpoint to get a list of job tiers, whose <code>id</code> is used in the path parameters.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_label_response = namely.jobs_info.update_label(
    job_tiers=[
        {
            "title": "title_example",
        }
    ],
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### job_tiers: List[`UpdateJobTierPayload`]<a id="job_tiers-listupdatejobtierpayload"></a>

##### id: `str`<a id="id-str"></a>

<code>id</code> of the job tier you want to view

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateJobTier`](./namely_python_sdk/type/update_job_tier.py)
#### 🔄 Return<a id="🔄-return"></a>

[`JobsInfoUpdateLabelResponse`](./namely_python_sdk/pydantic/jobs_info_update_label_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/job_tiers/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.likes.get_event_likes`<a id="namelylikesget_event_likes"></a>

Returns a list of profiles that liked a particular event.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_event_likes_response = namely.likes.get_event_likes(
    event_id="event-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### event_id: `str`<a id="event_id-str"></a>

<code>id</code> of the event whose likes you want to view

#### 🔄 Return<a id="🔄-return"></a>

[`HomeFeedGetEventLikesResponse`](./namely_python_sdk/pydantic/home_feed_get_event_likes_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/likes/event/{event-id}/recent` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.namely_system_info.countries`<a id="namelynamely_system_infocountries"></a>

Returns all valid countries in Namely. A country is universal and may not be modified.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
countries_response = namely.namely_system_info.countries()
```

#### 🔄 Return<a id="🔄-return"></a>

[`GetCountriesResponse`](./namely_python_sdk/pydantic/get_countries_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/countries` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.namely_system_info.get_country_details`<a id="namelynamely_system_infoget_country_details"></a>

Returns one country, as well as a list of a country’s subdivisions (e.g. a list of its states or provinces).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_country_details_response = namely.namely_system_info.get_country_details(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

id of the country (an abbreviation of the country's name) you want to view

#### 🔄 Return<a id="🔄-return"></a>

[`NamelySystemInfoGetCountryDetailsResponse`](./namely_python_sdk/pydantic/namely_system_info_get_country_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/countries/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.notifications.get_profile_notifications`<a id="namelynotificationsget_profile_notifications"></a>

Returns notifications for a profile in a paginated form. By default, there will be 30 notifications per page. At most, you can request 50 notifications per page.

There are three main types of notifications:
1. Time Off
2. Mentioned/Appreciated
3. Generic (All Other)

<strong>There are also three "200" responses on this page</strong>. However, the actual notification response is a combination of all three responses (assuming the user has received all three types of notifications).

Time Off and Mentioned/Appreciated have distinct "links" associated with the notification object. Certain keys will be present or absent based on the nature of notification (e.g. the "comment_id" key will only be present if you were mentioned in a comment).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_profile_notifications_response = namely.notifications.get_profile_notifications(
    id="id_example",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

id of the profile whose notifications you want to view

##### page: `int`<a id="page-int"></a>

the page of information you'd like to receive.

##### per_page: `int`<a id="per_page-int"></a>

the number of employees to retrieve when using pagination; default is 30 and the limit is 50.

#### 🔄 Return<a id="🔄-return"></a>

[`NotificationsGetProfileNotificationsResponse`](./namely_python_sdk/pydantic/notifications_get_profile_notifications_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/profiles/{id}/notifications` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.notifications.notifications`<a id="namelynotificationsnotifications"></a>

Returns all notifications for the current API user/token bearer.

There are three main types of notifications:
1. Time Off
2. Mentioned/Appreciated
3. Generic (All Other)

<strong>There are also three "200" responses on this page</strong>. However, the actual notification response is a combination of all three responses (assuming the user has received all three types of notifications).

Time Off and Mentioned/Appreciated have distinct "links" associated with the notification object. Certain keys will be present or absent based on the nature of notification (e.g. the "comment_id" key will only be present if you were mentioned in a comment).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
notifications_response = namely.notifications.notifications()
```

#### 🔄 Return<a id="🔄-return"></a>

[`GetNotificationsResponse`](./namely_python_sdk/pydantic/get_notifications_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/notifications` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.profile_fields.create_profile_field`<a id="namelyprofile_fieldscreate_profile_field"></a>

Creates a profile field within a profile field section.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_profile_field_response = namely.profile_fields.create_profile_field(
    fields=[
        {
            "label": "label_example",
            "section": "section_example",
            "type": "type_example",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### fields: List[`CreateProfileFieldPayload`]<a id="fields-listcreateprofilefieldpayload"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateProfileField`](./namely_python_sdk/type/create_profile_field.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ProfileFieldsCreateProfileFieldResponse`](./namely_python_sdk/pydantic/profile_fields_create_profile_field_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/profiles/fields` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.profile_fields.get_all_field_sections`<a id="namelyprofile_fieldsget_all_field_sections"></a>

Returns all profiles field sections as configured at your company. Linked to this endpoint is a list of profile fields, including additional fields not necessarily included in the #endpoint:2PMjgBj4iCTtp4tJe endpoint, as not all are API transferrable.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_field_sections_response = namely.profile_fields.get_all_field_sections()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ProfileFieldsGetAllFieldSectionsResponse`](./namely_python_sdk/pydantic/profile_fields_get_all_field_sections_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/profiles/fields/sections` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.profile_fields.get_all_fields`<a id="namelyprofile_fieldsget_all_fields"></a>

Returns all profiles fields as configured at your company with instructions on valid format for passing through the API. This includes custom fields, but exceptions can be found on the #endpoint:K6iFb2x6z2yTM9jev page.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_fields_response = namely.profile_fields.get_all_fields()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ProfileFieldsGetAllFieldsResponse`](./namely_python_sdk/pydantic/profile_fields_get_all_fields_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/profiles/fields` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.profile_fields.get_field_information`<a id="namelyprofile_fieldsget_field_information"></a>

Returns information about a single Profile Field.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_field_information_response = namely.profile_fields.get_field_information(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

id of the profile field you want to view

#### 🔄 Return<a id="🔄-return"></a>

[`ProfileFieldsGetFieldInformationResponse`](./namely_python_sdk/pydantic/profile_fields_get_field_information_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/profiles/fields/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.profile_fields.get_field_section`<a id="namelyprofile_fieldsget_field_section"></a>

Returns information about a single Profile Field Section.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_field_section_response = namely.profile_fields.get_field_section(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

id of the profile field section you want to view

#### 🔄 Return<a id="🔄-return"></a>

[`ProfileFieldsGetFieldSectionResponse`](./namely_python_sdk/pydantic/profile_fields_get_field_section_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/profiles/fields/sections/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.profile_fields.update_field_in_section`<a id="namelyprofile_fieldsupdate_field_in_section"></a>

Updates a profile field within a profile field section. Supports changing the label and the profile field section in which it sits.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_field_in_section_response = namely.profile_fields.update_field_in_section(
    fields=[
        {
        }
    ],
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### fields: List[`UpdateProfileFieldPayload`]<a id="fields-listupdateprofilefieldpayload"></a>

##### id: `str`<a id="id-str"></a>

id of the profile field you want to view

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateProfileField`](./namely_python_sdk/type/update_profile_field.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ProfileFieldsUpdateFieldInSectionResponse`](./namely_python_sdk/pydantic/profile_fields_update_field_in_section_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/profiles/fields/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.profile_fields.update_field_in_section_0`<a id="namelyprofile_fieldsupdate_field_in_section_0"></a>

Updates the name/label of a profile field section.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_field_in_section_0_response = namely.profile_fields.update_field_in_section_0(
    sections=[
        {
            "title": "title_example",
        }
    ],
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### sections: List[`UpdateSectionPayload`]<a id="sections-listupdatesectionpayload"></a>

##### id: `str`<a id="id-str"></a>

id of the profile field section you want to view

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateSection`](./namely_python_sdk/type/update_section.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ProfileFieldsUpdateFieldInSection200Response`](./namely_python_sdk/pydantic/profile_fields_update_field_in_section200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/profiles/fields/sections/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.profile_fields_sections.get_all_field_sections`<a id="namelyprofile_fields_sectionsget_all_field_sections"></a>

Returns all profiles field sections as configured at your company. Linked to this endpoint is a list of profile fields, including additional fields not necessarily included in the #endpoint:2PMjgBj4iCTtp4tJe endpoint, as not all are API transferrable.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_field_sections_response = namely.profile_fields_sections.get_all_field_sections()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ProfileFieldsGetAllFieldSectionsResponse`](./namely_python_sdk/pydantic/profile_fields_get_all_field_sections_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/profiles/fields/sections` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.profile_fields_sections.get_field_section`<a id="namelyprofile_fields_sectionsget_field_section"></a>

Returns information about a single Profile Field Section.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_field_section_response = namely.profile_fields_sections.get_field_section(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

id of the profile field section you want to view

#### 🔄 Return<a id="🔄-return"></a>

[`ProfileFieldsGetFieldSectionResponse`](./namely_python_sdk/pydantic/profile_fields_get_field_section_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/profiles/fields/sections/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.profile_fields_sections.update_field_in_section`<a id="namelyprofile_fields_sectionsupdate_field_in_section"></a>

Updates the name/label of a profile field section.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_field_in_section_response = namely.profile_fields_sections.update_field_in_section(
    sections=[
        {
            "title": "title_example",
        }
    ],
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### sections: List[`UpdateSectionPayload`]<a id="sections-listupdatesectionpayload"></a>

##### id: `str`<a id="id-str"></a>

id of the profile field section you want to view

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateSection`](./namely_python_sdk/type/update_section.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ProfileFieldsUpdateFieldInSection200Response`](./namely_python_sdk/pydantic/profile_fields_update_field_in_section200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/profiles/fields/sections/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.profiles.get_current_user_profile`<a id="namelyprofilesget_current_user_profile"></a>

Returns same information about the profile as in the #endpoint:E2y2tKYabriCCzTiJ endpoint but isolated, and about the current user only (the profile that owns the access token used to access the API).

Every client-created custom field (the token bearer has permission to see) will appear as key at the bottom of the profile object.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_current_user_profile_response = namely.profiles.get_current_user_profile()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ProfilesGetCurrentUserProfileResponse`](./namely_python_sdk/pydantic/profiles_get_current_user_profile_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/profiles/me` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.profiles.get_profile_by_id`<a id="namelyprofilesget_profile_by_id"></a>

Returns same information about the profile as in the #endpoint:E2y2tKYabriCCzTiJ endpoint but isolated.

Every client-created custom field (the token bearer has permission to see) will appear as key at the bottom of the profile object.

As a note, the following fields will always be returned in the API response, regardless of user permissions:

1. id
2. email
3. first_name
4. last_name
5. user_status
6. updated_at
7. created_at
8. preferred_name
9. full_name
10. job_title


These will NOT be exposed to the user in the UI if their permissions are set correctly.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_profile_by_id_response = namely.profiles.get_profile_by_id(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

id of the profile you want to view

#### 🔄 Return<a id="🔄-return"></a>

[`ProfilesGetProfileByIdResponse`](./namely_python_sdk/pydantic/profiles_get_profile_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/profiles/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.profiles.profiles`<a id="namelyprofilesprofiles"></a>

Returns all active and inactive employee profiles in the same format as the #endpoint:wn3pJ3WtCYWuuBL6r endpoint.

Every client-created custom field (the token bearer has permission to see) will appear as key at the bottom of the profile object.

As a note, the following fields will always be returned in the API response, regardless of user permissions:

1. id
2. email
3. first_name
4. last_name
5. user_status
6. updated_at
7. created_at
8. preferred_name
9. full_name
10. job_title


These will NOT be exposed to the user in the UI if their permissions are set correctly.

### Important Note About the Endpoint<a id="important-note-about-the-endpoint"></a>

Please ensure you're paginating the response of the GET `/profiles` endpoint to ensure optimal performance avoid possible time-outs.

**Examples:**
1. `https://clientname.namely.com/api/v1/profiles.json?page=1&per_page=20&filter[user_status]=active`
2. `https://clientname.namely.com/api/v1/profiles.json?page=2&per_page=20&filter[user_status]=active`
3. `https://clientname.namely.com/api/v1/profiles.json?page=3&per_page=20&filter[user_status]=active`

**Notes:**
1. If you do not specify the `per_page` value, this will default to 30. The max possible is 50.
2. If the response returns with less than the number of profiles requested (or none), the `count` in the `meta` object will be 0, and the `profiles` key will return an empty array.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
profiles_response = namely.profiles.profiles(
    page=1,
    per_page=1,
    profile_format="string_example",
    sort="string_example",
    filter_first_name="string_example",
    filter_last_name="string_example",
    filter_email="string_example",
    filter_personal_email="string_example",
    filter_job_title="string_example",
    filter_reports_to="string_example",
    filter_user_status="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `int`<a id="page-int"></a>

the page of information you'd like to receive.

##### per_page: `int`<a id="per_page-int"></a>

the number of employees to retrieve when using pagination; default is 30 and the limit is 50.

##### profile_format: `str`<a id="profile_format-str"></a>

format of the profile object; only <code>short</code> is supported - returns a truncated version of the profile object

##### sort: `str`<a id="sort-str"></a>

sort order of profiles; valid values - <code>first_name</code>, <code>last_name</code>, <code>created_at</code>, <code>updated_at</code>; prepend with a - (minus) sign to reverse the order

##### filter_first_name: `str`<a id="filter_first_name-str"></a>

returns only profiles with the defined first name

##### filter_last_name: `str`<a id="filter_last_name-str"></a>

returns only profiles with the defined last name

##### filter_email: `str`<a id="filter_email-str"></a>

returns only profiles with the defined (company) email

##### filter_personal_email: `str`<a id="filter_personal_email-str"></a>

returns only profiles with the defined personal email

##### filter_job_title: `str`<a id="filter_job_title-str"></a>

returns only profiles with the defined job title; must be the job_title's <code>title</code>

##### filter_reports_to: `str`<a id="filter_reports_to-str"></a>

<code>id</code> of the profile for whose direct reports you to view; returns only those profiles

##### filter_user_status: `str`<a id="filter_user_status-str"></a>

returns only profiles with the defined <code>user_status</code>; <code>active</code>, <code>pending</code>, and <code>inactive</code> are supported

#### 🔄 Return<a id="🔄-return"></a>

[`GetProfilesResponse`](./namely_python_sdk/pydantic/get_profiles_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/profiles` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.profiles.profiles_0`<a id="namelyprofilesprofiles_0"></a>

**Create a profile as a draft Onboarding session**

1. Ensure that the Onboarding feature has been enabled for your company.
2. In the body of the POST /profiles request, use "pending" as the value of the user_status field along with the other required fields found in the Request Body section below.

*Sample Request:*
```json
{
    "profiles": [
        {
            "first_name": "John",
            "last_name": "Smith",
            "user_status": "pending",
            "start_date": "2019-01-01",
            "personal_email": "personal@email.com",
            "email": "work@email.com"
        }
    ]
}
```

**Create a profile with a job title set**

1. Retrieve the title or id of a  by making a GET request to the /job_titles or /job_titles/{id} endpoint (see the  section).
2. In the body of the POST /profiles request, include the job_title field in addition to the other required fields found in the Request Body section below.
3. The value of the job_title field should be set to an object containing the title (string) or id (guid) of an existing job title. Passing both values is also valid.

*Sample Request:*
```json
{
    "profiles": [
        {
            "first_name": "John",
            "last_name": "Smith",
            "user_status": "active",
            "start_date": "2019-01-01",
            "personal_email": "personal@email.com",
            "email": "work@email.com",
            "job_title": {
            	"id": "a4d5783d-a447-4269-8724-b710d0267aa4"
            }
        }
    ]
}
```

**Create a profile with an address set**

1. Retrieve the country_id of an  by making a GET request to the /countries endpoint (see the  section).
2. The state_id is the 2-letter abbreviation for a state in the United States.
3. In the body of the POST /profiles request, include the home field and set its value equal to an object containing a valid street address as well as the country_id and state_id.
4. Note that every field in the home object (address1, address2, city, state_id, country_id, or zip) is validated against an actual address. If any field in the address object is invalid, a 422 Unprocessable Entity error will be returned.

*Sample Request:*
```json
{
    "profiles": [
        {
            "first_name": "John",
            "last_name": "Smith",
            "user_status": "active",
            "start_date": "2019-01-01",
            "personal_email": "personal@email.com",
            "email": "work@email.com",
            "home": {
                "address1": "195 Broadway",
                "address2": "",
                "city": "New York",
                "state_id": "NY",
                "country_id": "US",
                "zip": "10007"
            }
        }
    ]
}
```

**Create a profile with a salary set**

1. In the body of the POST /profiles request, include the salary field and set its value equal to an object containing a currency_type, a date representing the start date of the salary, and a yearly_amount.
2. "USD" is currently the only valid value for currency_type.

*Sample Request:*
```json
{
    "profiles": [
        {
            "first_name": "John",
            "last_name": "Smith",
            "user_status": "active",
            "start_date": "2019-01-01",
            "personal_email": "personal@email.com",
            "email": "work@email.com",
            "salary": {
                "currency_type": "USD",
                "date": "2019-01-10",
                "yearly_amount": 100000
            }
        }
    ]
}
```

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
profiles_0_response = namely.profiles.profiles_0(
    profiles=[
        {
            "first_name": "first_name_example",
            "last_name": "last_name_example",
            "user_status": "user_status_example",
            "start_date": "start_date_example",
            "email": "email_example",
            "personal_email": "personal_email_example",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### profiles: List[`CreateProfilePayload`]<a id="profiles-listcreateprofilepayload"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateProfile`](./namely_python_sdk/type/create_profile.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PostProfilesResponse`](./namely_python_sdk/pydantic/post_profiles_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/profiles` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.profiles.update_profile_with_new_job_title`<a id="namelyprofilesupdate_profile_with_new_job_title"></a>

Note: the only fields that need to be included in a PUT /profiles/{id} request are the ones that should be updated.

**Update a profile with a new job title**

1. Retrieve the `title` or `id` of a  #model:JcAXAf5CGXH22bS6Z by making a GET request to the /job_titles or /job_titles/{id} endpoint (see the #docTextSection:FwRLDxsBbevBbo8uz section).
2. In the body of the PUT /profiles/{id} request, include the `job_title` field.
3. The value of the `job_title` field should be set to an object containing the `title` (string) or `id` (guid) of an existing job title. Passing both values is also valid.

_Sample Request:_
```json
{
    "profiles": [
        {
            "job_title": {
            	"id": "a4d5783d-a447-4269-8724-b710d0267aa4"
            }
        }
    ]
}
```

**Update a profile with a new address**

1. Retrieve the `country_id` of an #model:yq9tkBR24wuBhzizY by making a GET request to the /countries endpoint (see the #endpoint:ECuAqAqRDoaFMn9ZH section).
2. The `state_id` is the 2-letter abbreviation for a state in the United States.
3. In the body of the PUT /profiles/{id} request, include the `home` field and set its value equal to an object containing a valid street address as well as the `country_id` and `state_id`.
4. Note that every field in the `home` object (`address1`, `address2`, `city`, `state_id`, `country_id`, or `zip`) is validated against an actual address. If any field in the address object is invalid, a 422 Unprocessable Entity error will be returned.

_Sample Request:_
```json
{
    "profiles": [
        {
            "home": {
                "address1": "195 Broadway",
                "address2": "",
                "city": "New York",
                "state_id": "NY",
                "country_id": "US",
                "zip": "10007"
            }
        }
    ]
}
```

**Update a profile with a new salary**

1. In the body of the PUT /profiles/{id} request, include the `salary` field and set its value equal to an object containing a `currency_type`, a `date` representing the start date of the salary, and a `yearly_amount`.
2. "USD" is currently the only valid value for `currency_type`.
3. Note that the `date` is the start date of the new salary. When updating an employee's salary, the `date` value that's passed in must be at least 2 days after the `date` value of the preceding salary. This is because with each new salary, the previous salary is automatically end-dated with a date that must be at least 1 day after the start date of the previous salary. If a passed-in date is invalid, a 422 Unprocessable Entity error will be returned.

_Sample Request:_
```json
{
    "profiles": [
        {
            "salary": {
                "currency_type": "USD",
                "date": "2019-01-10",
                "yearly_amount": 100000
            }
        }
    ]
}
```

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_profile_with_new_job_title_response = namely.profiles.update_profile_with_new_job_title(
    profiles=[
        {
        }
    ],
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### profiles: List[`UpdateProfilePayload`]<a id="profiles-listupdateprofilepayload"></a>

##### id: `str`<a id="id-str"></a>

id of the profile you want to view

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateProfile`](./namely_python_sdk/type/update_profile.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ProfilesUpdateProfileWithNewJobTitleResponse`](./namely_python_sdk/pydantic/profiles_update_profile_with_new_job_title_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/profiles/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.reports.get_report_data`<a id="namelyreportsget_report_data"></a>

This endpoint returns a JSON format version of a report created in Namely. These reports update instantly, so each new call to the API will provide the user with updated information.

After information about the report itself, there is an array of objects that are the columns within the report. The position of the columns is important.

After the columns is what is technically an array of arrays without any keys. Each "sub"-array represents a line in the report and is a list of values whose position on the list within each "sub"-array sequentially corresponds to the column. For example, if the second "column" is "last name", the second "value" in each "sub"-array is the value.

The reports API does not technically have a limit to how many lines can be pulled through the API at once. However, we would suggest limiting it to around 200 lines. A user could likely pull more than that without any problems, but they will eventually run into a timeout. There is no hard limit, however.

Do not have your integration rely on field 'labels' as they are dynamic.  Please use the field 'name' instead.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_report_data_response = namely.reports.get_report_data(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

<code>id</code> of the report from Namely; can be found at the end of the URL of the report on the web

#### 🔄 Return<a id="🔄-return"></a>

[`ReportsGetReportDataResponse`](./namely_python_sdk/pydantic/reports_get_report_data_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/reports/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `namely.teams.teams`<a id="namelyteamsteams"></a>

Returns an array of all teams as well as linked, a list of team categories. Every team can belong to zero to many team categories. Each team category can have zero to many associated teams. Although not present in this endpoint, each team can also have zero to many associated profiles (i.e. people within teams).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
teams_response = namely.teams.teams()
```

#### 🔄 Return<a id="🔄-return"></a>

[`GetTeamsResponse`](./namely_python_sdk/pydantic/get_teams_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
