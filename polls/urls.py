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
	url(r'^loginpop$',views.loginpop,name='loginpop'),
	url(r'^loginsucc$',views.loginsucc,name='loginsucc'),
	url(r'^registor$',views.registor,name='registor'),
	url(r'^blog/$',views.blog,name='blog'),
	url(r'^showblog/$',views.showblog,name='showblog'),
	url(r'^publish$',views.publish,name='publish'),
	url(r'^uploadpic$',views.uploadpic,name='uploadpic'),
	url(r'^uploadreport$',views.uploadreport,name='uploadreport'),
	url(r'^publishblog$',views.publishblog,name='publishblog'),
	url(r'^searchblog$',views.searchblog,name='searchblog'),
	url(r'^report/$',views.report,name='report'),
	url(r'^reportdetail/$',views.reportdetail,name='reportdetail'),
	url(r'^genreportmenu/$',views.genreportmenu,name='genreportmenu'),
	#url(r'^report/(?P<dic_1>[0-9]+)/(?P<dic_2>[0-9]+)$',views.report,name='report'),
]