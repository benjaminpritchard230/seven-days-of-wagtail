from lib2to3.pytree import Base
from unittest.util import _MAX_LENGTH
from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
# Create your models here.


@register_setting
class SocialMediaSettings(BaseSetting):
    instagram = models.URLField(max_length=100, blank=True)
    panels = [
        FieldPanel("instagram")
    ]
