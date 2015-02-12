from django.conf.urls import patterns, include, url
from django.contrib import admin
from celery_poc.views import SubmitTaskView
from celery_poc.views import SubmitFeedView
from celery_poc.views import SubmitWebhookTaskView
from celery_poc.views import SubmitToFanoutQueueView
from celery_poc.views import SubmitToBroadCastQueueView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'celery_poc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^task$', SubmitTaskView.as_view(), name='task'),
    url(r'^task/fanout$', SubmitToFanoutQueueView.as_view(), name='task_fanout'),
    url(r'^task/webhook$', SubmitWebhookTaskView.as_view(), name='task_webhook'),
    url(r'^task/bc$', SubmitToBroadCastQueueView.as_view(), name='task_bc'),
    url(r'^feed$', SubmitFeedView.as_view(), name='feed'),
)
