from tinymce.models import HTMLField
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.db.models import (Model, DateTimeField, BooleanField,
                              CharField, ForeignKey, SET_NULL)


class RevelationModel(Model):
    # Fields
    datetime = DateTimeField('Revelation date')
    subject = CharField('Subject (Public)', max_length=100)
    body = HTMLField('Revelation')
    public = BooleanField('Add to public directory', default=True)
    self_destruct = BooleanField('Self destruct on first view', default=False)

    # Internal
    created = DateTimeField(auto_now_add=True, editable=False)
    last_updated = DateTimeField(auto_now=True, editable=False)
    deleted = BooleanField(default=False, editable=False)

    # Relationship Fields
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=SET_NULL, null=True,
                      blank=True)

    def __unicode__(self):
        return u'%s' % self.subject

    def get_absolute_url(self):
        return reverse('revelation-view', args=(self.id,))

    def is_time_visible(self):
        return self.datetime < timezone.now()

    def save(self, *args, **kwargs):
        if self.self_destruct:
            self.public = False
        return super(RevelationModel, self).save(*args, **kwargs)

    class Meta:
        app_label = 'core'
        verbose_name = 'revelation'
        verbose_name_plural = 'revelations'
        ordering = ('-created',)
