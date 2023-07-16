from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.blocks import StreamBlock
from wagtail.fields import StreamField
from wagtail.models import Page

from .widgets import (
    BiographyCardWidget,
    CalendarWidget,
    LinksWidget,
    TabWidget,
    TaskListWidget,
    VideoWidget,
)


class Widgets(StreamBlock):
    calendar_widget = CalendarWidget()
    links_widget = LinksWidget()
    biography_card_widget = BiographyCardWidget()
    video_widget = VideoWidget()
    tab_widget = TabWidget()
    task_list_widget = TaskListWidget()


class HomePage(Page):
    widgets = StreamField(
        Widgets(),
        null=True,
        use_json_field=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("widgets"),
    ]
