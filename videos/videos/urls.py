from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from django.conf import settings 
from django.contrib import admin
import allauth
admin.autodiscover()

# from videocore.views import HomeView, CategoryIndexView, CategoryCreateView, ChannelCreateView, ChannelAddView, VideoCreateView, VideoDetailView, savePost
from videocore.views import HomeView, ChannelCreateView, ChannelDetailView, ChannelAddView, VideoDetailView, VideoCreateView, VideoUpdateView, savePost, video_delete, UserCreateView

urlpatterns = patterns('',
    
    url(r'^channel/add/$',        ChannelCreateView.as_view(), name='create_channel'),
    url(r'^channel/add2/$',        ChannelAddView.as_view(), name='add_channel'),
    url(r'^channel/(?P<pk>\d+)$',         ChannelDetailView.as_view(), name='channel'),
    url(r'^video/(?P<pk>\d+)$', 	    VideoDetailView.as_view(), name='video'),
    url(r'^video/add/$',  VideoCreateView.as_view(), name='create_video'),
    url(r'^video/edit/(?P<pk>\d+)$',  VideoUpdateView.as_view(), name='edit_video'),
    url(r'^video/delete/(?P<pk>\d+)$',  video_delete, name='delete_video'),

    url(r'^post/save/$',savePost, name='save_post'),
    
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    # url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    # url(r'^register/$',  UserCreateView.as_view(), name='create_user'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^$', HomeView.as_view(), name='home'),
)+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)#comment this if for production media serving