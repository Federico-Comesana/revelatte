from django.views.generic import (DetailView, ListView, CreateView,
                                  TemplateView, View, DeleteView)
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.core.urlresolvers import reverse
from .models import RevelationModel
from .forms import RevelationModelForm


class UserProfileView(View):
    @staticmethod
    def get(request, pk):
        user = get_object_or_404(get_user_model(), pk=pk)
        revelations = RevelationModel.objects.filter(user=user,
                                                     public=True)
        return render(request, 'core/user_profile.html',
                      {'object_list': revelations, 'profile': user})


class RevelationModelListView(ListView):
    model = RevelationModel
    paginate_by = 50

    def get_queryset(self):
        return self.model.objects.filter(public=True)


class RevelationModelCreateView(CreateView):
    model = RevelationModel
    form_class = RevelationModelForm
    object = None

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        # Set current user
        if self.request.user.is_authenticated():
            form.instance.user = self.request.user
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class RevelationModelDeleteView(DeleteView):
    model = RevelationModel

    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(RevelationModelDeleteView, self).get_object()
        if not obj.user == self.request.user or not obj.is_time_visible:
            raise Http404
        return obj

    def get_success_url(self):
        return reverse('user-view', args=[self.request.user.id])


class RevelationModelDetailView(DetailView):
    model = RevelationModel

    def get_object(self, queryset=None):
        obj = super(RevelationModelDetailView, self).get_object()
        # Object deleted
        if obj.deleted:
            raise Http404
        # Object self destruct
        if obj.self_destruct and obj.is_time_visible():
            obj.deleted = True
            obj.save()
        return obj

    def get_template_names(self):
        if not self.object.is_time_visible():
            return ['core/revelationmodel_countdown.html']
        return super(RevelationModelDetailView, self).get_template_names()


class HomePageView(TemplateView):
    template_name = "home.html"
