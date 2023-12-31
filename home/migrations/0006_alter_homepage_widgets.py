# Generated by Django 4.2.3 on 2023-07-16 21:36

import wagtail.blocks
import wagtail.documents.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0005_alter_homepage_widgets"),
    ]

    operations = [
        migrations.AlterField(
            model_name="homepage",
            name="widgets",
            field=wagtail.fields.StreamField(
                [
                    ("calendar_widget", wagtail.blocks.StructBlock([])),
                    (
                        "links_widget",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "links",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                (
                                                    "title",
                                                    wagtail.blocks.CharBlock(
                                                        required=True
                                                    ),
                                                ),
                                                (
                                                    "url",
                                                    wagtail.blocks.URLBlock(
                                                        required=True
                                                    ),
                                                ),
                                            ]
                                        )
                                    ),
                                )
                            ]
                        ),
                    ),
                    (
                        "biography_card_widget",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "photo",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        required=True
                                    ),
                                ),
                                ("name", wagtail.blocks.CharBlock(required=True)),
                                (
                                    "biography",
                                    wagtail.blocks.RichTextBlock(
                                        features=[""], max_length=500, required=True
                                    ),
                                ),
                                (
                                    "contact_email",
                                    wagtail.blocks.EmailBlock(required=True),
                                ),
                            ]
                        ),
                    ),
                    (
                        "video_widget",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.blocks.CharBlock(
                                        help_text="Video title.", required=True
                                    ),
                                ),
                                (
                                    "video",
                                    wagtail.documents.blocks.DocumentChooserBlock(),
                                ),
                                (
                                    "poster",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        help_text="Poster image for the video player.",
                                        required=True,
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "tab_widget",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "tabs",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                (
                                                    "title",
                                                    wagtail.blocks.CharBlock(
                                                        required=True
                                                    ),
                                                ),
                                                (
                                                    "body",
                                                    wagtail.blocks.RichTextBlock(
                                                        features=[
                                                            "bold",
                                                            "italic",
                                                            "link",
                                                            "ol",
                                                            "ul",
                                                            "blockquote",
                                                        ]
                                                    ),
                                                ),
                                            ]
                                        )
                                    ),
                                )
                            ]
                        ),
                    ),
                    (
                        "task_list_widget",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.blocks.CharBlock(
                                        help_text="Task list name.", required=True
                                    ),
                                ),
                                (
                                    "tasks",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.CharBlock(max_length=100)
                                    ),
                                ),
                            ]
                        ),
                    ),
                ],
                null=True,
                use_json_field=True,
            ),
        ),
    ]
