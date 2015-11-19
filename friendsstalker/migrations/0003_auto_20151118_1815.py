# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('friendsstalker', '0002_auto_20151118_1730'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='author',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='user',
            field=models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='text',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]
