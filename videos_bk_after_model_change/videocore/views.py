# core/views.py
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse

from braces.views import LoginRequiredMixin, CsrfExemptMixin

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic import DetailView, CreateView
from django.views.generic.edit import FormView

# from videocore.mixins import CategoryListMixin, VideoListMixin, CreateVideoMixin, PrevNextMixin
from videocore.mixins import ChannelListMixin, VideoListMixin, PrevNextMixin
from .models import Video,  Channel, Post#,Category

# Class Based Views
class HomeView(LoginRequiredMixin, ChannelListMixin,TemplateView):
	template_name = 'home.html'


class ChannelCreateView(ChannelListMixin, CreateView):
	model = Channel
	template_name = 'channel_create.html'
	fields = ['title', 'description']

	def get_success_url(self):
		return self.object.get_absolute_url()

class ChannelDetailView(ChannelListMixin, DetailView):
    model = Channel
    context_object_name = 'channel'
    template_name = 'channel_detail.html'

#Used in the iframe when adding lesson on the fly
class ChannelAddView(ChannelCreateView):
	template_name = 'channel_create_2.html'

	def get_success_url(self):
		return self.object.get_absolute_url()

class VideoCreateView(ChannelListMixin, CreateView):
    model = Video
    template_name = 'video_create.html'
    fields = ['title', 'description','video_upload',
              'channel', 'is_active']

    # def get_form(self, form_class):
    #     form = super(VideoCreateView, self).get_form(
    #         form_class)  # instantiate using parent
    #     form.fields['channel'].queryset = Channel.objects.filter(
    #         collection=get_object_or_404(Category, pk=self.kwargs['pk']))
    #     return form

    def form_valid(self, form):
        form.instance.creator=self.request.user
        return super(VideoCreateView, self).form_valid(form)

class VideoDetailView(ChannelListMixin,  VideoListMixin, PrevNextMixin, DetailView):  #
    model = Video
    context_object_name = 'video'
    template_name = 'video.html'

# Save Post
def savePost(request):
    # import pdb
    # pdb.set_trace()
    if request.method == 'POST':
        postuser = request.user
        textcontent = request.POST.get("text", '')
        # video to assign post to
        videoID = request.POST.get("videoID", '')
        parentPost = request.POST.get("parentID", '')
        #  validation and save
        if len(textcontent) > 0:
            mess = Post(text=textcontent, creator = request.user)
        if request.POST.get('parentID', '') != '':
            mess.parent_post = Post.objects.get(pk=parentPost)
        if request.POST.get('audio_URL', '') != '':
            mess.audio_URL = request.POST.get('audio', '')
        mess.save()
         #  save mess with that activity
        if videoID:
        	Video.objects.filter(id=videoID)[0].posts.add(mess)
        
    return HttpResponse("Post Success")