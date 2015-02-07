from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from name.views import AtomSiteNewsFeed
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'stats/$', 'name.views.stats', name='name_stats'),
    url(r'label/(?P<name_value>.*)$', 'name.views.label', name='name_label'),
    #url(r'admin/', include(admin.site.urls)),
    url(r'feed/$', AtomSiteNewsFeed()),
    url(r'label/(?P<name_value>.*)$', 'name.views.label', name='name_label'),
    url(r'map/$', 'name.views.map', name='name_map'),
    url(r'^$', 'name.views.landing', name='name_landing'),
    url(r'export/$', 'name.views.export', name='name_export'),
    url(r'search/$', 'name.views.search', name='name_search'),
    url(r'search.json$', 'name.views.get_names', name="name_names"),
    url(r'about/$', 'name.views.about', name='name_about'),
    url(r'(?P<name_id>.*).json$', 'name.views.name_json', name='name_json'),
    url(r'opensearch.xml$', 'name.views.opensearch', name='name_opensearch'),
    url(
        r'(?P<name_id>.*).mads.xml$',
        'name.views.mads_serialize',
        name='name_mads_serialize'
    ),
    url(
        r'(?P<name_id>[^/]+)/',
        'name.views.entry_detail',
        name='name_entry_detail'
    ),
)

if settings.DEBUG:

    # static files (images, css, javascript, etc.)
    urlpatterns += patterns(
        '',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT}))