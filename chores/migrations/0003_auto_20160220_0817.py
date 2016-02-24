# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chores', '0002_chore_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chore',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
