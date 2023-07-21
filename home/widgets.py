from wagtail.blocks import (
    CharBlock,
    EmailBlock,
    ListBlock,
    RichTextBlock,
    StructBlock,
    URLBlock,
)
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.blocks import ImageChooserBlock


class CalendarWidget(StructBlock):
    class Meta:
        template = "home/widgets/calendar_widget.html"

    pass


class LinksWidget(StructBlock):
    class Meta:
        template = "home/widgets/links_widget.html"

    links = ListBlock(
        StructBlock(
            [
                (
                    "title",
                    CharBlock(
                        required=True,
                    ),
                ),
                (
                    "url",
                    URLBlock(
                        required=True,
                    ),
                ),
            ],
        ),
    )


class BiographyCardWidget(StructBlock):
    class Meta:
        template = "home/widgets/biography_card_widget.html"

    photo = ImageChooserBlock(
        required=True,
    )
    name = CharBlock(
        required=True,
    )
    biography = RichTextBlock(
        required=True,
        max_length=500,
        features=[""],
    )
    contact_email = EmailBlock(
        required=True,
    )


class VideoWidget(StructBlock):
    class Meta:
        template = "home/widgets/video_widget.html"

    title = CharBlock(
        required=True,
        help_text="Video title.",
    )
    video = DocumentChooserBlock()
    poster = ImageChooserBlock(
        required=True,
        help_text="Poster image for the video player.",
    )


class TabWidget(StructBlock):
    class Meta:
        template = "home/widgets/tab_widget.html"

    tabs = ListBlock(
        StructBlock(
            [
                ("title", CharBlock(required=True)),
                (
                    "body",
                    RichTextBlock(
                        features=[
                            "bold",
                            "italic",
                            "link",
                            "ol",
                            "ul",
                            "blockquote",
                        ],
                    ),
                ),
            ],
        ),
    )


class TaskListWidget(StructBlock):
    class Meta:
        template = "home/widgets/task_list_widget.html"

    title = CharBlock(
        required=True,
        help_text="Task list name.",
    )
    tasks = ListBlock(CharBlock(max_length=100))
