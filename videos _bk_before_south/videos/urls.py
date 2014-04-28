from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.contrib import admin
admin.autodiscover()

from core.views import HomeView, CourseIndexView, CourseCreateView, ActivityCreateIndexView, LessonCreateView, LessonAddView
from discussions.views import DiscussionCreateView, DiscussionDetailView
from essays.views import EssayCreateView, EssayDetailView

urlpatterns = patterns('',
    url(r'^$', 							  'core.views.login_view', name='login'),
    url(r'^home/$', 					    login_required(HomeView.as_view()), name='home'),
    url(r'^course/(?P<pk>\d+)$', 		    CourseIndexView.as_view(), name='course'),
    # url(r'^lesson/(?P<pk>\d+)$',           LessonIndexView.as_view(), name='lesson'),
    url(r'^course/add/$',                   CourseCreateView.as_view(), name='create_collection'),
    url(r'^lesson/add/(?P<addpk>\d+)$',        LessonCreateView.as_view(), name='create_lesson'),
    url(r'^lesson/add2/(?P<addpk>\d+)$',        LessonAddView.as_view(), name='add_lesson'),
    url(r'^activity/add/(?P<pk>\d+)$',      ActivityCreateIndexView.as_view(), name='create_activity'),
    url(r'^discussion/(?P<pk>\d+)$', 	    DiscussionDetailView.as_view(), name='discussion'),
    url(r'^discussion/add/(?P<pk>\d+)$',   DiscussionCreateView.as_view(), name='create_discussion'),
    url(r'^essay/(?P<pk>\d+)$', 		    EssayDetailView.as_view(), name='essay'),
    url(r'^essay/add/(?P<pk>\d+)$',        EssayCreateView.as_view(), name='create_essay'),
    url(r'^overdub/(?P<pk>\d+)$', 		   'overdub_discussions.views.overdub_detail_view', name='overdub'),
    
    url(r'^admin/', include(admin.site.urls)),
)
