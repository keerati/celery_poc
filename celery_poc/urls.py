from django.conf.urls import patterns, include, url
from django.contrib import admin
from celery_poc.views import SubmitTaskView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'celery_poc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^task$', SubmitTaskView.as_view(), name='task'),
)
