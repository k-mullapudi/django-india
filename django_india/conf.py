import django.conf

url_bases = {
    'geonames': {
        'dump': 'http://download.geonames.org/export/dump/',
        'zip': 'http://download.geonames.org/export/zip/',
    },
}

india_country_code = 'IN'

files = {
    'state': {
        'filename': '',
        'urls': [
            url_bases['geonames']['dump'] + '{filename}',
        ],
        'fields': [

        ]
    },
    'district': {
        'filename': '',
        'urls': [
            url_bases['geonames']['dump'] + '{filename}',
        ],
        'fields': [

        ]
    },
    'city': {
        'filename': '',
        'urls': [
            url_bases['geonames']['dump'] + '{filename}',
        ],
        'fields': [

        ]
    }
}

LANGUAGE_DATA = {
    
}


class AppSettings(object):
    """
    A holder for app-specific default settings that allows overriding via
    the project's settings.
    """

    def __getattribute__(self, attr):
        if attr == attr.upper():
            try:
                return getattr(django.conf.settings, attr)
            except AttributeError:
                pass
        return super(AppSettings, self).__getattribute__(attr)
