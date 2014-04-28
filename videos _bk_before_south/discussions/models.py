from django.db import models

from core.models import AbstractActivity

class DiscussionActivity(AbstractActivity):
    read_after_post = models.BooleanField()
    

    