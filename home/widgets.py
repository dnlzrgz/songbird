from wagtail.blocks import (
    CharBlock,
    EmailBlock,
    ListBlock,
    RichTextBlock,
    StructBlock,
    URLBlock,
)
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
