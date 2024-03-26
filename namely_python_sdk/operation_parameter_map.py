operation_parameter_map = {
    '/events/{id}/comments-POST': {
        'parameters': [
            {
                'name': 'comments'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/events/{event-id}/comments-GET': {
        'parameters': [
            {
                'name': 'event-id'
            },
        ]
    },
    '/events/{event-id}/comments/{comment-id}-DELETE': {
        'parameters': [
            {
                'name': 'event-id'
            },
            {
                'name': 'comment-id'
            },
        ]
    },
    '/companies/info-GET': {
        'parameters': [
        ]
    },
    '/folders/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/folders/{id}/resources-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/folders-GET': {
        'parameters': [
        ]
    },
    '/folders-POST': {
        'parameters': [
            {
                'name': 'folders'
            },
        ]
    },
    '/resources/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/folders/{id}/resources-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/resources-GET': {
        'parameters': [
        ]
    },
    '/folders/{id}-PUT': {
        'parameters': [
            {
                'name': 'folders'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/countries-GET': {
        'parameters': [
        ]
    },
    '/countries/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/events-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'after'
            },
            {
                'name': 'filter[type]'
            },
            {
                'name': 'profile_id'
            },
            {
                'name': 'order'
            },
        ]
    },
    '/events-POST': {
        'parameters': [
            {
                'name': 'events'
            },
        ]
    },
    '/events/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/group_types-GET': {
        'parameters': [
        ]
    },
    '/groups/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/groups-GET': {
        'parameters': [
        ]
    },
    '/teams/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/group_types-GET': {
        'parameters': [
        ]
    },
    '/groups/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/group_types/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/group_types/{id}/groups-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/groups-GET': {
        'parameters': [
        ]
    },
    '/teams-GET': {
        'parameters': [
        ]
    },
    '/events/{id}/comments-POST': {
        'parameters': [
            {
                'name': 'comments'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/likes/event/{id}-POST': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/events/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/likes/event_comment/{comment-id}-DELETE': {
        'parameters': [
            {
                'name': 'comment-id'
            },
        ]
    },
    '/events-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'after'
            },
            {
                'name': 'filter[type]'
            },
            {
                'name': 'profile_id'
            },
            {
                'name': 'order'
            },
        ]
    },
    '/events-POST': {
        'parameters': [
            {
                'name': 'events'
            },
        ]
    },
    '/events/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/likes/event_comment/{comment-id}/recent-GET': {
        'parameters': [
            {
                'name': 'comment-id'
            },
        ]
    },
    '/events/{event-id}/comments-GET': {
        'parameters': [
            {
                'name': 'event-id'
            },
        ]
    },
    '/likes/event/{event-id}/recent-GET': {
        'parameters': [
            {
                'name': 'event-id'
            },
        ]
    },
    '/likes/event_comment/{comment-id}-POST': {
        'parameters': [
            {
                'name': 'comment-id'
            },
        ]
    },
    '/events/{event-id}/comments/{comment-id}-DELETE': {
        'parameters': [
            {
                'name': 'event-id'
            },
            {
                'name': 'comment-id'
            },
        ]
    },
    '/likes/event/{event-id}-DELETE': {
        'parameters': [
            {
                'name': 'message'
            },
            {
                'name': 'event-id'
            },
        ]
    },
    '/job_tiers-POST': {
        'parameters': [
            {
                'name': 'job_tiers'
            },
        ]
    },
    '/job_tiers-GET': {
        'parameters': [
        ]
    },
    '/job_tiers/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/job_tiers/{id}-PUT': {
        'parameters': [
            {
                'name': 'job_tiers'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/job_titles-POST': {
        'parameters': [
            {
                'name': 'job_titles'
            },
        ]
    },
    '/job_titles-GET': {
        'parameters': [
        ]
    },
    '/job_titles/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/job_titles/{id}-PUT': {
        'parameters': [
            {
                'name': 'job_titles'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/job_tiers-POST': {
        'parameters': [
            {
                'name': 'job_tiers'
            },
        ]
    },
    '/job_titles-POST': {
        'parameters': [
            {
                'name': 'job_titles'
            },
        ]
    },
    '/job_tiers-GET': {
        'parameters': [
        ]
    },
    '/job_titles-GET': {
        'parameters': [
        ]
    },
    '/job_tiers/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/job_titles/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/job_titles/{id}-PUT': {
        'parameters': [
            {
                'name': 'job_titles'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/job_tiers/{id}-PUT': {
        'parameters': [
            {
                'name': 'job_tiers'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/likes/event/{event-id}/recent-GET': {
        'parameters': [
            {
                'name': 'event-id'
            },
        ]
    },
    '/countries-GET': {
        'parameters': [
        ]
    },
    '/countries/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/profiles/{id}/notifications-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/notifications-GET': {
        'parameters': [
        ]
    },
    '/profiles/fields-POST': {
        'parameters': [
            {
                'name': 'fields'
            },
        ]
    },
    '/profiles/fields/sections-GET': {
        'parameters': [
        ]
    },
    '/profiles/fields-GET': {
        'parameters': [
        ]
    },
    '/profiles/fields/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/profiles/fields/sections/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/profiles/fields/{id}-PUT': {
        'parameters': [
            {
                'name': 'fields'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/profiles/fields/sections/{id}-PUT': {
        'parameters': [
            {
                'name': 'sections'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/profiles/fields/sections-GET': {
        'parameters': [
        ]
    },
    '/profiles/fields/sections/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/profiles/fields/sections/{id}-PUT': {
        'parameters': [
            {
                'name': 'sections'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/profiles/me-GET': {
        'parameters': [
        ]
    },
    '/profiles/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/profiles-GET': {
        'parameters': [
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'profile_format'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'filter[first_name]'
            },
            {
                'name': 'filter[last_name]'
            },
            {
                'name': 'filter[email]'
            },
            {
                'name': 'filter[personal_email]'
            },
            {
                'name': 'filter[job_title]'
            },
            {
                'name': 'filter[reports_to]'
            },
            {
                'name': 'filter[user_status]'
            },
        ]
    },
    '/profiles-POST': {
        'parameters': [
            {
                'name': 'profiles'
            },
        ]
    },
    '/profiles/{id}-PUT': {
        'parameters': [
            {
                'name': 'profiles'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/reports/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/teams-GET': {
        'parameters': [
        ]
    },
};