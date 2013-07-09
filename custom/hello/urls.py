from django.conf.urls.defaults import patterns, url
from .views import IndexView
from .views import MsgView


urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^msg/(?P<msg>.*)$', MsgView.as_view(), name='hello_msg'),
)
