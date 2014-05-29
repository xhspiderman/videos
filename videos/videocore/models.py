from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Channel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    display_order = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('channel', args=[str(self.id)])

    def get_channel_videos(self):
        return Video.objects.filter(channel__id__contains=self.id)

    def __unicode__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True)
    creator = models.ForeignKey(User, blank=True, null=True)
    parent_post = models.ForeignKey('self', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('post', args=[str(self.id)])

    def __unicode__(self):
        return self.text


class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_upload = models.FileField(
        upload_to='video_uploads', null=True, blank=True)
    channel = models.ManyToManyField(
        Channel, blank=True, null=True)
    display_order = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    posts = models.ForeignKey(Post, null=True, blank=True)
    creator = models.ForeignKey(User, blank=True, null=True)

    def get_siblings(self):
        return self.objects.filter(channel=self.channel).order_by("display_order")

    def get_channels(self):
        return self.channel.all().order_by("id","display_order")

    def get_absolute_url(self):
        return reverse('video', args=[str(self.id)])

    def __unicode__(self):
        return self.title

