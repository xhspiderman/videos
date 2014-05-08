from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from django.conf import settings 
from django.contrib import admin
admin.autodiscover()

# from videocore.views import HomeView, CategoryIndexView, CategoryCreateView, ChannelCreateView, ChannelAddView, VideoCreateView, VideoDetailView, savePost
from videocore.views import HomeView, ChannelCreateView, ChannelDetailView, ChannelAddView, VideoDetailView, VideoCreateView, savePost

urlpatterns = patterns('',
    
    url(r'^channel/add/$',        ChannelCreateView.as_view(), name='create_channel'),
    url(r'^channel/add2/$',        ChannelAddView.as_view(), name='add_channel'),
    url(r'^channel/(?P<pk>\d+)$',         ChannelDetailView.as_view(), name='channel'),
    url(r'^video/(?P<pk>\d+)$', 	    VideoDetailView.as_view(), name='video'),
    url(r'^video/add/$',  VideoCreateView.as_view(), name='create_video'),
    url(r'^post/save/$',savePost, name='save_post'),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^$', HomeView.as_view(), name='home'),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
