from turtle import title
from unicodedata import name
from django.db import models

from wagtail.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel


class GenericPage(Page):
    banner_title = models.CharField(
        max_length=100, default='Welcome to my generic page')

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("introduction"),
        FieldPanel("banner_image"),
        SnippetChooserPanel("author"),

    ]
    introduction = models.TextField(blank=True)
    banner_image = models.ForeignKey(
        'wagtailimages.Image',
        null='True',
        blank='False',
        on_delete=models.SET_NULL,
        related_name='+',
    )
    author = models.ForeignKey(
        'Author',
        null='True',
        blank='False',
        on_delete=models.SET_NULL,
        related_name='+',
    )


@register_snippet
class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, blank=True)
    company_name = models.CharField(max_length=100, blank=True)
    company_url = models.URLField(blank=True)
    image = models.ForeignKey('wagtailimages.Image',
                              on_delete=models.SET_NULL, null=True, blank=False, related_name='+')

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("introduction"),
        FieldPanel("banner_image"),

    ]

    def __str__(self):
        return self.name
