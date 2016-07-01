# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin


@python_2_unicode_compatible
class GistUser(models.Model):
    username = models.CharField(
        _('username'), blank=False, default='', max_length=32,
        help_text=_('Choose the GitHub user for this Gist.')
    )

    def __str__(self):
        return self.username


@python_2_unicode_compatible
class GistPluginModel(CMSPlugin):
    gist_user = models.ForeignKey(
        GistUser, default=None,
        help_text=_('Choose the GitHub user for this Gist.')
    )

    gist_id = models.CharField(
        _('Gist ID'), blank=False, default='', max_length=32,
        help_text=_('Enter the Gist ID.')
    )

    filename = models.CharField(
        _('filename'), blank=True, default='', max_length=32,
        help_text=_('Optional. Enter the filename, if there are multiple files and you only want to display one.'),
    )

    def __str__(self):
        return 'Gist: {id} by {name}'.format(id=self.gist_id, name=self.gist_user.username)
