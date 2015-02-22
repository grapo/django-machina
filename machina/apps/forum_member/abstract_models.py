# -*- coding: utf-8 -*-

# Standard library imports
from __future__ import unicode_literals

# Third party imports
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

# Local application / specific library imports
from machina.conf import settings as machina_settings
from machina.core.compat import AUTH_USER_MODEL
from machina.models.fields import ExtendedImageField
from machina.models.fields import MarkupTextField


@python_2_unicode_compatible
class AbstractProfile(models.Model):
    """
    Represents the profile associated with each forum user.
    """
    user = models.OneToOneField(AUTH_USER_MODEL, verbose_name=_('User'), related_name='forum_profile')

    # The user's avatar
    avatar = ExtendedImageField(verbose_name=_('Avatar'), null=True, blank=True,
                                upload_to=machina_settings.PROFILE_AVATAR_UPLOAD_TO,
                                **machina_settings.DEFAULT_AVATAR_SETTINGS)

    # The user's signature
    signature = MarkupTextField(verbose_name=_('Signature'), max_length=machina_settings.PROFILE_SIGNATURE_MAX_LENGTH, blank=True, null=True)

    # The amount of posts the user has posted
    posts_count = models.PositiveIntegerField(verbose_name=_('Total posts'), blank=True, default=0)

    class Meta:
        abstract = True
        app_label = 'forum_member'
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')

    def __str__(self):
        return '{}'.format(self.user.username)