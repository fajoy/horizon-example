from django.conf.urls.defaults import patterns, url

from .views import IndexView
from .views import DataView
from .views import WorkflowView


urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^data$', DataView.as_view(), name='data'),
    url(r'^create$', WorkflowView.as_view(), name='create'),
)
