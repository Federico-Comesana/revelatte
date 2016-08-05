from django.contrib import admin
from django import forms
from .models import RevelationModel


class RevelationModelAdminForm(forms.ModelForm):
    class Meta:
        model = RevelationModel
        exclude = ()


class RevelationModelAdmin(admin.ModelAdmin):
    form = RevelationModelAdminForm
    list_display = ['id', 'user', 'subject', 'public', 'datetime',
                    'self_destruct', 'deleted']
    readonly_fields = ['created', 'last_updated', 'deleted']


admin.site.register(RevelationModel, RevelationModelAdmin)
