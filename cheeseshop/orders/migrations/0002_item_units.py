# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='units',
            field=models.CharField(default='oz', max_length=15),
            preserve_default=False,
        ),
    ]
