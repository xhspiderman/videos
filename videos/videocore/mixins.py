# mixins.py
from django.shortcuts import render, get_object_or_404

from videocore.models import  Video, Post, Channel#Category,

class ChannelListMixin(object):

	def get_context_data(self, **kwargs):
	    context = super(ChannelListMixin, self).get_context_data(**kwargs)
	    context['channel_list'] = Channel.objects.all().order_by("display_order")
 	    return context

class AllVideoMixin(object):

	def get_context_data(self, **kwargs):
	    context = super(AllVideoMixin, self).get_context_data(**kwargs)
	    context['all_videos'] = Video.objects.all().order_by("display_order", "-modified")
 	    return context

class VideoListMixin(object):
	
	def get_context_data(self, **kwargs):
	    context = super(VideoListMixin, self).get_context_data(**kwargs)
	    # determine if we are generating list from an activity object context (self.object) or from a course object using view arguments (pk)	 
	    keys = self.object.channel.all()
	    context['channel'] = keys
	    context['video_list'] = Video.objects.filter(channel__in=keys).order_by("channel__id","display_order")
	    return context

class PrevNextMixin(object):

	def get_context_data(self, **kwargs):
		context = super(PrevNextMixin, self).get_context_data(**kwargs)
		videoChannels = self.object.channel.all()
		candidates = Video.objects.filter(channel__in=videoChannels)

		try:
			context['previous'] = candidates.filter(modified__lt=self.object.modified).order_by('-modified')[0]
		except:
			pass
		try:
			context['next'] = candidates.filter(modified__gt=self.object.modified).order_by('modified')[0]
		except:
			pass
		return context