from turtle import title
from unicodedata import name
from django.db import models

from wagtail.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class GenericPage(Page):
    banner_title = models.CharField(
        max_length=100, default='Welcome to my generic page')

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("introduction"),
        FieldPanel("banner_image"),
        SnippetChooserPanel("author"),
        StreamFieldPanel("body"),

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
    body = StreamField([
        # ('name', blocks.SomethingBlock()),
        ('heading', blocks.CharBlock(template="heading_block.html")),
        ('image', ImageChooserBlock()),
        ('paragraph', blocks.RichTextBlock())

    ], null=True)


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
