from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    nickname = models.CharField(max_length=100)
    membership = models.ManyToManyField(User)

    def get_absolute_url(self):
        return reverse('category', args=[str(self.id)])

    def __unicode__(self):
        return self.title + " (" + self.nickname + ")"

class Channel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    display_order = models.IntegerField(default=0)
    collection = models.ForeignKey(
        Category, blank=True, null=True, on_delete=models.SET_NULL)

    def get_absolute_url(self):
        return reverse('Channel', args=[str(self.id)])

    def __unicode__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True)
    creator = models.ForeignKey(User)
    parent_post = models.ForeignKey('self', blank=True, null=True)
    audio_URL = models.URLField(max_length=200, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('post', args=[str(self.id)])

    def __unicode__(self):
        return self.text


class Video(models.Model):
    title = models.CharField(max_length=100)
    instructions = models.TextField()
    video_upload = models.FileField(
        upload_to='video_uploads', null=True, blank=True)
    collection = models.ForeignKey(
        Category, blank=True, null=True, on_delete=models.SET_NULL)
    channel = models.ForeignKey(
        Channel, blank=True, null=True, on_delete=models.SET_NULL)
    display_order = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField(default=True)
    posts = models.ManyToManyField(Post, null=True, blank=True)

    def get_siblings(self):
        return self.objects.filter(collection=self.collection).order_by("display_order")

    def get_absolute_url(self):
        return reverse('video', args=[str(self.id)])

    def __unicode__(self):
        return self.title

