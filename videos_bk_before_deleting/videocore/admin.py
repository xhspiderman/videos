from django.contrib import admin

from videocore.models import Category
from videocore.models import Post
from videocore.models import Channel
from videocore.models import Video

class CategoryAdmin(admin.ModelAdmin):
	save_as = True

class VideoAdmin(admin.ModelAdmin):
	save_as = True

admin.site.register(Category, CategoryAdmin)
admin.site.register(Channel)
admin.site.register(Post)
admin.site.register(Video, VideoAdmin)
