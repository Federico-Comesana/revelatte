from django.forms import ModelForm, CharField, ValidationError
from tinymce.widgets import TinyMCE
from .models import RevelationModel
from django.utils import timezone
import datetime


class RevelationModelForm(ModelForm):
    body = CharField(widget=TinyMCE(attrs={'cols': 90, 'rows': 20}))

    def clean_datetime(self):
        timestamp = self.cleaned_data['datetime']
        if timestamp < timezone.now():
            raise ValidationError("The date cannot be in the past!",
                                  code='invalid')
        return timestamp

    def clean(self):
        user = self.instance.user
        if user:
            last = RevelationModel.objects.filter(
                user=user).order_by('created').last()
            if last and timezone.now() <= last.created + datetime.timedelta(
                    minutes=1):
                raise ValidationError("Sorry, 1 post per minute please!",
                                      code='invalid')

    class Meta:
        model = RevelationModel
        exclude = ('user',)
