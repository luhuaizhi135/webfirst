from django.conf.urls import url

from . import views

urlpatterns=[
	url(r'^$',views.login,name='login'),
	url(r'^(?P<question_id>[0-9]+)/$',views.detail,name='detail'),
	url(r'^didi$',views.didi,name='didi'),
	url(r'^driver/(?P<driver_id>[0-9]+)$',views.driver,name='driver'),
	url(r'^comment/(?P<comment_id>[0-9]+)$',views.comment,name='comment'),
	url(r'^verify$',views.verify,name='verify'),
	url(r'^login$',views.login,name='login'),
	url(r'^registor$',views.registor,name='registor'),
	url(r'^blog$',views.blog,name='blog'),
]