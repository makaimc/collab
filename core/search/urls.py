from django.conf.urls import patterns, url

urlpatterns = patterns('core.search.views',
                       url(r'^$', 'index', name='index'),
                       url(r'^json/$',
                           'search_results_json', name='json_results'),
                       url(r'^tags/json/$',
                           'search_tags_json', name='tags_json'),
                       url(r'^tags/json/(?P<term>[^/]+)/$', 'search_tags_json',
                           name='tags_json'),
                       url(r'^persons/json/$', 'search_persons_json',
                           name='persons_json'),
                       url(r'^all/$', 'search', name='search_all'),
                       url(r'^all/(?P<term>[^/]+)/$',
                           'search', name='search_all'),
                       url(r'^(?P<index>[a-zA-Z0-9/\-_ ]+)/(?P<term>[^/]+)/$',
                           'search', name='search_index'),
                       )
