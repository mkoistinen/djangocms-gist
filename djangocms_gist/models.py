# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin


class GistPluginModel(CMSPlugin):

    gist_user = models.CharField('GitHub user',
        blank=False,
        default='',
        help_text=_('Choose the GitHub user for this Gist.'),
        max_length=32,
    )

    gist_id = models.CharField('Gist ID',
        blank=False,
        default='',
        help_text=_('Enter the Gist ID.'),
        max_length=32,
    )

    filename = models.CharField('filename',
        blank=False,
        default='',
        help_text=_('Optional. Enter the filename, if there are multiple files.'),
        max_length=32,
    )
