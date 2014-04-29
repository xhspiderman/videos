# core/views.py
from django.shortcuts import render, get_object_or_404

from braces.views import LoginRequiredMixin, CsrfExemptMixin

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic import DetailView, CreateView
from django.views.generic.edit import FormView

from videocore.mixins import CategoryListMixin, VideoListMixin, CreateVideoMixin, PrevNextMixin

from .models import Video, Category, Channel

# Simple function-based-view #
def login_view(request):
	return render(request, 'signin.html', {})

# Class Based Views
class HomeView(LoginRequiredMixin, CategoryListMixin,TemplateView):
	template_name = 'home.html'

class CategoryIndexView(CategoryListMixin, VideoListMixin, DetailView):
	model = Category
	context_object_name = 'category'
	template_name = 'category.html'

class CategoryCreateView(CategoryListMixin, CreateView):
	model = Category
	template_name = 'category_create.html'
	fields = ['title','nickname']

	def form_valid(self, form):
		newcourse = form.save(commit = False)
		newcourse.save()
		currentUser=self.request.user
		newcourse.membership.add(currentUser)
		form.save_m2m()
		return super(CategoryCreateView, self).form_valid(form)

# class LessonIndexView(CourseListMixin, LessonActivityListMixin, DetailView):
# 	model = Lesson
# 	context_object_name = 'lesson'
# 	template_name = 'lesson.html'

class ChannelCreateView(CategoryListMixin, CreateView):
	model = Channel
	template_name = 'channel_create.html'
	fields = ['title', 'description']
	
	def form_valid(self, form):
	# Auto set the following fields:
		form.instance.collection = get_object_or_404(Category, pk=self.kwargs['addpk'])
		return super(ChannelCreateView, self).form_valid(form)
	def get_success_url(self):
		return self.object.collection.get_absolute_url()

#Used in the iframe when adding lesson on the fly
class ChannelAddView(ChannelCreateView):
	template_name = 'channel_create_2.html'

	def form_valid(self, form):
	# Auto set the following fields:
		form.instance.collection = get_object_or_404(Category, pk=self.kwargs['addpk'])
		return super(ChannelAddView, self).form_valid(form)
	def get_success_url(self):
		return self.object.collection.get_absolute_url()
	

class VideoDetailView(CategoryListMixin, VideoListMixin, PrevNextMixin, DetailView):
    model = Video
    context_object_name = 'video'
    template_name = 'video.html'


class VideoCreateView(CategoryListMixin, CreateVideoMixin, CreateView):
    model = Video
    template_name = 'video_create.html'
    fields = ['title', 'instructions','video_upload',
              'channel', 'is_active']

    def get_form(self, form_class):
        form = super(VideoCreateView, self).get_form(
            form_class)  # instantiate using parent
        form.fields['channel'].queryset = Channel.objects.filter(
            collection=get_object_or_404(Category, pk=self.kwargs['pk']))
        return form

    def form_valid(self, form):
        # Auto set the following fields:
        form.instance.collection = get_object_or_404(
            Category, pk=self.kwargs['pk'])
        return super(VideoCreateView, self).form_valid(form)