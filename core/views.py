from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import FormView

from .forms import infoForm


# Create your views here.

class info(FormView):
    template_name = 'core/info.html'
    form_class = infoForm

    def form_valid(self, form):
        name = form.cleaned_data['name']
        form.save()
        return JsonResponse({"name": name}, status=200)

    def form_invalid(self, form):
        errors = form.errors.as_json()
        return JsonResponse({"errors": errors}, status=400)
