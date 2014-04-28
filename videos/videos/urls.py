from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from django.conf import settings 
from django.contrib import admin
admin.autodiscover()

from videocore.views import HomeView, CategoryIndexView, CategoryCreateView, ChannelCreateView, ChannelAddView, VideoCreateView, VideoDetailView

urlpatterns = patterns('',
    url(r'^$', 							  'videocore.views.login_view', name='login'),
    url(r'^home/$', 					    login_required(HomeView.as_view()), name='home'),
    url(r'^category/(?P<pk>\d+)$', 		    CategoryIndexView.as_view(), name='category'),
    # url(r'^lesson/(?P<pk>\d+)$',           LessonIndexView.as_view(), name='lesson'),
    url(r'^category/add/$',                   CategoryCreateView.as_view(), name='create_category'),
    url(r'^channel/add/(?P<addpk>\d+)$',        ChannelCreateView.as_view(), name='create_channel'),
    url(r'^channel/add2/(?P<addpk>\d+)$',        ChannelAddView.as_view(), name='add_channel'),
    # url(r'^video/add/(?P<pk>\d+)$',     VideoCreateIndexView.as_view(), name='create_activity'),
    url(r'^video/(?P<pk>\d+)$', 	    VideoDetailView.as_view(), name='video'),
    url(r'^video/add/(?P<pk>\d+)$',  VideoCreateView.as_view(), name='create_video'),
    
    url(r'^admin/', include(admin.site.urls)),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
