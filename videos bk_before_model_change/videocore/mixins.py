# mixins.py
from django.shortcuts import render, get_object_or_404

from videocore.models import Category, Video, Post, Channel

class CategoryListMixin(object):

	def get_context_data(self, **kwargs):
	    context = super(CategoryListMixin, self).get_context_data(**kwargs)
	    context['category_list'] = Category.objects.filter(membership=self.request.user)
 	    return context

class VideoListMixin(object):
	
	def get_context_data(self, **kwargs):
	    context = super(VideoListMixin, self).get_context_data(**kwargs)
	    # determine if we are generating list from an activity object context (self.object) or from a course object using view arguments (pk)	 
	    try:# in activity index view
			key = self.object.collection
			context['category'] = self.object.collection
			context['video_list'] = Video.objects.filter(collection=key).order_by("channel__id","display_order")
	    
	    except: # in course detail view
	    	key = self.kwargs['pk']
	    	context['video_list'] = Video.objects.filter(collection=key).order_by("channel__id","display_order")
		
 	    return context

class CreateVideoMixin(object):
	
	def get_context_data(self, **kwargs):
	    context = super(CreateVideoMixin, self).get_context_data(**kwargs)
	    # context['activity_type'] = self.activity_type
	    context['category'] = get_object_or_404(Category, pk=self.kwargs['pk'])
 	    return context	

class PrevNextMixin(object):

	def get_context_data(self, **kwargs):
		context = super(PrevNextMixin, self).get_context_data(**kwargs)
		videoCategory = self.object.collection
		try:
			videoChannel  = self.object.channel
		except:
			pass

		candidates = Video.objects.filter(collection=videoCategory)
		if(videoChannel):
			candidates.filter(channel=videoChannel)
		try:
			context['previous'] = candidates.filter(modified__lt=self.object.modified).order_by('-modified')[0]
		except:
			pass
		try:
			context['next'] = candidates.filter(modified__gt=self.object.modified).order_by('modified')[0]
		except:
			pass
		return context