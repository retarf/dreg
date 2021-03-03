from django.shortcuts import render
from django.views import View
from django.views.generic.edit import FormView
from django.views.generic import TemplateView

from .forms import CompanyForm

from .pulling import Web
from .__realdata__ import ExampleWeb


class CompanyView(FormView):
    template_name = 'scrub/company.html'
    form_class = CompanyForm

    #def get_success_url(self):
    #    company = self.request.POST.get('name', None)

class DataView(View):

    def post(self, request, *args, **kwargs):
        template = 'scrub/data.html'
        name = request.POST.get('name')
        data = Web(ExampleWeb, name).data
        return render(request,
                      template,
                      {'columns': data.columns,
                       'rows': data.iterrows()})
