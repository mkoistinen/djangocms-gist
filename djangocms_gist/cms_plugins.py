# -*- coding: utf-8 -*-

from django.conf import settings
from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .forms import GistPluginAdminForm
from .models import GistPluginModel


class GistPlugin(CMSPluginBase):
    form = GistPluginAdminForm
    model = GistPluginModel
    name = _("Gist")
    render_template = "djangocms_gist/_gist_plugin.html"
    text_enabled = True

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder,
        })
        return context

    def icon_src(self, instance):
        return settings.STATIC_URL + 'djangocms_gist/images/gist_plugin_icon.png'

    def icon_alt(self, instance):
        return 'Gist: %s:%s' % (instance.gist_user, instance.gist_id, )

plugin_pool.register_plugin(GistPlugin)
