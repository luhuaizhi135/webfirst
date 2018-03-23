from django.conf.urls import url

from . import views

urlpatterns=[
	url(r'^$',views.index,name='index'),
	url(r'^(?P<question_id>[0-9]+)/$',views.detail,name='detail'),
	url(r'^didi$',views.didi,name='didi'),
	url(r'^driver/(?P<driver_id>[0-9]+)$',views.driver,name='driver'),
	url(r'^comment/(?P<comment_id>[0-9]+)$',views.comment,name='comment'),
]