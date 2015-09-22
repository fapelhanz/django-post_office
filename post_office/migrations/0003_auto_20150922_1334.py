# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import post_office.validators


class Migration(migrations.Migration):

    dependencies = [
        ('post_office', '0002_add_i18n_and_backend_alias'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailtemplate',
            name='content_en',
            field=models.TextField(blank=True, null=True, verbose_name='Content', validators=[post_office.validators.validate_template_syntax]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='emailtemplate',
            name='content_es',
            field=models.TextField(blank=True, null=True, verbose_name='Content', validators=[post_office.validators.validate_template_syntax]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='emailtemplate',
            name='html_content_en',
            field=models.TextField(blank=True, null=True, verbose_name='HTML content', validators=[post_office.validators.validate_template_syntax]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='emailtemplate',
            name='html_content_es',
            field=models.TextField(blank=True, null=True, verbose_name='HTML content', validators=[post_office.validators.validate_template_syntax]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='emailtemplate',
            name='subject_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Subject', validators=[post_office.validators.validate_template_syntax]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='emailtemplate',
            name='subject_es',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Subject', validators=[post_office.validators.validate_template_syntax]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='emailtemplate',
            name='language',
            field=models.CharField(default='', help_text='Render template in alternative language', max_length=12, blank=True, choices=[(b'en', 'English'), (b'es', 'Spanish')]),
            preserve_default=True,
        ),
    ]
