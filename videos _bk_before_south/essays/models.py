from django.db import models

from core.models import AbstractActivity, Post

class EssayActivity(AbstractActivity):
    required_revisions = models.IntegerField()